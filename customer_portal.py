import streamlit as st
import time
from utils import load_design_system, render_header

def render_submission_form():
    """
    Renders the 'Submit Your Claim' input form (Image 4).
    """
    st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Submit Your Claim</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; margin-bottom: 40px;'>Upload your accident image and provide claim details for instant analysis</p>", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns([1, 1.5], gap="large")

        # --- LEFT: IMAGE UPLOAD ---
        with col1:
            st.markdown('<div class="css-card">', unsafe_allow_html=True)
            st.markdown("### 📤 Upload a car damage image")
            
            uploaded_file = st.file_uploader("Drop your crash photo here", type=['png', 'jpg'], label_visibility="collapsed")
            
            if uploaded_file:
                st.image(uploaded_file, caption="41-major (2).png", use_container_width=True)
                st.markdown(f"<div style='text-align:center; color: #64748B; font-size: 0.8rem; margin-top: 5px;'>{uploaded_file.name} (1.7 MB)</div>", unsafe_allow_html=True)
                # Store in session state for the next page
                st.session_state['uploaded_image'] = uploaded_file
            else:
                st.markdown("""
                    <div style='height: 200px; border: 2px dashed #CBD5E1; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #94A3B8; flex-direction: column; gap: 10px;'>
                        <div style='font-size: 2rem;'>📄</div>
                        <div>Drag and drop or click to browse</div>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- RIGHT: CLAIM DETAILS ---
        with col2:
            st.markdown('<div class="css-card">', unsafe_allow_html=True)
            st.markdown("### Claim Details")
            st.caption("Please provide accurate information about your incident")
            
            # Form Inputs
            c1, c2 = st.columns(2)
            with c1: st.text_input("Policy Number *", value="12345")
            with c2: st.text_input("Accident Location *", value="Munich")
            
            c3, c4 = st.columns(2)
            with c3: st.text_input("Claim Amount ($) *", value="20000")
            with c4: st.date_input("Accident Date *")
            
            c5, c6 = st.columns(2)
            with c5: st.selectbox("Self-Assessed Severity *", ["Major", "Minor", "Moderate"])
            with c6: st.selectbox("Collision Type *", ["Rollover", "Front-end", "Rear-end", "Side-impact"])
            
            st.selectbox("Vehicles Involved *", ["1 Vehicle", "2 Vehicles", "3+ Vehicles"])
            st.text_area("Additional Notes", placeholder="Provide any additional details...")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # SUBMIT ACTION
            if st.button("Submit Claim"):
                if not uploaded_file:
                    st.error("Please upload an image first.")
                else:
                    with st.spinner("Analyzing image with Computer Vision..."):
                        time.sleep(1.5) # Simulate API call
                        st.session_state['page'] = 'results'
                        st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)

def render_results_page():
    """
    Renders the 'Claim Analysis Results' page (Image 6).
    """
    st.markdown("<h1 style='text-align: center; margin-bottom: 40px;'>Claim Analysis Results</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; margin-top: -30px; margin-bottom: 40px;'>Your claim has been analyzed using AI-powered image recognition</p>", unsafe_allow_html=True)

    # --- SUCCESS BANNER ---
    st.markdown("""
        <div style="background-color: #ECFDF5; border: 1px solid #10B981; border-radius: 12px; padding: 2rem; text-align: center; margin-bottom: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #065F46; margin-bottom: 10px;">
                🎉 Congratulations! Your claim has been approved.
            </div>
            <div style="color: #047857; margin-bottom: 20px;">
                You will receive your refund within 3-5 business days.
            </div>
            <div style="font-size: 0.875rem; color: #064E3B; background: rgba(255,255,255,0.5); display: inline-block; padding: 5px 15px; border-radius: 20px;">
                Claim Number: <strong>235284a4-b650-496e</strong> &nbsp; • &nbsp; Status: <strong>Approved</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- CIRCULAR CHECKS (Image 6 Bottom) ---
    st.markdown('<div class="css-card" style="max-width: 800px; margin: 0 auto;">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-bottom: 30px;'>Policy Form Analysis Results</h3>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    
    def render_circle(label, icon, color="#10B981"):
        return f"""
            <div style="text-align: center;">
                <div style="width: 60px; height: 60px; background-color: {color}; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin: 0 auto 15px auto; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    {icon}
                </div>
                <div style="font-weight: 600; color: #334155;">{label}</div>
            </div>
        """

    c1.markdown(render_circle("Image Severity", "✓"), unsafe_allow_html=True)
    c2.markdown(render_circle("Policy Amount", "🛡️"), unsafe_allow_html=True)
    c3.markdown(render_circle("Policy Data", "📊"), unsafe_allow_html=True)
    c4.markdown(render_circle("Speed Check", "📄"), unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Reset Button
    if st.button("Submit Another Claim"):
        st.session_state['page'] = 'form'
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)


# --- MAIN APP LOOP ---
def main():
    load_design_system()
    render_header()
    
    if 'page' not in st.session_state:
        st.session_state['page'] = 'form'
        
    if st.session_state['page'] == 'form':
        render_submission_form()
    else:
        render_results_page()

if __name__ == "__main__":
    main()