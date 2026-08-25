import streamlit as st

st.set_page_config(page_title="Ambulance Fleet", page_icon="🚑", layout="wide")

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
    
    .kpi-card { background: #ffffff; border-radius: 10px; padding: 14px 18px; border: 1px solid #e2e8f0; }
    .kpi-title { font-size: 13px; color: #64748b; font-weight: 600; }
    .kpi-val { font-size: 24px; font-weight: 800; color: #0f172a; margin: 2px 0; }
    .amb-card { 
        background: #ffffff; 
        border-radius: 12px; 
        padding: 18px; 
        border: 1px solid #e2e8f0; 
        text-align: center; 
        margin-bottom: 15px; 
    }
    .badge-avail { background-color: #dcfce7; color: #16a34a; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
    .badge-duty { background-color: #fef3c7; color: #d97706; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
    .badge-maint { background-color: #fee2e2; color: #dc2626; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
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

# Session State for Ambulance Fleet Data
if "ambulances_master" not in st.session_state:
    st.session_state.ambulances_master = [
        {"id": "MH-09-AB-1234", "type": "Basic Life Support", "driver": "Ramesh Kumar", "phone": "9876543210", "status": "Available"},
        {"id": "MH-09-CD-5678", "type": "Advanced Life Support", "driver": "Suresh Patil", "phone": "9765432109", "status": "On Duty"},
        {"id": "MH-09-EF-9012", "type": "Basic Life Support", "driver": "Mahesh Yadav", "phone": "9654321098", "status": "Maintenance"}
    ]

# Header
st.markdown("## 🚑 Ambulance Fleet")

# Fleet Summary KPIs
c1, c2, c3, c4, c5 = st.columns(5)
total = len(st.session_state.ambulances_master)
avail = len([a for a in st.session_state.ambulances_master if a["status"] == "Available"])
duty = len([a for a in st.session_state.ambulances_master if a["status"] == "On Duty"])
maint = len([a for a in st.session_state.ambulances_master if a["status"] == "Maintenance"])
out = len([a for a in st.session_state.ambulances_master if a["status"] == "Out of Service"])

c1.markdown(f'<div class="kpi-card"><div class="kpi-title">Total Ambulances</div><div class="kpi-val">{total}</div></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="kpi-card"><div class="kpi-title">Available</div><div class="kpi-val" style="color:#16a34a;">{avail}</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="kpi-card"><div class="kpi-title">On Duty</div><div class="kpi-val" style="color:#d97706;">{duty}</div></div>', unsafe_allow_html=True)
c4.markdown(f'<div class="kpi-card"><div class="kpi-title">Maintenance</div><div class="kpi-val" style="color:#dc2626;">{maint}</div></div>', unsafe_allow_html=True)
c5.markdown(f'<div class="kpi-card"><div class="kpi-title">Out of Service</div><div class="kpi-val" style="color:#64748b;">{out}</div></div>', unsafe_allow_html=True)

st.write("")

# Action Row (Add Ambulance)
col_s, col_b = st.columns([6, 2])
with col_b:
    if st.button("➕ Add Ambulance", type="primary", use_container_width=True):
        @st.dialog("➕ Add New Ambulance")
        def add_amb_dialog():
            with st.form("add_amb_form"):
                a_id = st.text_input("Vehicle Number (e.g. MH-09-XY-9999)")
                a_type = st.selectbox("Ambulance Type", ["Basic Life Support", "Advanced Life Support", "Patient Transport"])
                a_driver = st.text_input("Driver Name")
                a_phone = st.text_input("Phone Number")
                a_status = st.selectbox("Status", ["Available", "On Duty", "Maintenance", "Out of Service"])

                if st.form_submit_button("Save Vehicle", use_container_width=True):
                    if a_id and a_driver:
                        st.session_state.ambulances_master.append({
                            "id": a_id, "type": a_type, "driver": a_driver, "phone": a_phone, "status": a_status
                        })
                        st.success("Ambulance added successfully!")
                        st.rerun()

        add_amb_dialog()

st.write("---")

# Ambulance Grid View Cards
cols = st.columns(3)

for idx, amb in enumerate(st.session_state.ambulances_master):
    with cols[idx % 3]:
        # Badge logic
        if amb["status"] == "Available":
            badge_html = '<span class="badge-avail">Available</span>'
        elif amb["status"] == "On Duty":
            badge_html = '<span class="badge-duty">On Duty</span>'
        else:
            badge_html = '<span class="badge-maint">Maintenance / Out</span>'

        # Card Container
        with st.container(border=True):
            st.markdown(f"""
            <div style="text-align: center;">
                <div style="font-size: 32px;">🚑</div>
                <h4 style="margin: 5px 0;">{amb['id']}</h4>
                <div style="color: #64748b; font-size: 13px; margin-bottom: 8px;">{amb['type']}</div>
                <div>{badge_html}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("")
            st.write(f"👤 **Driver:** {amb['driver']}")
            st.write(f"📞 **Phone:** {amb['phone']}")
            st.divider()
            
            # Actions (Edit / Delete)
            ca, cb = st.columns(2)
            if ca.button("✏️ Edit", key=f"edit_amb_{amb['id']}", use_container_width=True):
                @st.dialog(f"Edit {amb['id']}")
                def edit_amb_dialog(a):
                    with st.form("edit_amb_form"):
                        n_type = st.selectbox("Type", ["Basic Life Support", "Advanced Life Support", "Patient Transport"], index=["Basic Life Support", "Advanced Life Support", "Patient Transport"].index(a["type"]))
                        n_driver = st.text_input("Driver", value=a["driver"])
                        n_phone = st.text_input("Phone", value=a["phone"])
                        n_status = st.selectbox("Status", ["Available", "On Duty", "Maintenance", "Out of Service"], index=["Available", "On Duty", "Maintenance", "Out of Service"].index(a["status"]))
                        
                        if st.form_submit_button("Update Ambulance"):
                            a["type"] = n_type
                            a["driver"] = n_driver
                            a["phone"] = n_phone
                            a["status"] = n_status
                            st.success("Updated successfully!")
                            st.rerun()

                edit_amb_dialog(amb)

            if cb.button("🗑️ Delete", key=f"del_amb_{amb['id']}", use_container_width=True):
                st.session_state.ambulances_master.remove(amb)
                st.success("Vehicle deleted!")
                st.rerun()