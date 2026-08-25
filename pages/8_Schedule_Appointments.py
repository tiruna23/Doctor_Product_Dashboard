import streamlit as st
import pandas as pd

st.set_page_config(page_title="Schedule & Appointments", page_icon="📅", layout="wide")

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
    .badge-conf { background-color: #dcfce7; color: #16a34a; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
    .badge-comp { background-color: #dbeafe; color: #2563eb; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
    .badge-pend { background-color: #fef3c7; color: #d97706; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
    .badge-canc { background-color: #fee2e2; color: #dc2626; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
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

# Session State for Appointments Master Data
if "appointments_master" not in st.session_state:
    st.session_state.appointments_master = [
        {"id": "APT001", "patient": "Rahul Patil", "doctor": "Dr. Amit Sharma", "dept": "Cardiology", "date": "2026-08-25", "time": "10:00 AM", "status": "Confirmed"},
        {"id": "APT002", "patient": "Priya Deshmukh", "doctor": "Dr. Sneha Joshi", "dept": "Neurology", "date": "2026-08-25", "time": "11:00 AM", "status": "Completed"},
        {"id": "APT003", "patient": "Karan Singh", "doctor": "Dr. Raj Mehta", "dept": "Orthopedics", "date": "2026-08-25", "time": "12:00 PM", "status": "Pending"},
        {"id": "APT004", "patient": "Anjali Desai", "doctor": "Dr. Karan Patel", "dept": "Dermatology", "date": "2026-08-26", "time": "02:30 PM", "status": "Confirmed"},
        {"id": "APT005", "patient": "Vikram Joshi", "doctor": "Dr. Neha Singh", "dept": "Gynecology", "date": "2026-08-26", "time": "04:00 PM", "status": "Cancelled"}
    ]

# Header
st.markdown("## 📅 Schedule & Appointments")

# Metric Summary Row
c1, c2, c3, c4 = st.columns(4)
total = len(st.session_state.appointments_master)
conf = len([a for a in st.session_state.appointments_master if a["status"] == "Confirmed"])
comp = len([a for a in st.session_state.appointments_master if a["status"] == "Completed"])
pend = len([a for a in st.session_state.appointments_master if a["status"] == "Pending"])

c1.markdown(f'<div class="kpi-card"><div class="kpi-title">Total Appointments</div><div class="kpi-val">{total}</div></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="kpi-card"><div class="kpi-title">Confirmed</div><div class="kpi-val" style="color:#16a34a;">{conf}</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="kpi-card"><div class="kpi-title">Completed</div><div class="kpi-val" style="color:#2563eb;">{comp}</div></div>', unsafe_allow_html=True)
c4.markdown(f'<div class="kpi-card"><div class="kpi-title">Pending</div><div class="kpi-val" style="color:#d97706;">{pend}</div></div>', unsafe_allow_html=True)

st.write("")

# Action Row
col_s, col_st, col_b = st.columns([4, 3, 2])

with col_s:
    search_q = st.text_input("Search Appointments", placeholder="Search patient or doctor name...", label_visibility="collapsed")

with col_st:
    selected_status = st.selectbox("Status Filter", ["All Status", "Confirmed", "Completed", "Pending", "Cancelled"], label_visibility="collapsed")

with col_b:
    add_btn = st.button("➕ Book Appointment", type="primary", use_container_width=True)

# Modal Dialog for Booking Appointment (CRUD: Create)
if add_btn:
    @st.dialog("➕ Book New Appointment")
    def add_apt_dialog():
        with st.form("new_apt_form"):
            apt_id = f"APT00{len(st.session_state.appointments_master)+1}"
            p_name = st.text_input("Patient Name")
            d_name = st.text_input("Doctor Name", "Dr. Amit Sharma")
            dept = st.selectbox("Department", ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Dermatology", "Gynecology"])
            c_d, c_t = st.columns(2)
            a_date = c_d.date_input("Date")
            a_time = c_t.text_input("Time Slot", "10:30 AM")
            a_status = st.selectbox("Status", ["Confirmed", "Pending"])

            if st.form_submit_button("Book Appointment", use_container_width=True):
                if p_name:
                    st.session_state.appointments_master.insert(0, {
                        "id": apt_id, "patient": p_name, "doctor": d_name, "dept": dept,
                        "date": str(a_date), "time": a_time, "status": a_status
                    })
                    st.success("Appointment booked successfully!")
                    st.rerun()

    add_apt_dialog()

st.write("")

# Filtering Logic
filtered_apts = st.session_state.appointments_master

if search_q:
    filtered_apts = [a for a in filtered_apts if search_q.lower() in a["patient"].lower() or search_q.lower() in a["doctor"].lower()]

if selected_status != "All Status":
    filtered_apts = [a for a in filtered_apts if a["status"] == selected_status]

# Display Appointments Table with Actions (CRUD: Read, Update, Delete)
headers = st.columns([1.2, 2, 2, 1.8, 1.5, 1.2, 1.5, 1.8])
headers[0].markdown("**Apt ID**")
headers[1].markdown("**Patient Name**")
headers[2].markdown("**Doctor**")
headers[3].markdown("**Department**")
headers[4].markdown("**Date**")
headers[5].markdown("**Time**")
headers[6].markdown("**Status**")
headers[7].markdown("**Action**")

st.divider()

for idx, apt in enumerate(filtered_apts):
    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([1.2, 2, 2, 1.8, 1.5, 1.2, 1.5, 1.8])
    c1.write(apt["id"])
    c2.write(f"**{apt['patient']}**")
    c3.write(apt["doctor"])
    c4.write(apt["dept"])
    c5.write(apt["date"])
    c6.write(apt["time"])

    # Status Badges
    if apt["status"] == "Confirmed":
        c7.markdown('<span class="badge-conf">Confirmed</span>', unsafe_allow_html=True)
    elif apt["status"] == "Completed":
        c7.markdown('<span class="badge-comp">Completed</span>', unsafe_allow_html=True)
    elif apt["status"] == "Pending":
        c7.markdown('<span class="badge-pend">Pending</span>', unsafe_allow_html=True)
    else:
        c7.markdown('<span class="badge-canc">Cancelled</span>', unsafe_allow_html=True)

    # Actions: Edit / Delete (CRUD)
    col_e, col_d = c8.columns(2)

    if col_e.button("✏️", key=f"edit_apt_{apt['id']}"):
        @st.dialog(f"Edit Appointment: {apt['id']}")
        def edit_apt_dialog(a):
            with st.form("edit_apt_form"):
                n_pat = st.text_input("Patient Name", value=a["patient"])
                n_doc = st.text_input("Doctor", value=a["doctor"])
                n_dept = st.text_input("Department", value=a["dept"])
                n_date = st.text_input("Date", value=a["date"])
                n_time = st.text_input("Time", value=a["time"])
                n_status = st.selectbox("Status", ["Confirmed", "Completed", "Pending", "Cancelled"], index=["Confirmed", "Completed", "Pending", "Cancelled"].index(a["status"]))

                if st.form_submit_button("Update Appointment"):
                    a["patient"] = n_pat
                    a["doctor"] = n_doc
                    a["dept"] = n_dept
                    a["date"] = n_date
                    a["time"] = n_time
                    a["status"] = n_status
                    st.success("Appointment Updated!")
                    st.rerun()

        edit_apt_dialog(apt)

    if col_d.button("🗑️", key=f"del_apt_{apt['id']}"):
        st.session_state.appointments_master.remove(apt)
        st.success("Appointment Deleted!")
        st.rerun()

st.caption(f"Showing {len(filtered_apts)} Appointments")