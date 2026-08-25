import streamlit as st

def show_sidebar():
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                background-color: #0b1727 !important;
                min-width: 260px !important;
            }
            [data-testid="stSidebar"] * {
                color: #94a3b8 !important;
            }
            .nav-header {
                font-size: 18px;
                font-weight: 800;
                color: #ffffff !important;
                padding: 10px 5px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown('<div class="nav-header">🏥 MediCare Admin</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    # Navigation Links to pages
    st.sidebar.page_link("app.py", label="Overview", icon="🏠")
    st.sidebar.page_link("pages/1_Analytics_Dashboard.py", label="Analytics", icon="📊")
    st.sidebar.page_link("pages/2_Doctor_Directory.py", label="Doctor Directory", icon="👨‍⚕️")
    st.sidebar.page_link("pages/3_Patient_Records.py", label="Patient Records", icon="👤")
    st.sidebar.page_link("pages/4_Bed_Allocation.py", label="Bed Allocation", icon="🛏️")
    st.sidebar.page_link("pages/5_Pharmacy_Inventory.py", label="Pharmacy Inventory", icon="💊")
    st.sidebar.page_link("pages/6_Assign_Product.py", label="Assign Product", icon="📦")
    st.sidebar.page_link("pages/7_Ambulance_Fleet.py", label="Ambulance Fleet", icon="🚑")
    st.sidebar.page_link("pages/8_Schedule_Appointments.py", label="Schedule & Appointments", icon="📅")
    st.sidebar.page_link("pages/9_Billing_System.py", label="Billing System", icon="🧾")
    st.sidebar.page_link("pages/10_Settings.py", label="Settings", icon="⚙️")
    st.sidebar.page_link("pages/11_Help_Center.py", label="Help Center", icon="❓")