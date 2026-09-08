import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pharmacy Inventory | HealthPlus", page_icon="💊", layout="wide")

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
    st.title("💊 Pharmacy Inventory")
    st.caption("Medicine Stock, Prescriptions & Pharma Supply Logistics")
with h_col2:
    st.write("")
    if st.button("🚪 Logout", key="top_logout_btn", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.query_params.clear()
        st.switch_page("app.py")

st.divider()

# ----------------- 📈 PHARMA METRICS -----------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Total Medicines</div><div class="kpi-val">💊 1,240</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Low Stock Items</div><div class="kpi-val">⚠️ 18</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Expired Medicine</div><div class="kpi-val">🚨 03</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Daily Prescriptions</div><div class="kpi-val">🧾 156</div></div>', unsafe_allow_html=True)

st.write("")
st.subheader("📋 Medicine Stock Table")

# Sample Inventory Data Table
pharma_data = pd.DataFrame({
    "Medicine Name": ["Paracetamol 650mg", "Amoxicillin 500mg", "Ibuprofen 400mg", "Cetirizine 10mg", "Azithromycin 500mg"],
    "Category": ["Analgesic", "Antibiotic", "Anti-inflammatory", "Antihistamine", "Antibiotic"],
    "Stock Count": [450, 85, 230, 600, 42],
    "Unit Price (₹)": [15, 45, 25, 10, 120],
    "Status": ["In Stock", "Low Stock", "In Stock", "In Stock", "Low Stock"]
})

st.dataframe(pharma_data, use_container_width=True)