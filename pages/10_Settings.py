import streamlit as st

st.set_page_config(
    page_title="MediCare | System Settings",
    page_icon="⚙️",
    layout="wide"
)

# ----------------- 🛡️ LOGIN GUARD -----------------
if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

# Custom CSS matching Theme & Dark Navy Blue Sidebar
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
    }
    [data-testid="stSidebar"] * {
        color: #f1f5f9 !important;
    }
    
    /* Red Logout Button Styling */
    [data-testid="stSidebar"] .stButton > button {
        background-color: #ef4444 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #dc2626 !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- ⚙️ INITIALIZE SETTINGS IN SESSION STATE -----------------
if "settings_config" not in st.session_state:
    st.session_state.settings_config = {
        "h_name": "MediCare Health Institute",
        "h_reg": "REG-2026-MH-9812",
        "h_addr": "123 Healthcare Ave, Metro City",
        "opd_open": "09:00",
        "opd_close": "20:00",
        "emergency": "24/7 Active",
        "beds_capacity": 200,
        "departments": ["Cardiology", "Emergency", "ICU"],
        "rbac_role": "Admin",
        "rbac_edit_patient": True,
        "2fa_enabled": True,
        "session_timeout": 30,
        "email_alerts": True,
        "sms_alerts": True,
        "backup_freq": "Daily",
        "theme": "Dark Navy Blue (Default)",
        "currency": "₹",
        "gst_rate": 18.0,
        "low_stock_limit": 10
    }

cfg = st.session_state.settings_config

# ----------------- UNIFORM SIDEBAR NAVIGATION -----------------
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="24" height="24" rx="6" fill="#2563EB"/>
            <path d="M8 12H16M12 8V16" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
        </svg>
        <h2 style="color: white; margin: 0; font-size: 22px; font-weight: 700;">MediCare</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption(f"Logged in: **{st.session_state.get('current_user', 'Admin')}**")
    st.write("")
    st.caption("MAIN MENU")
    
    st.page_link("app.py", label="Overview", icon="📊")
    st.page_link("pages/1_Analytics_Dashboard.py", label="Analytics", icon="📈")
    st.page_link("pages/2_Doctor_Directory.py", label="Doctor Directory", icon="👨‍⚕️")
    st.page_link("pages/3_Patient_Records.py", label="Patient Records", icon="👨‍👩‍👧‍👦")
    st.page_link("pages/4_Bed_Allocation.py", label="Bed Allocation", icon="🛏️")
    st.page_link("pages/5_Pharmacy_Inventory.py", label="Pharmacy Inventory", icon="💊")
    st.page_link("pages/6_Assign_Product.py", label="Assign Product", icon="📋")
    st.page_link("pages/7_Ambulance_Fleet.py", label="Ambulance Fleet", icon="🚑")
    st.page_link("pages/8_Schedule_Appointments.py", label="Schedule & Appointments", icon="📅")
    st.page_link("pages/9_Billing_System.py", label="Billing System", icon="💳")
    st.page_link("pages/10_Settings.py", label="Settings", icon="⚙️")
    st.page_link("pages/11_Help_Center.py", label="Help Center", icon="❓")
    
    st.divider()
    
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.switch_page("app.py")

st.title("⚙️ Functional System Settings")
st.caption("10 Functional Hospital Configuration Settings.")
st.write("")

# 1. Hospital Profile Information
st.markdown("### 1. Hospital Profile Information")
h_name = st.text_input("Hospital Name", value=cfg["h_name"])
h_reg = st.text_input("Registration / License Number", value=cfg["h_reg"])
h_addr = st.text_area("Official Address", value=cfg["h_addr"])
if st.button("💾 Save Profile Info", key="b1"):
    cfg["h_name"] = h_name
    cfg["h_reg"] = h_reg
    cfg["h_addr"] = h_addr
    st.success("Hospital Profile updated successfully in Session State!")

st.divider()

# 2. Operational Timings
st.markdown("### 2. Operational Timings & Emergency")
c1, c2 = st.columns(2)
with c1:
    open_t = st.text_input("OPD Opening Hours", value=cfg["opd_open"])
    close_t = st.text_input("OPD Closing Hours", value=cfg["opd_close"])
with c2:
    emerg = st.selectbox("Emergency Services Availability", ["24/7 Active", "Day Shift Only"], index=0 if cfg["emergency"] == "24/7 Active" else 1)
if st.button("💾 Save Operational Timings", key="b2"):
    cfg["opd_open"] = open_t
    cfg["opd_close"] = close_t
    cfg["emergency"] = emerg
    st.success("Operational timings saved!")

st.divider()

# 3. Bed Capacity & Department Config
st.markdown("### 3. Bed & Department Configuration")
beds = st.number_input("Total Hospital Bed Capacity", value=cfg["beds_capacity"], step=10)
deps = st.multiselect("Active Departments", ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Emergency", "ICU"], default=cfg["departments"])
if st.button("💾 Save Bed & Dept Config", key="b3"):
    cfg["beds_capacity"] = beds
    cfg["departments"] = deps
    st.success("Department and Bed configuration updated!")

st.divider()

# 4. User Roles & Access Control (RBAC)
st.markdown("### 4. User Access Controls (RBAC)")
role = st.selectbox("Select Role to Edit Permissions", ["Admin", "Doctor", "Nurse", "Receptionist", "Pharmacist"])
p_edit = st.checkbox("Allow Patient Data Editing", value=cfg["rbac_edit_patient"])
if st.button("💾 Save Role Permissions", key="b4"):
    cfg["rbac_role"] = role
    cfg["rbac_edit_patient"] = p_edit
    st.success(f"Permissions for role '{role}' updated!")

st.divider()

# 5. Security Settings
st.markdown("### 5. Security & Session Settings")
two_fa = st.checkbox("Enable Two-Factor Authentication (2FA)", value=cfg["2fa_enabled"])
timeout = st.number_input("Session Timeout (Minutes)", value=cfg["session_timeout"])
if st.button("💾 Save Security Settings", key="b5"):
    cfg["2fa_enabled"] = two_fa
    cfg["session_timeout"] = timeout
    st.success("Security settings updated!")

st.divider()

# 6. Notifications & Alert Preferences
st.markdown("### 6. Notifications & Alert Preferences")
n_email = st.checkbox("Email Alerts for Low Stock & System Updates", value=cfg["email_alerts"])
n_sms = st.checkbox("SMS Alerts for Patient Appointments", value=cfg["sms_alerts"])
if st.button("💾 Save Notification Settings", key="b6"):
    cfg["email_alerts"] = n_email
    cfg["sms_alerts"] = n_sms
    st.success("Notification preferences saved!")

st.divider()

# 7. Database Backup Settings
st.markdown("### 7. Database Backup & Management")
freq = st.selectbox("Auto Backup Frequency", ["Daily", "Weekly", "Monthly"], index=["Daily", "Weekly", "Monthly"].index(cfg["backup_freq"]))
if st.button("💾 Save Backup Schedule", key="b7"):
    cfg["backup_freq"] = freq
    st.success(f"Auto-backup frequency set to {freq}!")

st.divider()

# 8. Billing, Currency & Taxes
st.markdown("### 8. Billing, Currency & Taxes")
curr = st.text_input("Currency Symbol", value=cfg["currency"])
gst = st.number_input("Standard Tax / GST Rate (%)", value=cfg["gst_rate"])
if st.button("💾 Save Billing Settings", key="b8"):
    cfg["currency"] = curr
    cfg["gst_rate"] = gst
    st.success("Billing & Tax configurations updated!")

st.divider()

# 9. Pharmacy & Stock Thresholds
st.markdown("### 9. Pharmacy & Inventory Thresholds")
stock_limit = st.number_input("Global Low Stock Alert Level (Units)", value=cfg["low_stock_limit"])
if st.button("💾 Save Inventory Thresholds", key="b9"):
    cfg["low_stock_limit"] = stock_limit
    st.success(f"Low stock alert limit set to {stock_limit} units!")

st.divider()

# 10. System UI Theme
st.markdown("### 10. Interface Theme")
sys_theme = st.selectbox("System Theme Preference", ["Dark Navy Blue (Default)", "Light Mode", "High Contrast"])
if st.button("💾 Save Theme Settings", key="b10"):
    cfg["theme"] = sys_theme
    st.success("UI Theme preference saved!")