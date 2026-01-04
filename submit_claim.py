import streamlit as st
from utils import load_design_system, render_header

# 1. Load Design
load_design_system()
render_header()

# 2. Main Layout
st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>File a New Claim</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B; margin-bottom: 40px;'>Upload photos and details. Our AI will handle the rest in seconds.</p>", unsafe_allow_html=True)

# Container for the content to center it nicely
with st.container():
    col1, col2 = st.columns([1, 1.5], gap="large")

    # --- LEFT COLUMN: IMAGE UPLOAD ---
    with col1:
        st.markdown('<div class="css-card">', unsafe_allow_html=True)
        st.markdown("### 📸 Evidence Upload")
        st.info("Supported: JPG, PNG. Max size: 10MB")
        
        uploaded_file = st.file_uploader("Drop your crash photo here", type=['png', 'jpg'], label_visibility="collapsed")
        
        if uploaded_file:
            st.image(uploaded_file, caption="Preview", use_column_width=True)
            st.success("Image analyzed successfully!")
        else:
            # Placeholder for visual balance
            st.markdown("""
                <div style="height: 200px; border: 2px dashed #CBD5E1; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #94A3B8;">
                    No Image Selected
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- RIGHT COLUMN: DETAILS FORM ---
    with col2:
        st.markdown('<div class="css-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Incident Details")
        
        # Row 1
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            policy_num = st.text_input("Policy Number", placeholder="e.g. POL-88221")
        with r1c2:
            date = st.date_input("Date of Incident")

        # Row 2
        r2c1, r2c2 = st.columns(2)
        with r2c1:
            severity = st.selectbox("Self-Assessed Severity", ["Minor Scratch", "Moderate Dent", "Major Damage", "Total Loss"])
        with r2c2:
            collision_type = st.selectbox("Collision Type", ["Single Vehicle", "Multi-Vehicle", "Stationary Object", "Other"])

        # Row 3
        description = st.text_area("Description", placeholder="Describe what happened...", height=100)
        
        # Submit Button (Full Width via CSS)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Analyze & Submit Claim"):
            if not uploaded_file:
                st.error("Please upload an image first.")
            else:
                # This is where we would trigger the backend logic
                st.markdown("""
                    <div class="success-box">
                        <b>Success!</b> Claim #8821 submitted. Analysis in progress...
                    </div>
                """, unsafe_allow_html=True)
                
        st.markdown('</div>', unsafe_allow_html=True)