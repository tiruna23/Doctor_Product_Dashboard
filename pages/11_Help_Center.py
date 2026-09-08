import streamlit as st

st.set_page_config(page_title="Help Center", page_icon="❓", layout="wide")

# ----------------- 🛡️ LOGIN GUARD -----------------
if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

# Custom Styling matching Theme & Dark Navy Blue Sidebar
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
    
    .help-card { background: #ffffff; border-radius: 10px; padding: 20px; border: 1px solid #e2e8f0; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# ----------------- UNIFORM SIDEBAR NAVIGATION -----------------
with st.sidebar:
    # Standard Blue MediCare Logo
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
    
    # 🚪 FAST WORKING LOGOUT BUTTON
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.switch_page("app.py")

# Header
st.markdown("## ❓ Help & Support Center")
st.write("")

# FAQs Section
st.markdown("### 📌 Frequently Asked Questions")

with st.expander("👨‍⚕️ How do I add a new Doctor to the Directory?"):
    st.write("Go to the **Doctor Directory** page from the sidebar and click on the **'➕ Add Doctor'** button at the top right. Fill in the required details and click save.")

with st.expander("🛏️ How to update Bed Allocation status?"):
    st.write("Navigate to **Bed Allocation**, click on **'➕ Allocate / Change Bed Status'**, select the ward and bed ID, update the status (Available, Occupied, Reserved), and save.")

with st.expander("💊 What triggers a Low Stock alert in Pharmacy Inventory?"):
    st.write("When any medicine stock falls below 250 units, it is automatically flagged as **Low Stock**. If stock reaches 0, it changes to **Out of Stock**.")

with st.expander("💳 How to generate patient invoices?"):
    st.write("Visit the **Billing System** module and click **'➕ Generate Invoice'**. Enter patient details, amount, and payment mode to create a bill instantly.")

st.write("---")

# Contact Support Form
st.markdown('<div class="help-card">', unsafe_allow_html=True)
st.markdown("### 💬 Need Further Assistance?")
st.caption("Submit your query to our technical IT support team.")

with st.form("support_form"):
    st.text_input("Your Name")
    st.text_input("Email Address")
    st.text_area("Describe your issue / inquiry")
    if st.form_submit_button("Submit Support Ticket", type="primary"):
        st.success("Your support request has been submitted! Our team will contact you shortly.")
st.markdown('</div>', unsafe_allow_html=True)