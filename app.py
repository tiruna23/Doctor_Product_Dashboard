import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="MediCare | Portal",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- 💾 PERMANENT JSON USER DATABASE -----------------
USER_FILE = "users_db.json"

def load_users():
    """JSON फाइलमधून युझर्स वाचणे (With Fallback)"""
    if not os.path.exists(USER_FILE):
        default_users = {"admin": "admin123"}
        with open(USER_FILE, "w") as f:
            json.dump(default_users, f, indent=4)
        return default_users

    try:
        with open(USER_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {"admin": "admin123"}
    except (json.JSONDecodeError, Exception):
        return {"admin": "admin123"}

def save_user(username, password):
    """नवीन युझर किंवा अपडेट केलेला पासवर्ड JSON मध्ये सेव्ह करणे"""
    users = load_users()
    users[username] = password
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ----------------- 🔄 URL QUERY PARAMETERS AUTH CHECK -----------------
# ब्राऊझर रिफ्रेश केला तरी URL वरून युझर ओळखणे
query_params = st.query_params
logged_in_user = query_params.get("user", None)

if "logged_in" not in st.session_state:
    if logged_in_user:
        st.session_state.logged_in = True
        st.session_state.current_user = logged_in_user
    else:
        st.session_state.logged_in = False
        st.session_state.current_user = "Admin"

# ----------------- MODERN CUSTOM CSS -----------------
st.markdown("""
<style>
    /* Full Page Background */
    .stApp {
        background: #f1f5f9 !important;
    }
    
    header { visibility: hidden; }
    
    /* Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        display: var(--sidebar-display, block);
    }
    [data-testid="stSidebar"] * { color: #f1f5f9 !important; }
    
    /* Sidebar Logout Button */
    [data-testid="stSidebar"] .stButton > button {
        background-color: #ef4444 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }

    /* Single Seamless Box Design */
    .single-login-card {
        background: #ffffff;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
        overflow: hidden;
        border: 1px solid #e2e8f0;
        margin-top: 25px;
    }

    /* Top Blue Header */
    .login-top-banner {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        padding: 35px 20px 25px 20px;
        text-align: center;
        color: white;
    }

    /* FIX: Remove inner st.form border completely */
    [data-testid="stForm"] {
        border: none !important;
        padding: 0px !important;
        background: transparent !important;
    }

    /* Input Field Styling */
    .stTextInput > div > div > input {
        border-radius: 10px !important;
        border: 1px solid #cbd5e1 !important;
        padding: 10px 14px !important;
        background-color: #f8fafc !important;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        justify-content: center;
        border-bottom: 1px solid #f1f5f9;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 14px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 13px;
    }

    /* Primary Login Button Styling */
    .stButton > button[kind="primary"] {
        background: #2563eb !important;
        border-radius: 10px !important;
        height: 44px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3) !important;
    }
    .stButton > button[kind="primary"]:hover {
        background: #1d4ed8 !important;
    }

    /* Dashboard UI */
    .kpi-card { background: #ffffff; border-radius: 12px; padding: 16px; border: 1px solid #e2e8f0; }
    .kpi-title { font-size: 13px; color: #64748b; font-weight: 600; }
    .kpi-val { font-size: 24px; font-weight: 800; color: #0f172a; margin: 4px 0; }
    .kpi-sub { font-size: 11px; color: #94a3b8; }
    .badge-green { background-color: #dcfce7; color: #16a34a; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }
    .badge-orange { background-color: #fef3c7; color: #d97706; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }
    .content-box { background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #e2e8f0; margin-top: 10px; }
    .act-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #f1f5f9; font-size: 13px; }
</style>
""", unsafe_allow_html=True)


# ==========================================
# 🔐 SINGLE BOX LOGIN SECTION
# ==========================================
if not st.session_state.logged_in:
    st.markdown("<style>:root { --sidebar-display: none; }</style>", unsafe_allow_html=True)
    
    st.write("")
    
    # Centered Vertical Layout
    _, center_col, _ = st.columns([1, 1.3, 1])
    
    with center_col:
        st.markdown("""
        <div class="single-login-card">
            <div class="login-top-banner">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="24" height="24" rx="6" fill="white" fill-opacity="0.2"/>
                    <path d="M12 7V17M7 12H17" stroke="white" stroke-width="3" stroke-linecap="round"/>
                </svg>
                <h2 style="color: white; font-size: 26px; font-weight: 800; margin: 8px 0 2px 0;">MediCare Portal</h2>
                <p style="color: #bfdbfe; font-size: 13px; margin: 0;">Smart Hospital & Pharmacist Platform</p>
            </div>
            <div style="padding: 25px 30px;">
        """, unsafe_allow_html=True)
        
        tab_login, tab_reg, tab_forgot = st.tabs(["🔑 Sign In", "📝 Create Account", "❓ Forgot Password"])
        
        # 1. SIGN IN TAB
        with tab_login:
            with st.form("login_form"):
                u_name = st.text_input("Username or Email", placeholder="admin").strip()
                u_pass = st.text_input("Password", type="password", placeholder="••••••••").strip()
                st.write("")
                btn_login = st.form_submit_button("Sign In", type="primary", use_container_width=True)
                
                if btn_login:
                    users_db = load_users()
                    if u_name in users_db and users_db[u_name] == u_pass:
                        st.session_state.logged_in = True
                        st.session_state.current_user = u_name
                        # URL parameter सेव्ह करणे जेणेकरून रिफ्रेशवर सत्र टिकेल
                        st.query_params["user"] = u_name
                        st.rerun()
                    else:
                        st.error("Invalid Username or Password!")

        # 2. CREATE ACCOUNT TAB
        with tab_reg:
            with st.form("register_form"):
                new_user = st.text_input("Choose Username").strip()
                new_pass = st.text_input("Choose Password", type="password").strip()
                confirm_pass = st.text_input("Confirm Password", type="password").strip()
                btn_reg = st.form_submit_button("Register Account", use_container_width=True)
                
                if btn_reg:
                    users_db = load_users()
                    if not new_user or not new_pass:
                        st.warning("All fields are required!")
                    elif new_user in users_db:
                        st.error("Username already exists!")
                    elif new_pass != confirm_pass:
                        st.error("Passwords do not match!")
                    else:
                        save_user(new_user, new_pass)
                        st.success("Account created successfully! Go to 'Sign In' tab.")

        # 3. FORGOT PASSWORD TAB
        with tab_forgot:
            with st.form("forgot_form"):
                forgot_user = st.text_input("Username").strip()
                reset_pass = st.text_input("New Password", type="password").strip()
                btn_reset = st.form_submit_button("Reset Password", use_container_width=True)
                
                if btn_reset:
                    users_db = load_users()
                    if forgot_user in users_db:
                        if reset_pass:
                            save_user(forgot_user, reset_pass)
                            st.success("Password reset successfully! Go to 'Sign In' tab.")
                        else:
                            st.warning("Enter a new password.")
                    else:
                        st.error("Username not found!")
                        
        st.markdown("""
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 📊 MAIN DASHBOARD (AFTER LOGIN)
# ==========================================
else:
    st.markdown("<style>:root { --sidebar-display: block; }</style>", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="24" height="24" rx="6" fill="#2563EB"/>
                <path d="M8 12H16M12 8V16" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
            <h2 style="color: white; margin: 0; font-size: 22px;">MediCare</h2>
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
        
        # 🚪 DIRECT GUARANTEED LOGOUT
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            # Logout करताना query parameter काढून टाकणे
            st.query_params.clear()
            st.rerun()

    # DYNAMIC GREETING AND DATE CALCULATION
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting_text = "Good Morning"
    elif 12 <= current_hour < 17:
        greeting_text = "Good Afternoon"
    else:
        greeting_text = "Good Evening"

    today_str = datetime.now().strftime("%d %b %Y, %A")

    h_col1, h_col2 = st.columns([3, 1])
    with h_col1:
        st.markdown(f"## {greeting_text}, {st.session_state.get('current_user', 'Admin')} 👋")
        st.caption("Here's what's happening with your hospital today.")
    with h_col2:
        st.markdown(f"<p style='text-align: right; color: #64748b; font-size: 13px; margin-top: 10px;'>{today_str}</p>", unsafe_allow_html=True)

    st.write("")

    doc_val = len(st.session_state.get('doctors', [1]*128))
    pat_val = len(st.session_state.get('patients', [1]*1452))
    bed_val = len(st.session_state.get('beds', [1]*86))
    amb_val = len(st.session_state.get('ambulances', [1]*12))

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Doctors</div><div class="kpi-val">🧑‍⚕️ {doc_val}</div><div class="kpi-sub">Total Doctors</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Patients</div><div class="kpi-val">👤 {pat_val:,}</div><div class="kpi-sub">Total Patients</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Available Beds</div><div class="kpi-val">🛏️ {bed_val}</div><div class="kpi-sub">Total 200 Beds</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Ambulances</div><div class="kpi-val">🚑 {amb_val}</div><div class="kpi-sub">Total Ambulances</div></div>', unsafe_allow_html=True)

    st.write("")

    m5, m6, m7, m8 = st.columns(4)
    with m5:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Today\'s Appointments</div><div class="kpi-val">24</div><span class="badge-green">▲ 12% from yesterday</span></div>', unsafe_allow_html=True)
    with m6:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Pharmacy Low Stock</div><div class="kpi-val">8</div><span class="badge-orange">Items need attention</span></div>', unsafe_allow_html=True)
    with m7:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Pending Bills</div><div class="kpi-val">18</div><div class="kpi-sub">Total Pending</div></div>', unsafe_allow_html=True)
    with m8:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Total Revenue (Today)</div><div class="kpi-val">₹ 1,24,560</div><span class="badge-green">▲ 9.5% from yesterday</span></div>', unsafe_allow_html=True)

    st.write("")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("""
        <div class="content-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <b style="font-size: 15px;">Recent Activities</b>
            </div>
            <hr style="margin: 5px 0 15px 0; border-top: 1px solid #e2e8f0;">
            <div class="act-item">
                <span>📝 New patient <b>Rahul Patil</b> registered</span>
                <span style="color:#94a3b8; font-size: 12px;">10:30 AM</span>
            </div>
            <div class="act-item">
                <span>🛏️ Bed allocated to patient <b>#12345</b></span>
                <span style="color:#94a3b8; font-size: 12px;">09:45 AM</span>
            </div>
            <div class="act-item">
                <span>🚑 Ambulance <b>MH-09-AB-1234</b> on duty</span>
                <span style="color:#94a3b8; font-size: 12px;">08:15 AM</span>
            </div>
            <div class="act-item">
                <span>💳 Invoice <b>#INV-00123</b> created</span>
                <span style="color:#94a3b8; font-size: 12px;">08:00 AM</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("""
        <div class="content-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <b style="font-size: 15px;">Upcoming Appointments</b>
                <span style="color: #2563eb; font-size: 12px; font-weight: 600; cursor: pointer;">View All</span>
            </div>
            <hr style="margin: 5px 0 15px 0; border-top: 1px solid #e2e8f0;">
        """, unsafe_allow_html=True)
        
        ap1, ap2, ap3 = st.columns([1.5, 2.5, 1])
        ap1.write("⏰ **10:00 AM**")
        ap2.write("Dr. Amit Sharma\n*(Rahul Patil)*")
        ap3.markdown('<span class="badge-green">Cardiology</span>', unsafe_allow_html=True)
        st.divider()

        bp1, bp2, bp3 = st.columns([1.5, 2.5, 1])
        bp1.write("⏰ **11:00 AM**")
        bp2.write("Dr. Sneha Joshi\n*(Priya Deshmukh)*")
        bp3.markdown('<span class="badge-green">Neurology</span>', unsafe_allow_html=True)
        st.divider()

        cp1, cp2, cp3 = st.columns([1.5, 2.5, 1])
        cp1.write("⏰ **12:00 PM**")
        cp2.write("Dr. Raj Mehta\n*(Karan Singh)*")
        cp3.markdown('<span class="badge-green">Orthopedics</span>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)