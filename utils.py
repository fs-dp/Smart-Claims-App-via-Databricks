import streamlit as st

def load_design_system():
    """
    Injects the complete CSS Design System for the Smart Claims App.
    Includes global resets, component styling, and utility classes for the Admin Dashboard.
    """
    
    # 1. Page Configuration
    st.set_page_config(
        page_title="Smart Claims Portal",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # 2. Custom CSS Injection
    st.markdown("""
        <style>
            /* --- 1. GLOBAL TYPOGRAPHY & RESET --- */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
            
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: #F8FAFC; /* Slate-50: Light Blue-Gray Background */
                color: #1E293B; /* Slate-800 */
            }

            /* Hide default Streamlit elements for a cleaner look */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Remove default top padding */
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
            }

            /* --- 2. CONTAINER COMPONENT (CARDS) --- */
            /* We disable the default background of vertical blocks */
            div[data-testid="stVerticalBlock"] > div {
                background-color: transparent;
            }
            
            /* The 'css-card' class is used to wrap content in white boxes */
            .css-card {
                background-color: white;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                border: 1px solid #E2E8F0;
                margin-bottom: 1.5rem;
            }

            /* --- 3. INPUTS & INTERACTION --- */
            /* Buttons - Databricks Electric Orange Theme */
            .stButton > button {
                width: 100%;
                background-color: #FF3621; 
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0.75rem 1.5rem;
                font-weight: 600;
                letter-spacing: 0.025em;
                transition: all 0.2s ease;
            }
            .stButton > button:hover {
                background-color: #D92B19;
                box-shadow: 0 4px 12px rgba(255, 54, 33, 0.25);
                color: white;
            }
            .stButton > button:focus {
                color: white;
            }

            /* Text Inputs & Select Boxes */
            .stTextInput > div > div > input, .stSelectbox > div > div > div {
                border-radius: 8px;
                border: 1px solid #CBD5E1;
                color: #334155;
            }
            .stTextInput > div > div > input:focus {
                border-color: #FF3621;
                box-shadow: 0 0 0 2px rgba(255, 54, 33, 0.2);
            }

            /* --- 4. MESSAGING & ALERTS --- */
            .success-box {
                background-color: #ECFDF5;
                border: 1px solid #10B981;
                color: #065F46;
                padding: 1rem;
                border-radius: 8px;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                font-weight: 500;
            }

            /* --- 5. ADMIN DASHBOARD SPECIFICS --- */
            
            /* KPI Cards (Top Row) */
            .metric-container {
                background-color: white;
                padding: 1.5rem;
                border-radius: 10px;
                border: 1px solid #E2E8F0;
                box-shadow: 0 1px 3px rgba(0,0,0,0.05);
                text-align: center;
                height: 100%;
            }
            .metric-label {
                color: #64748B;
                font-size: 0.75rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                margin-top: 10px;
            }
            .metric-value {
                color: #0F172A;
                font-size: 1.75rem;
                font-weight: 700;
                margin-top: 0.25rem;
            }

            /* Status Badges (Pills) */
            .badge {
                padding: 4px 10px;
                border-radius: 9999px;
                font-size: 0.75rem;
                font-weight: 600;
                display: inline-block;
                text-align: center;
                min-width: 80px;
            }
            .badge-blue { background-color: #EFF6FF; color: #1D4ED8; border: 1px solid #BFDBFE; }
            .badge-green { background-color: #ECFDF5; color: #047857; border: 1px solid #A7F3D0; }
            .badge-red { background-color: #FEF2F2; color: #B91C1C; border: 1px solid #FECACA; }
            .badge-gray { background-color: #F1F5F9; color: #475569; border: 1px solid #E2E8F0; }

            /* Data Grid Headers */
            .grid-header {
                font-weight: 600;
                font-size: 0.875rem;
                color: #64748B;
                border-bottom: 2px solid #E2E8F0;
                padding-bottom: 8px;
                margin-bottom: 12px;
                text-transform: uppercase;
                letter-spacing: 0.025em;
            }

            /* --- 6. HEADERS --- */
            h1 { color: #0F172A; font-weight: 700; letter-spacing: -0.025em; }
            h2, h3 { color: #334155; font-weight: 600; }
            
        </style>
    """, unsafe_allow_html=True)

def render_header():
    """
    Renders the top navigation bar with Logo and User Profile.
    """
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 1rem 0; margin-bottom: 2rem; border-bottom: 1px solid #E2E8F0; background-color: #F8FAFC;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="background-color: #FF3621; width: 32px; height: 32px; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">S</div>
                <span style="font-weight: 700; font-size: 1.25rem; color: #0F172A;">SmartClaims</span>
            </div>
            <div style="display: flex; align-items: center; gap: 24px;">
                <a href="#" style="text-decoration: none; color: #64748B; font-weight: 500; font-size: 0.875rem;">Dashboard</a>
                <a href="#" style="text-decoration: none; color: #64748B; font-weight: 500; font-size: 0.875rem;">My Policies</a>
                <a href="#" style="text-decoration: none; color: #64748B; font-weight: 500; font-size: 0.875rem;">Support</a>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <div style="width: 32px; height: 32px; background-color: #EFF6FF; color: #1D4ED8; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.875rem;">LD</div>
                    <span style="font-size: 0.875rem; font-weight: 600; color: #334155;">Lotta Dietz</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)