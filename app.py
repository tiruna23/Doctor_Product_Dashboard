import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="HealthPlus | Executive Portal",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- 💾 PERMANENT JSON USER DATABASE -----------------
USER_FILE = "users_db.json"

def load_users():
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
    users = load_users()
    users[username] = password
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ----------------- 🔄 URL QUERY PARAMETERS AUTH CHECK -----------------
query_params = st.query_params
logged_in_user = query_params.get("user", None)

if "logged_in" not in st.session_state:
    if logged_in_user:
        st.session_state.logged_in = True
        st.session_state.current_user = logged_in_user
    else:
        st.session_state.logged_in = False
        st.session_state.current_user = "Admin"

# ----------------- NEW EMERALD & TEAL MODERN THEME (CSS) -----------------
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: #f0fdf4 !important; /* Soft Mint/Emerald Light Tint */
    }
    
    header { visibility: hidden; }
    
    /* Sidebar Customization - Deep Forest Teal */
    [data-testid="stSidebar"] {
        background-color: #064e3b !important;
        display: var(--sidebar-display, block);
    }
    [data-testid="stSidebar"] * { color: #ecfdf5 !important; }

    /* Single Card Login Container */
    .single-login-card {
        background: #ffffff;
        border-radius: 24px;
        box-shadow: 0 25px 50px -12px rgba(6, 78, 59, 0.15);
        overflow: hidden;
        border: 1px solid #a7f3d0;
        margin-top: 20px;
    }

    /* Top Emerald Header Banner */
    .login-top-banner {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        padding: 38px 20px 28px 20px;
        text-align: center;
        color: white;
    }

    /* Form Clean Design */
    [data-testid="stForm"] {
        border: none !important;
        padding: 0px !important;
        background: transparent !important;
    }

    /* Input Field Styling */
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        border: 1px solid #cbd5e1 !important;
        padding: 12px 16px !important;
        background-color: #f8fafc !important;
    }

    /* Primary Emerald Button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        border-radius: 12px !important;
        height: 46px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(5, 150, 105, 0.35) !important;
    }

    /* Top Right Logout Button Styling */
    div[data-testid="stColumn"]:has(button[key="top_logout_btn"]) button {
        background-color: #dc2626 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
    }

    /* Dashboard UI Elements */
    .kpi-card { 
        background: #ffffff; 
        border-radius: 16px; 
        padding: 20px; 
        border: 1px solid #d1fae5;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
    }
    .kpi-title { font-size: 13px; color: #047857; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
    .kpi-val { font-size: 26px; font-weight: 800; color: #064e3b; margin: 6px 0; }
    .kpi-sub { font-size: 12px; color: #64748b; }
    .badge-green { background-color: #d1fae5; color: #047857; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; }
    .badge-orange { background-color: #ffedd5; color: #c2410c; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 700; }
    .content-box { background: #ffffff; border-radius: 16px; padding: 22px; border: 1px solid #d1fae5; margin-top: 10px; }
    .act-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #f0fdf4; font-size: 13px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🔐 LOGIN SECTION
# ==========================================
if not st.session_state.logged_in:
    st.markdown("<style>:root { --sidebar-display: none; }</style>", unsafe_allow_html=True)
    st.write("")
    
    _, center_col, _ = st.columns([1, 1.3, 1])
    
    with center_col:
        st.markdown("""
        <div class="single-login-card">
            <div class="login-top-banner">
                <h2 style="color: white; font-size: 28px; font-weight: 800; margin: 0;">🩺 HealthPlus Portal</h2>
                <p style="color: #a7f3d0; font-size: 13px; margin-top: 4px;">Advanced Medical & Hospital Operations</p>
            </div>
            <div style="padding: 25px 30px;">
        """, unsafe_allow_html=True)
        
        tab_login, tab_reg, tab_forgot = st.tabs(["🔑 Sign In", "📝 Create Account", "❓ Forgot Password"])
        
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
                        st.query_params["user"] = u_name
                        st.rerun()
                    else:
                        st.error("Invalid Username or Password!")

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
                            st.success("Password reset successfully!")
                        else:
                            st.warning("Enter a new password.")
                    else:
                        st.error("Username not found!")
                        
        st.markdown("</div></div>", unsafe_allow_html=True)

# ==========================================
# 📊 DASHBOARD (OVERVIEW)
# ==========================================
else:
    st.markdown("<style>:root { --sidebar-display: block; }</style>", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
            <h2 style="color: #a7f3d0; margin: 0; font-size: 24px;">🩺 HealthPlus</h2>
        </div>
        """, unsafe_allow_html=True)
            
        st.caption(f"Active Session: **{st.session_state.get('current_user', 'Admin')}**")
        st.write("")
        st.caption("NAVIGATION MENU")
        
        # Updated exact file paths matching your pages/ directory
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

    # Dynamic Greetings & Top Right Logout Header
    current_hour = datetime.now().hour
    greeting_text = "Good Morning" if current_hour < 12 else ("Good Afternoon" if current_hour < 17 else "Good Evening")
    today_str = datetime.now().strftime("%d %b %Y, %A")

    h_col1, h_col2, h_col3 = st.columns([3, 1.2, 0.8])
    with h_col1:
        st.markdown(f"## {greeting_text}, {st.session_state.get('current_user', 'Admin')} 👋")
        st.caption("Welcome to HealthPlus Executive Overview.")
    with h_col2:
        st.markdown(f"<p style='text-align: right; color: #047857; font-size: 13px; font-weight: 600; margin-top: 15px;'>{today_str}</p>", unsafe_allow_html=True)
    with h_col3:
        st.write("")
        if st.button("🚪 Logout", key="top_logout_btn", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            st.query_params.clear()
            st.rerun()

    st.write("")

    # KPI Metrics Cards
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Active Doctors</div><div class="kpi-val">🧑‍⚕️ 128</div><div class="kpi-sub">On duty</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Total Patients</div><div class="kpi-val">👤 1,452</div><div class="kpi-sub">Registered</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Bed Occupancy</div><div class="kpi-val">🛏️ 114 / 200</div><div class="kpi-sub">86 Beds Free</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Emergency Fleet</div><div class="kpi-val">🚑 12</div><div class="kpi-sub">Ambulances Ready</div></div>', unsafe_allow_html=True)

    st.write("")

    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("""
        <div class="content-box">
            <b style="font-size: 16px; color: #064e3b;">Recent Activity Log</b>
            <hr style="margin: 10px 0; border-top: 1px solid #d1fae5;">
            <div class="act-item"><span>📝 Patient Registration (#PAT-892)</span><span style="color:#047857;">Just now</span></div>
            <div class="act-item"><span>🛏️ ICU Bed #04 Allocated</span><span style="color:#047857;">15 mins ago</span></div>
            <div class="act-item"><span>💊 Medicine Restock Order Placed</span><span style="color:#047857;">1 hour ago</span></div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("""
        <div class="content-box">
            <b style="font-size: 16px; color: #064e3b;">Today's Priority Schedule</b>
            <hr style="margin: 10px 0; border-top: 1px solid #d1fae5;">
            <div class="act-item"><span>⏰ 10:00 AM - Dr. Amit Sharma (Cardiology)</span><span class="badge-green">Confirmed</span></div>
            <div class="act-item"><span>⏰ 11:30 AM - Dr. Sneha Joshi (Neurology)</span><span class="badge-green">Confirmed</span></div>
            <div class="act-item"><span>⏰ 02:00 PM - Dr. Raj Mehta (Orthopedics)</span><span class="badge-orange">Pending</span></div>
        </div>
        """, unsafe_allow_html=True)