import streamlit as st
import pandas as pd

st.set_page_config(page_title="Patient Records | HealthPlus", page_icon="👨‍👩‍👧‍👦", layout="wide")

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
    st.title("👨‍👩‍👧‍👦 Patient Records & EHR")
    st.caption("Electronic Health Records, Admissions & Patient Database")
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
    st.markdown('<div class="kpi-card"><div class="kpi-title">Total Patients</div><div class="kpi-val">👥 1,850</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Currently Admitted</div><div class="kpi-val">🏥 114</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Discharged Today</div><div class="kpi-val">🏡 22</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Critical Cases</div><div class="kpi-val">🚨 08</div></div>', unsafe_allow_html=True)

st.write("")
col_form, col_table = st.columns([1, 1.2])

with col_form:
    st.subheader("➕ Register New Patient")
    with st.form("patient_form"):
        p_name = st.text_input("Full Name", placeholder="e.g. Rahul Sharma")
        p_age = st.number_input("Age", min_value=0, max_value=120, value=30)
        p_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        p_contact = st.text_input("Contact Number", placeholder="e.g. 9876543210")
        p_illness = st.text_input("Diagnosis / Symptom", placeholder="e.g. Viral Fever / Cardiac Check")
        
        btn_pat = st.form_submit_button("Save Patient Record", type="primary", use_container_width=True)
        if btn_pat:
            if p_name:
                st.success(f"Patient {p_name} registered successfully!")
            else:
                st.warning("Please enter patient name.")

with col_table:
    st.subheader("📋 Patient Database Directory")
    patient_df = pd.DataFrame({
        "ID": ["PAT-101", "PAT-102", "PAT-103", "PAT-104", "PAT-105"],
        "Name": ["Rahul Sharma", "Priya More", "Amit Kothari", "Sneha Joshi", "Anil Patil"],
        "Age": [34, 28, 45, 52, 39],
        "Gender": ["Male", "Female", "Male", "Female", "Male"],
        "Status": ["Admitted", "Discharged", "Admitted", "ICU", "Admitted"]
    })
    st.dataframe(patient_df, use_container_width=True)