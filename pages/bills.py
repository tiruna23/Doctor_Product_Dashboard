import streamlit as st
import pandas as pd

st.set_page_config(page_title="Billing System | HealthPlus", page_icon="💳", layout="wide")

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
    st.title("💳 Billing & Invoicing System")
    st.caption("Patient Accounts, Payment Gateways & Discharge Invoicing")
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
    st.markdown('<div class="kpi-card"><div class="kpi-title">Today Collection</div><div class="kpi-val">💰 ₹1,45,200</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Pending Invoices</div><div class="kpi-val">⏳ 12</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Insurance Claims</div><div class="kpi-val">🏥 08</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Total Bills Generated</div><div class="kpi-val">🧾 450</div></div>', unsafe_allow_html=True)

st.write("")
col_form, col_table = st.columns([1, 1.2])

with col_form:
    st.subheader("🧾 Generate Patient Bill")
    with st.form("billing_form"):
        p_bill_name = st.text_input("Patient Name / ID", placeholder="e.g. Sachin Tendulkar")
        room_charges = st.number_input("Room & Ward Charges (₹)", min_value=0.0, value=5000.0)
        med_charges = st.number_input("Pharmacy & Medicines (₹)", min_value=0.0, value=2500.0)
        doc_fees = st.number_input("Doctor Consultation Fees (₹)", min_value=0.0, value=1500.0)
        
        btn_gen = st.form_submit_button("Calculate & Generate Bill", type="primary", use_container_width=True)
        if btn_gen:
            total = room_charges + med_charges + doc_fees
            st.success(f"Bill generated successfully! Total Amount: ₹{total}")

with col_table:
    st.subheader("📋 Recent Invoices")
    bills_data = pd.DataFrame({
        "Bill ID": ["INV-501", "INV-502", "INV-503", "INV-504"],
        "Patient": ["Rahul S.", "Anita P.", "Suresh K.", "Priya M."],
        "Amount (₹)": [18500, 42000, 9500, 31000],
        "Payment Mode": ["Insurance", "UPI", "Cash", "Credit Card"],
        "Status": ["Paid", "Paid", "Pending", "Paid"]
    })
    st.dataframe(bills_data, use_container_width=True)