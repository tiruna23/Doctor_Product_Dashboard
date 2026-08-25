import streamlit as st

st.set_page_config(
    page_title="MediCare | System Settings",
    page_icon="⚙️",
    layout="wide"
)

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
    
    .section-box {
        background: #ffffff;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR NAVIGATION -----------------
with st.sidebar:
    st.markdown("### 🏥 MediCare")
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

st.title("⚙️ System Settings")
st.caption("Manage all 12 core hospital settings sequentially.")
st.write("")

# 1. Hospital Profile Information
st.markdown("### 1. Hospital Profile Information")
st.text_input("Hospital Name", value="MediCare Health Institute", key="s1_name")
st.text_input("Registration / License Number", value="REG-2026-MH-9812", key="s1_reg")
st.text_area("Official Address", value="123 Healthcare Ave, Metro City", key="s1_addr")
if st.button("Save Profile Info", key="btn1"):
    st.success("Hospital Profile updated!")

st.divider()

# 2. Operational Timings & Shifts
st.markdown("### 2. Operational Timings & Shifts")
c1, c2 = st.columns(2)
with c1:
    st.time_input("OPD Opening Time", key="s2_open")
    st.time_input("OPD Closing Time", key="s2_close")
with c2:
    st.selectbox("Emergency Services Availability", ["24/7 Active", "Day Shift Only"], key="s2_emerg")
    st.number_input("Shift Duration (Hours)", value=8, key="s2_shift")
if st.button("Save Operational Timings", key="btn2"):
    st.success("Timings updated!")

st.divider()

# 3. Bed & Department Configuration
st.markdown("### 3. Bed & Department Configuration")
st.number_input("Total Hospital Bed Capacity", value=200, key="s3_beds")
st.multiselect("Active Departments", ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Emergency", "ICU"], default=["Cardiology", "Emergency", "ICU"], key="s3_deps")
if st.button("Save Bed & Department Config", key="btn3"):
    st.success("Department configuration saved!")

st.divider()

# 4. User Access & Roles (RBAC)
st.markdown("### 4. User Access & Roles (RBAC)")
st.selectbox("Select Role to Edit Permissions", ["Admin", "Doctor", "Nurse", "Receptionist", "Pharmacist"], key="s4_role")
st.checkbox("Allow Patient Data Editing", value=True, key="s4_p1")
st.checkbox("Allow Financial Report Viewing", value=False, key="s4_p2")
st.checkbox("Allow Inventory Restocking", value=True, key="s4_p3")
if st.button("Save Role Permissions", key="btn4"):
    st.success("Permissions updated!")

st.divider()

# 5. Security & Authentication
st.markdown("### 5. Security & Authentication")
st.checkbox("Enable Two-Factor Authentication (2FA)", value=True, key="s5_2fa")
st.number_input("Session Timeout (Minutes)", value=30, key="s5_timeout")
st.text_input("Change Admin Password", type="password", key="s5_pass")
if st.button("Save Security Settings", key="btn5"):
    st.success("Security settings updated!")

st.divider()

# 6. Audit & Activity Logs
st.markdown("### 6. Audit & Activity Logs")
st.checkbox("Log User Login Activities", value=True, key="s6_log1")
st.checkbox("Log Data Modification/Deletion Actions", value=True, key="s6_log2")
st.button("Export Audit Logs (.CSV)", key="btn6_exp")

st.divider()

# 7. Notification & Alert Settings
st.markdown("### 7. Notification & Alert Settings")
st.checkbox("Email Alerts for Low Pharmacy Stock", value=True, key="s7_n1")
st.checkbox("SMS Alerts for Appointment Confirmation", value=True, key="s7_n2")
st.checkbox("Emergency Bed Full Alerts", value=True, key="s7_n3")
if st.button("Save Notification Settings", key="btn7"):
    st.success("Notification preferences saved!")

st.divider()

# 8. Database Backup & Restore
st.markdown("### 8. Database Backup & Restore")
c1, c2 = st.columns(2)
with c1:
    st.selectbox("Auto Backup Frequency", ["Daily", "Weekly", "Monthly"], key="s8_freq")
    st.button("Backup Database Now", type="primary", key="btn8_bk")
with c2:
    st.file_uploader("Restore Database File (.db / .sql)", key="s8_file")

st.divider()

# 9. Theme & Display Customization
st.markdown("### 9. Theme & Display Customization")
st.selectbox("System Interface Theme", ["Dark Navy Blue (Default)", "Light Mode", "High Contrast"], key="s9_theme")
st.selectbox("Default Language", ["English", "Marathi", "Hindi"], key="s9_lang")
if st.button("Save Display Settings", key="btn9"):
    st.success("Theme settings saved!")

st.divider()

# 10. Billing, Taxes & Currency
st.markdown("### 10. Billing, Taxes & Currency")
st.text_input("Currency Symbol", value="₹", key="s10_curr")
st.number_input("Standard GST / Tax Rate (%)", value=18.0, key="s10_tax")
st.text_input("Tax Registration / GSTIN", value="27AAAAA0000A1Z5", key="s10_gst")
if st.button("Save Billing Config", key="btn10"):
    st.success("Billing settings saved!")

st.divider()

# 11. Pharmacy & Inventory Thresholds
st.markdown("### 11. Pharmacy & Inventory Thresholds")
st.number_input("Global Low Stock Alert Level (Quantity)", value=10, key="s11_stock")
st.checkbox("Auto-Mark Expired Medicines as Inactive", value=True, key="s11_exp")
if st.button("Save Pharmacy Thresholds", key="btn11"):
    st.success("Inventory thresholds saved!")

st.divider()

# 12. API & Third-Party Integrations
st.markdown("### 12. API & Third-Party Integrations")
st.text_input("SMS Gateway API Key", value="••••••••••••••••", type="password", key="s12_sms")
st.text_input("Payment Gateway API Key", value="••••••••••••••••", type="password", key="s12_pay")
st.checkbox("Enable WhatsApp Integration for Reports", value=False, key="s12_wa")
if st.button("Save API Integrations", key="btn12"):
    st.success("API Keys saved!")