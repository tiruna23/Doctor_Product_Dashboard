import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bed Allocation | HealthPlus", page_icon="🛏️", layout="wide")

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
    st.title("🛏️ Bed Allocation & Ward Occupancy")
    st.caption("ICU, General Wards, Special Rooms & Bed Availability Tracker")
with h_col2:
    st.write("")
    if st.button("🚪 Logout", key="top_logout_btn", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.query_params.clear()
        st.switch_page("app.py")

st.divider()

# ----------------- 📈 BED METRICS -----------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Total Beds</div><div class="kpi-val">🛏️ 200</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Occupied Beds</div><div class="kpi-val">🔴 114</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Available Beds</div><div class="kpi-val">🟢 86</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">ICU Occupancy</div><div class="kpi-val">🚨 18 / 20</div></div>', unsafe_allow_html=True)

st.write("")

# ----------------- 📝 BED ALLOCATION & TABLE -----------------
col_form, col_table = st.columns([1, 1.2])

with col_form:
    st.subheader("➕ Allocate Bed to Patient")
    with st.form("allocate_bed_form"):
        patient_name = st.text_input("Patient ID / Name", placeholder="e.g. PAT-901 or Amit K.")
        ward_type = st.selectbox("Ward Type", ["ICU Ward", "General Male Ward", "General Female Ward", "Special Private Suite", "Emergency ER"])
        bed_no = st.text_input("Bed Number", placeholder="e.g. ICU-05 or B-12")
        doctor_assigned = st.text_input("Attending Doctor", placeholder="e.g. Dr. Sharma")
        
        btn_allocate = st.form_submit_button("Allocate Bed", type="primary", use_container_width=True)
        if btn_allocate:
            if patient_name and bed_no:
                st.success(f"Bed {bed_no} ({ward_type}) successfully allocated to {patient_name}.")
            else:
                st.warning("Please enter Patient Name and Bed Number.")

with col_table:
    st.subheader("📋 Current Bed Status")
    beds_data = pd.DataFrame({
        "Bed No": ["ICU-01", "ICU-02", "B-101", "B-102", "S-201", "S-202"],
        "Ward": ["ICU Ward", "ICU Ward", "General Ward", "General Ward", "Special Suite", "Special Suite"],
        "Status": ["Occupied", "Occupied", "Available", "Occupied", "Available", "Occupied"],
        "Patient": ["Rahul S.", "Priya M.", "Vacant", "Suresh P.", "Vacant", "Anil R."]
    })
    st.dataframe(beds_data, use_container_width=True)