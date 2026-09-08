import streamlit as st
import pandas as pd

st.set_page_config(page_title="Doctor Directory", page_icon="👨‍⚕️", layout="wide")

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
    
    .badge-avail { background-color: #dcfce7; color: #16a34a; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
    .badge-duty { background-color: #dbeafe; color: #2563eb; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
    .badge-leave { background-color: #fee2e2; color: #dc2626; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
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

# Session State for Doctors List (Master Data)
if "doctors_master" not in st.session_state:
    st.session_state.doctors_master = [
        {"id": "DOC001", "name": "Dr. Amit Sharma", "specialty": "Cardiology", "exp": "12 Years", "status": "Available"},
        {"id": "DOC002", "name": "Dr. Sneha Joshi", "specialty": "Neurology", "exp": "8 Years", "status": "Available"},
        {"id": "DOC003", "name": "Dr. Raj Mehta", "specialty": "Orthopedics", "exp": "15 Years", "status": "On Duty"},
        {"id": "DOC004", "name": "Dr. Priya Verma", "specialty": "Pediatrics", "exp": "6 Years", "status": "Available"},
        {"id": "DOC005", "name": "Dr. Karan Patel", "specialty": "Dermatology", "exp": "9 Years", "status": "Available"},
        {"id": "DOC006", "name": "Dr. Neha Singh", "specialty": "Gynecology", "exp": "10 Years", "status": "On Leave"},
        {"id": "DOC007", "name": "Dr. Rohit Kumar", "specialty": "ENT", "exp": "7 Years", "status": "Available"}
    ]

# Top Bar & Actions
st.markdown("## 👨‍⚕️ Doctor Directory")

col_search, col_spec, col_stat, col_btn = st.columns([3, 2, 2, 2])

with col_search:
    search_q = st.text_input("Search Doctor", placeholder="Search doctor...", label_visibility="collapsed")

with col_spec:
    specs = ["All Specialties", "Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Dermatology", "Gynecology", "ENT"]
    selected_spec = st.selectbox("Specialty", specs, label_visibility="collapsed")

with col_stat:
    selected_status = st.selectbox("Status", ["All Status", "Available", "On Duty", "On Leave"], label_visibility="collapsed")

with col_btn:
    add_modal = st.button("➕ Add Doctor", use_container_width=True, type="primary")

# Modal Dialog / Form for Adding New Doctor (CRUD: Create)
if add_modal:
    @st.dialog("➕ Add New Doctor")
    def add_doc_dialog():
        with st.form("new_doc_form"):
            d_id = f"DOC00{len(st.session_state.doctors_master)+1}"
            d_name = st.text_input("Doctor Name", placeholder="Dr. First Last")
            d_spec = st.selectbox("Specialty", specs[1:])
            d_exp = st.text_input("Experience", placeholder="e.g. 5 Years")
            d_status = st.selectbox("Status", ["Available", "On Duty", "On Leave"])
            
            if st.form_submit_button("Save Doctor", use_container_width=True):
                if d_name:
                    st.session_state.doctors_master.append({
                        "id": d_id, "name": d_name, "specialty": d_spec, "exp": d_exp, "status": d_status
                    })
                    st.success("Doctor added successfully!")
                    st.rerun()

    add_doc_dialog()

st.write("")

# Filtering Logic
filtered_docs = st.session_state.doctors_master

if search_q:
    filtered_docs = [d for d in filtered_docs if search_q.lower() in d["name"].lower() or search_q.lower() in d["id"].lower()]

if selected_spec != "All Specialties":
    filtered_docs = [d for d in filtered_docs if d["specialty"] == selected_spec]

if selected_status != "All Status":
    filtered_docs = [d for d in filtered_docs if d["status"] == selected_status]

# Display Doctor Directory Table with Action Buttons (CRUD: Read, Update, Delete)
headers = st.columns([1.5, 2.5, 2, 1.5, 1.5, 2])
headers[0].markdown("**Doctor ID**")
headers[1].markdown("**Doctor Name**")
headers[2].markdown("**Specialty**")
headers[3].markdown("**Experience**")
headers[4].markdown("**Availability**")
headers[5].markdown("**Action**")

st.divider()

for idx, doc in enumerate(filtered_docs):
    c1, c2, c3, c4, c5, c6 = st.columns([1.5, 2.5, 2, 1.5, 1.5, 2])
    c1.write(doc["id"])
    c2.write(f"**{doc['name']}**")
    c3.write(doc["specialty"])
    c4.write(doc["exp"])
    
    # Status Badge
    if doc["status"] == "Available":
        c5.markdown('<span class="badge-avail">Available</span>', unsafe_allow_html=True)
    elif doc["status"] == "On Duty":
        c5.markdown('<span class="badge-duty">On Duty</span>', unsafe_allow_html=True)
    else:
        c5.markdown('<span class="badge-leave">On Leave</span>', unsafe_allow_html=True)

    # Actions: Edit / Delete (CRUD)
    col_e, col_d = c6.columns(2)
    
    if col_e.button("✏️ Edit", key=f"edit_{doc['id']}"):
        @st.dialog(f"Edit {doc['name']}")
        def edit_doc_dialog(d):
            with st.form("edit_doc_form"):
                n_name = st.text_input("Name", value=d["name"])
                n_spec = st.selectbox("Specialty", specs[1:], index=specs[1:].index(d["specialty"]) if d["specialty"] in specs[1:] else 0)
                n_exp = st.text_input("Experience", value=d["exp"])
                n_stat = st.selectbox("Status", ["Available", "On Duty", "On Leave"], index=["Available", "On Duty", "On Leave"].index(d["status"]))
                
                if st.form_submit_button("Update Doctor"):
                    d["name"] = n_name
                    d["specialty"] = n_spec
                    d["exp"] = n_exp
                    d["status"] = n_stat
                    st.success("Updated!")
                    st.rerun()
        edit_doc_dialog(doc)

    if col_d.button("🗑️", key=f"del_{doc['id']}"):
        st.session_state.doctors_master.remove(doc)
        st.success(f"{doc['name']} Deleted!")
        st.rerun()

st.caption(f"Showing {len(filtered_docs)} of {len(st.session_state.doctors_master)} Doctors")