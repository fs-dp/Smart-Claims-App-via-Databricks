import streamlit as st
from utils import load_design_system, render_header

# --- MOCK DATA (In real app, this comes from Databricks SQL) ---
MOCK_CLAIMS = [
    {"id": "CLM-8821", "policy": "66777", "date": "Aug 16, 2025", "amount": "$12,345", "severity": "Major", "status": "Under Review", "risk": "30%", "img": "car_crash_1.jpg"},
    {"id": "CLM-9923", "policy": "76283", "date": "Aug 16, 2025", "amount": "$5,000", "severity": "Minor", "status": "Processed", "risk": "5%", "img": "car_crash_2.jpg"},
    {"id": "CLM-1102", "policy": "12345", "date": "Aug 15, 2025", "amount": "$30,000", "severity": "Major", "status": "Under Review", "risk": "85%", "img": "car_crash_3.jpg"},
]

def render_kpi_card(label, value, icon):
    st.markdown(f"""
        <div class="metric-container">
            <div style="font-size: 1.5rem; margin-bottom: 10px;">{icon}</div>
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)

def render_list_view():
    st.markdown("### 📋 All Claims Management")
    
    # 1. TOP KPI ROW
    k1, k2, k3, k4 = st.columns(4)
    with k1: render_kpi_card("Total Claims", "4,528", "📄")
    with k2: render_kpi_card("Total Loss", "2,485", "📅") # Icon placeholder
    with k3: render_kpi_card("Major Damage", "1,631", "👁️")
    with k4: render_kpi_card("Total Amount", "$237.9M", "💲")

    st.markdown("---")

    # 2. FILTERS
    f1, f2 = st.columns([3, 1])
    with f1:
        st.text_input("Search", placeholder="Search by Claim ID or Policy...", label_visibility="collapsed")
    with f2:
        st.selectbox("Filter Status", ["All Status", "Under Review", "Processed"], label_visibility="collapsed")

    # 3. CUSTOM DATA GRID
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Header
    h1, h2, h3, h4, h5, h6, h7 = st.columns([1.5, 1.5, 1.5, 1, 1, 1, 1])
    headers = ["Claim Number", "Policy", "Date", "Amount", "Severity", "Status", "Action"]
    for col, h in zip([h1, h2, h3, h4, h5, h6, h7], headers):
        col.markdown(f"<div class='grid-header'>{h}</div>", unsafe_allow_html=True)

    # Rows
    for claim in MOCK_CLAIMS:
        c1, c2, c3, c4, c5, c6, c7 = st.columns([1.5, 1.5, 1.5, 1, 1, 1, 1])
        
        with c1: st.write(f"**{claim['id']}**")
        with c2: st.caption(claim['policy'])
        with c3: st.write(claim['date'])
        with c4: st.write(claim['amount'])
        with c5: 
            # Conditional Formatting for Severity
            color = "#EF4444" if claim['severity'] == "Major" else "#10B981"
            st.markdown(f"<span style='color:{color}; font-weight:600'>● {claim['severity']}</span>", unsafe_allow_html=True)
        with c6:
            # Badge CSS
            badge_class = "badge-blue" if claim['status'] == "Under Review" else "badge-green"
            st.markdown(f"<span class='badge {badge_class}'>{claim['status']}</span>", unsafe_allow_html=True)
        with c7:
            if st.button("👁️ View", key=claim['id']):
                # SET STATE TO VIEW DETAIL
                st.session_state['current_view'] = 'detail'
                st.session_state['selected_claim'] = claim
                st.rerun()
        
        st.markdown("<div style='border-bottom: 1px solid #F1F5F9; margin-bottom: 10px;'></div>", unsafe_allow_html=True)

def render_detail_view():
    claim = st.session_state.get('selected_claim', MOCK_CLAIMS[0])
    
    # Breadcrumb / Back Button
    if st.button("← Back to List"):
        st.session_state['current_view'] = 'list'
        st.rerun()

    st.markdown(f"## 🔍 Investigation: {claim['id']}")

    # --- RULE ENGINE RESULTS (Top Section of Image 5) ---
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.markdown("#### ⚙️ Automated Rule Engine Results")
    
    r1, r2, r3, r4 = st.columns(4)
    
    # Helper for Check Results
    def check_box(label, status, subtext):
        icon = "✅" if status == "PASS" else "⚠️"
        color = "green" if status == "PASS" else "orange"
        return f"""
        <div style="text-align: center; padding: 10px; background: #F8FAFC; border-radius: 8px;">
            <div style="color: #64748B; font-size: 0.8rem;">{label}</div>
            <div style="font-size: 1.2rem; font-weight: 700; color: {color}; margin: 5px 0;">{icon} {status}</div>
            <div style="font-size: 0.75rem; color: #94A3B8;">{subtext}</div>
        </div>
        """

    r1.markdown(check_box("Severity Check", "PASS", "AI matches User input"), unsafe_allow_html=True)
    r2.markdown(check_box("Policy Amount", "PASS", "Within Limit ($50k)"), unsafe_allow_html=True)
    r3.markdown(check_box("Policy Active", "PASS", "Active until 12/2025"), unsafe_allow_html=True)
    r4.markdown(check_box("Speed Check", "WARN", "44mph in 35mph zone"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- MAIN CONTENT ---
    c1, c2, c3 = st.columns([1, 1.5, 1])
    
    # Left: Claim Details
    with c1:
        st.markdown('<div class="css-card">', unsafe_allow_html=True)
        st.markdown("#### Claim Details")
        st.markdown(f"**Incident Type:** Multi-Vehicle")
        st.markdown(f"**Collision:** Front-End")
        st.markdown(f"**Vehicles:** 2")
        st.divider()
        st.metric("Total Claim Amount", claim['amount'])
        st.markdown('</div>', unsafe_allow_html=True)

    # Middle: The Image (Centerpiece)
    with c2:
        st.markdown('<div class="css-card" style="text-align:center;">', unsafe_allow_html=True)
        st.markdown("#### 📸 Accident Image")
        # Placeholder image logic
        st.image("https://placehold.co/600x400/png?text=Car+Damage+Evidence", caption="Uploaded Evidence", use_column_width=True)
        st.info("AI Detected: Major Damage (98% Confidence)")
        st.markdown('</div>', unsafe_allow_html=True)

    # Right: Customer Info & Action
    with c3:
        st.markdown('<div class="css-card">', unsafe_allow_html=True)
        st.markdown("#### 👤 Customer")
        st.markdown("**Lotta Dietz**")
        st.caption("Policy #10212")
        st.caption("Munich, Germany")
        st.divider()
        
        st.markdown("#### Decision")
        if st.button("✅ Approve Claim", type="primary"):
            st.success("Claim Approved & Payment Scheduled")
        if st.button("❌ Reject Claim"):
            st.error("Claim Rejected. Email sent to customer.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN EXECUTION ---
def main():
    load_design_system()
    render_header()
    
    # Initialize State
    if 'current_view' not in st.session_state:
        st.session_state['current_view'] = 'list'

    # Router
    if st.session_state['current_view'] == 'list':
        render_list_view()
    else:
        render_detail_view()

if __name__ == "__main__":
    main()