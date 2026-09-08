import streamlit as st
import pandas as pd

st.set_page_config(page_title="Doctor Directory | HealthPlus", page_icon="👨‍⚕️", layout="wide")

if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

st.markdown("""
<style>
    .stApp { background: #f0fdf4 !important; }
    header { visibility: hidden; }
    [data-testid="stSidebar"] { background-color: #064e3b !important; display: block !important; }
    [data-testid="stSidebar"] * { color: #ecfdf5 !important; }
    div[data-testid="stColumn"]:has(button[key="top_logout_btn"]) button {
        background-color: #dc2626 !important; color: #ffffff !important; border: none !important; font-weight: 600 !important; border-radius: 10px !important;
    }
    .kpi-card { background: #ffffff; border-radius: 16px; padding: 20px; border: 1px solid #d1fae5; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03); }
    .kpi-title { font-size: 13px; color: #047857; font-weight: 700; text-transform: uppercase; }
    .kpi-val { font-size: 26px; font-weight: 800; color: #064e3b; margin: 6px 0; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='color: #a7f3d0; margin-bottom: 20px;'>🩺 HealthPlus</h2>", unsafe_allow_html=True)
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

h_col1, h_col2 = st.columns([3, 1])
with h_col1:
    st.title("👨‍⚕️ Doctor Directory & Specialists")
    st.caption("Manage Hospital Specialists, On-Duty Rosters & Consultation Timings")
with h_col2:
    st.write("")
    if st.button("🚪 Logout", key="top_logout_btn", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.query_params.clear()
        st.switch_page("app.py")

st.divider()

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Total Doctors</div><div class="kpi-val">👨‍⚕️ 45</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">On Duty Today</div><div class="kpi-val">🟢 32</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Specialists</div><div class="kpi-val">⭐ 18</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">On Leave</div><div class="kpi-val">🌴 03</div></div>', unsafe_allow_html=True)

st.write("")
col_form, col_table = st.columns([1, 1.2])

with col_form:
    st.subheader("➕ Add New Doctor")
    with st.form("doctor_form"):
        doc_name = st.text_input("Doctor Name", placeholder="e.g. Dr. Rajesh Sharma")
        doc_spec = st.selectbox("Specialization", ["Cardiologist", "Pediatrician", "Orthopedic", "Neurologist", "Dermatologist", "General Surgeon"])
        doc_shift = st.selectbox("Shift Timing", ["Morning (08:00 AM - 02:00 PM)", "Evening (02:00 PM - 08:00 PM)", "Night (08:00 PM - 08:00 AM)"])
        doc_contact = st.text_input("Phone Number", placeholder="e.g. 9811223344")
        
        btn_doc = st.form_submit_button("Add Doctor", type="primary", use_container_width=True)
        if btn_doc:
            if doc_name:
                st.success(f"{doc_name} added successfully to directory!")
            else:
                st.warning("Please enter doctor name.")

with col_table:
    st.subheader("📋 On-Duty Doctor Roster")
    doc_df = pd.DataFrame({
        "Doctor Name": ["Dr. Rajesh Sharma", "Dr. Priya Deshmukh", "Dr. Amit Kothari", "Dr. Sneha Joshi", "Dr. Vikramaditya"],
        "Specialty": ["Cardiologist", "Pediatrician", "Orthopedic", "Dermatologist", "Neurologist"],
        "Shift": ["Morning", "Evening", "Morning", "Night", "Morning"],
        "Status": ["Available", "In Surgery", "Available", "On Leave", "Available"]
    })
    st.dataframe(doc_df, use_container_width=True)