import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ambulance Fleet | HealthPlus", page_icon="🚑", layout="wide")

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
    st.title("🚑 Ambulance Fleet & Emergency Dispatch")
    st.caption("Real-time Tracking, Driver Allocation & Emergency Response")
with h_col2:
    st.write("")
    if st.button("🚪 Logout", key="top_logout_btn", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.query_params.clear()
        st.switch_page("app.py")

st.divider()

# ----------------- 📈 AMBULANCE METRICS -----------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Total Ambulances</div><div class="kpi-val">🚑 12</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">On Dispatch</div><div class="kpi-val">🚨 04</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Available</div><div class="kpi-val">🟢 07</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Maintenance</div><div class="kpi-val">⚠️ 01</div></div>', unsafe_allow_html=True)

st.write("")

# ----------------- 📝 DISPATCH FORM & TABLE -----------------
col_form, col_table = st.columns([1, 1.2])

with col_form:
    st.subheader("🚨 Emergency Dispatch Request")
    with st.form("ambulance_form"):
        p_name = st.text_input("Patient / Caller Name", placeholder="e.g. Ramesh Patil")
        location = st.text_input("Pickup Location", placeholder="e.g. Station Road, Near Bus Stand")
        ambulance_type = st.selectbox("Ambulance Type", ["Advanced Life Support (ALS)", "Basic Life Support (BLS)", "ICU Ambulance"])
        driver_pref = st.text_input("Assign Driver / Vehicle No", placeholder="e.g. MH-10-AB-1234")
        
        btn_dispatch = st.form_submit_button("Dispatch Ambulance", type="primary", use_container_width=True)
        if btn_dispatch:
            if p_name and location:
                st.success(f"Ambulance dispatched successfully to {location} for {p_name}!")
            else:
                st.warning("Please enter Patient Name and Location.")

with col_table:
    st.subheader("📋 Fleet Status & Live Tracking")
    amb_data = pd.DataFrame({
        "Vehicle No": ["MH-10-AB-1111", "MH-10-AB-2222", "MH-10-AB-3333", "MH-10-AB-4444", "MH-10-AB-5555"],
        "Type": ["ALS", "BLS", "ICU", "BLS", "ALS"],
        "Driver": ["Santosh K.", "Vijay M.", "Anil D.", "Prakash S.", "Kiran P."],
        "Status": ["On Dispatch", "Available", "On Dispatch", "Available", "Maintenance"],
        "Location": ["City Hospital", "Standby Zone", "Highway 4", "Standby Zone", "Workshop"]
    })
    st.dataframe(amb_data, use_container_width=True)