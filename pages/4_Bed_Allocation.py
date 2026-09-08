import streamlit as st

st.set_page_config(page_title="Bed Allocation", page_icon="🛏️", layout="wide")

# ----------------- 🛡️ LOGIN GUARD -----------------
if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

# ----------------- UNIFORM SIDEBAR & CUSTOM CSS -----------------
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
    
    /* Page Specific Custom Cards */
    .kpi-card { background: #ffffff; border-radius: 10px; padding: 14px 18px; border: 1px solid #e2e8f0; }
    .kpi-title { font-size: 13px; color: #64748b; font-weight: 600; }
    .kpi-val { font-size: 26px; font-weight: 800; color: #0f172a; margin: 2px 0; }
    .bed-box { 
        background: #ffffff; 
        border-radius: 8px; 
        padding: 12px; 
        border: 1px solid #cbd5e1; 
        text-align: center; 
        margin-bottom: 10px;
    }
    .status-avail { color: #16a34a; font-size: 12px; font-weight: bold; }
    .status-occ { color: #dc2626; font-size: 12px; font-weight: bold; }
    .status-res { color: #d97706; font-size: 12px; font-weight: bold; }
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

# Session State for Beds Data
if "beds_master" not in st.session_state:
    st.session_state.beds_master = {
        "ICU": [
            {"id": "ICU-01", "status": "Available", "patient": None},
            {"id": "ICU-02", "status": "Occupied", "patient": "Rahul Patil"},
            {"id": "ICU-03", "status": "Available", "patient": None},
            {"id": "ICU-04", "status": "Occupied", "patient": "Vikram Joshi"},
            {"id": "ICU-05", "status": "Available", "patient": None},
        ],
        "General Ward": [
            {"id": "GW-01", "status": "Available", "patient": None},
            {"id": "GW-02", "status": "Occupied", "patient": "Karan Singh"},
            {"id": "GW-03", "status": "Occupied", "patient": "Anjali Desai"},
            {"id": "GW-04", "status": "Available", "patient": None},
        ],
        "Private Room": [
            {"id": "PR-01", "status": "Occupied", "patient": "Priya Deshmukh"},
            {"id": "PR-02", "status": "Available", "patient": None},
            {"id": "PR-03", "status": "Reserved", "patient": "Upcoming Booking"},
            {"id": "PR-04", "status": "Available", "patient": None},
        ],
        "Deluxe Room": [
            {"id": "DR-01", "status": "Occupied", "patient": "Sneha Gupta"},
            {"id": "DR-02", "status": "Occupied", "patient": "Rohit Verma"},
            {"id": "DR-03", "status": "Available", "patient": None},
            {"id": "DR-04", "status": "Reserved", "patient": "Reserved VIP"},
        ]
    }

# Header & Actions
st.markdown("## 🛏️ Bed Allocation")

# Metric Summary
c1, c2, c3, c4 = st.columns(4)
c1.markdown('<div class="kpi-card"><div class="kpi-title">Total Beds</div><div class="kpi-val">200</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="kpi-card"><div class="kpi-title">Available</div><div class="kpi-val" style="color:#16a34a;">86 <span style="font-size:12px;">(43%)</span></div></div>', unsafe_allow_html=True)
c3.markdown('<div class="kpi-card"><div class="kpi-title">Occupied</div><div class="kpi-val" style="color:#dc2626;">98 <span style="font-size:12px;">(49%)</span></div></div>', unsafe_allow_html=True)
c4.markdown('<div class="kpi-card"><div class="kpi-title">Reserved</div><div class="kpi-val" style="color:#d97706;">16</div></div>', unsafe_allow_html=True)

st.write("")

# Action Button for Quick Bed Allocate / Manage
col_act1, col_act2 = st.columns([6, 2])
with col_act2:
    if st.button("➕ Allocate / Change Bed Status", type="primary", use_container_width=True):
        @st.dialog("🛏️ Manage Bed Allocation")
        def allocate_dialog():
            ward = st.selectbox("Select Ward / Category", list(st.session_state.beds_master.keys()))
            bed_ids = [b["id"] for b in st.session_state.beds_master[ward]]
            selected_bed_id = st.selectbox("Select Bed ID", bed_ids)
            
            # Find current bed details
            bed_obj = next(b for b in st.session_state.beds_master[ward] if b["id"] == selected_bed_id)
            
            new_status = st.selectbox("Status", ["Available", "Occupied", "Reserved"], index=["Available", "Occupied", "Reserved"].index(bed_obj["status"]))
            patient_name = st.text_input("Patient Name (if Occupied/Reserved)", value=bed_obj["patient"] if bed_obj["patient"] else "")
            
            if st.button("Save Changes", use_container_width=True):
                bed_obj["status"] = new_status
                bed_obj["patient"] = patient_name if new_status != "Available" else None
                st.success(f"Updated {selected_bed_id} successfully!")
                st.rerun()

        allocate_dialog()

st.write("---")

# Render Wards & Beds Cards
for ward_name, beds in st.session_state.beds_master.items():
    st.subheader(f"{ward_name}")
    cols = st.columns(len(beds))
    
    for idx, bed in enumerate(beds):
        with cols[idx]:
            if bed["status"] == "Available":
                badge = '<span class="status-avail">🟢 Available</span>'
                sub_text = 'Vacant'
            elif bed["status"] == "Occupied":
                badge = '<span class="status-occ">🔴 Occupied</span>'
                sub_text = f"👤 {bed['patient']}"
            else:
                badge = '<span class="status-res">🟠 Reserved</span>'
                sub_text = f"📌 {bed['patient']}"
                
            st.markdown(f"""
            <div class="bed-box">
                <div style="font-weight: bold; font-size: 16px; margin-bottom: 4px;">{bed['id']}</div>
                <div>{badge}</div>
                <div style="font-size: 12px; color: #64748b; margin-top: 4px;">{sub_text}</div>
            </div>
            """, unsafe_allow_html=True)
            
    st.write("")