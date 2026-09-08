import streamlit as st
import pandas as pd

st.set_page_config(page_title="Assign Product | HealthPlus", page_icon="📋", layout="wide")

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
    st.title("📋 Assign Product & Equipment")
    st.caption("Allocate Medical Equipment, Assets, & Surgical Products to Wards / Patients")
with h_col2:
    st.write("")
    if st.button("🚪 Logout", key="top_logout_btn", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.query_params.clear()
        st.switch_page("app.py")

st.divider()

# ----------------- 📝 ASSIGN PRODUCT FORM -----------------
col_form, col_assigned = st.columns([1, 1])

with col_form:
    st.subheader("➕ Assign Product / Equipment")
    with st.form("assign_product_form"):
        p_name = st.text_input("Patient ID / Name", placeholder="e.g. PAT-892 or Rahul Sharma")
        equipment = st.selectbox("Select Equipment / Product", [
            "Oxygen Concentrator 10L",
            "Patient Monitor (ECG/SpO2)",
            "Wheelchair (Standard)",
            "IV Infusion Pump",
            "Nebulizer Machine"
        ])
        dept = st.selectbox("Department / Ward", ["ICU Ward", "General Ward A", "General Ward B", "Emergency ER"])
        quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)
        
        btn_assign = st.form_submit_button("Assign Product", type="primary", use_container_width=True)
        if btn_assign:
            st.success(f"Successfully assigned {quantity} x {equipment} to {p_name} ({dept}).")

with col_assigned:
    st.subheader("📌 Recently Assigned Inventory")
    assigned_df = pd.DataFrame({
        "Patient/Ward": ["PAT-892 (Rahul S.)", "ICU Room #04", "General Ward B", "PAT-712 (Anita P.)"],
        "Item": ["Oxygen Concentrator", "ECG Monitor", "IV Infusion Pump", "Wheelchair"],
        "Qty": [1, 2, 1, 1],
        "Status": ["Assigned", "Active", "Active", "Assigned"]
    })
    st.dataframe(assigned_df, use_container_width=True)