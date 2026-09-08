import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analytics & Reports | HealthPlus", page_icon="📈", layout="wide")

# ----------------- 🔐 LOGIN GUARD & SESSION CHECK -----------------
if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

# ----------------- 🎨 THEME & STYLING -----------------
st.markdown("""
<style>
    .stApp { background: #f0fdf4 !important; }
    header { visibility: hidden; }
    
    [data-testid="stSidebar"] {
        background-color: #064e3b !important;
        display: block !important;
    }
    [data-testid="stSidebar"] * { color: #ecfdf5 !important; }

    /* Top Right Logout Button */
    div[data-testid="stColumn"]:has(button[key="top_logout_btn"]) button {
        background-color: #dc2626 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
    }

    .kpi-card { 
        background: #ffffff; 
        border-radius: 16px; 
        padding: 20px; 
        border: 1px solid #d1fae5;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
    }
    .kpi-title { font-size: 13px; color: #047857; font-weight: 700; text-transform: uppercase; }
    .kpi-val { font-size: 26px; font-weight: 800; color: #064e3b; margin: 6px 0; }
</style>
""", unsafe_allow_html=True)

# ----------------- 🧭 SIDEBAR NAVIGATION -----------------
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <h2 style="color: #a7f3d0; margin: 0; font-size: 24px;">🩺 HealthPlus</h2>
    </div>
    """, unsafe_allow_html=True)
        
    st.caption(f"Active Session: **{st.session_state.get('current_user', 'Admin')}**")
    st.write("")
    st.caption("NAVIGATION MENU")
    
    st.page_link("app.py", label="Overview", icon="📊")
    st.page_link("pages/Analytics.py", label="Analytics", icon="📈")
    st.page_link("pages/doctors.py", label="Doctor Directory", icon="👨‍⚕️")
    st.page_link("pages/patient.py", label="Patient Records", icon="👨‍👩‍👧‍👦")
    st.page_link("pages/beds.py", label="Bed Allocation", icon="🛏️")
    st.page_link("pages/pharma.py", label="Pharmacy Inventory", icon="💊")
    st.page_link("pages/products.py", label="Assign Product", icon="📋")
    st.page_link("pages/ambulances.py", label="Ambulance Fleet", icon="🚑")
    st.page_link("pages/appointments.py", label="Schedule & Appointments", icon="📅")
    st.page_link("pages/bills.py", label="Billing System", icon="💳")

# ----------------- 📊 HEADER & TOP RIGHT LOGOUT -----------------
h_col1, h_col2 = st.columns([3, 1])
with h_col1:
    st.title("📈 Analytics & Hospital Performance")
    st.caption("Insights, Revenue Trends, Departmental Load & Patient Statistics")
with h_col2:
    st.write("")
    if st.button("🚪 Logout", key="top_logout_btn", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.query_params.clear()
        st.switch_page("app.py")

st.divider()

# ----------------- 📈 ANALYTICS METRICS -----------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Monthly Revenue</div><div class="kpi-val">💰 45.8L</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Bed Occupancy Rate</div><div class="kpi-val">🛏️ 78.5%</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Avg Recovery Time</div><div class="kpi-val">⏱️ 4.2 Days</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Patient Satisfaction</div><div class="kpi-val">⭐ 94.2%</div></div>', unsafe_allow_html=True)

st.write("")

# ----------------- 📊 MULTI-LINE TRENDS GRAPH -----------------
st.subheader("📊 Monthly Patient Admission Trends & Department Performance")

# Creating structured multi-line dataframe matching image 2 style
chart_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Cardiology": [40, 65, 45, 80, 50, 75],
    "Pediatrics": [55, 30, 50, 42, 48, 46],
    "Orthopedics": [75, 48, 52, 20, 60, 60]
})

st.line_chart(chart_data.set_index("Month"))