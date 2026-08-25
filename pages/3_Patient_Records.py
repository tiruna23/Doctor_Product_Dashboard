import streamlit as st
import pandas as pd

st.set_page_config(page_title="Patient Records", page_icon="👤", layout="wide")

# Custom CSS matching Image #4 & Dark Navy Blue Sidebar
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
    
    .badge-admitted { background-color: #fef3c7; color: #d97706; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
    .badge-outpatient { background-color: #dbeafe; color: #2563eb; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
    .badge-icu { background-color: #fee2e2; color: #dc2626; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
    .badge-discharged { background-color: #dcfce7; color: #16a34a; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
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

# Session State for Patient Data (Master Data)
if "patients_master" not in st.session_state:
    st.session_state.patients_master = [
        {"id": "PAT001", "name": "Rahul Patil", "age": 32, "gender": "Male", "phone": "9876543210", "disease": "Fever & Cold", "doctor": "Dr. Amit Sharma", "status": "Admitted"},
        {"id": "PAT002", "name": "Priya Deshmukh", "age": 28, "gender": "Female", "phone": "9812345678", "disease": "Migraine", "doctor": "Dr. Sneha Joshi", "status": "Outpatient"},
        {"id": "PAT003", "name": "Karan Singh", "age": 45, "gender": "Male", "phone": "9765432109", "disease": "Fracture", "doctor": "Dr. Raj Mehta", "status": "Admitted"},
        {"id": "PAT004", "name": "Anjali Desai", "age": 36, "gender": "Female", "phone": "9988776655", "disease": "Skin Rash", "doctor": "Dr. Karan Patel", "status": "Outpatient"},
        {"id": "PAT005", "name": "Vikram Joshi", "age": 52, "gender": "Male", "phone": "9822334455", "disease": "Chest Pain", "doctor": "Dr. Amit Sharma", "status": "ICU"},
        {"id": "PAT006", "name": "Sneha Gupta", "age": 29, "gender": "Female", "phone": "9711223344", "disease": "Pregnancy Checkup", "doctor": "Dr. Neha Singh", "status": "Outpatient"},
        {"id": "PAT007", "name": "Rohit Verma", "age": 38, "gender": "Male", "phone": "9655443322", "disease": "Sinusitis", "doctor": "Dr. Rohit Kumar", "status": "Discharged"}
    ]

# Top Header & Actions
st.markdown("## 👤 Patient Records")

col_search, col_status, col_btn = st.columns([5, 3, 2])

with col_search:
    search_q = st.text_input("Search Patient", placeholder="Search patient name, ID or disease...", label_visibility="collapsed")

with col_status:
    selected_status = st.selectbox("Status", ["All Status", "Admitted", "Outpatient", "ICU", "Discharged"], label_visibility="collapsed")

with col_btn:
    add_btn = st.button("➕ Add Patient", use_container_width=True, type="primary")

# Modal Dialog for Adding New Patient (CRUD: Create)
if add_btn:
    @st.dialog("➕ Add New Patient")
    def add_patient_dialog():
        with st.form("new_patient_form"):
            p_id = f"PAT00{len(st.session_state.patients_master)+1}"
            p_name = st.text_input("Patient Name")
            c1, c2 = st.columns(2)
            p_age = c1.number_input("Age", min_value=1, max_value=120, value=30)
            p_gender = c2.selectbox("Gender", ["Male", "Female", "Other"])
            p_phone = st.text_input("Phone Number")
            p_disease = st.text_input("Disease / Diagnosis")
            p_doctor = st.text_input("Assigned Doctor", "Dr. Amit Sharma")
            p_status = st.selectbox("Status", ["Admitted", "Outpatient", "ICU", "Discharged"])

            if st.form_submit_button("Save Patient", use_container_width=True):
                if p_name:
                    st.session_state.patients_master.append({
                        "id": p_id, "name": p_name, "age": p_age, "gender": p_gender,
                        "phone": p_phone, "disease": p_disease, "doctor": p_doctor, "status": p_status
                    })
                    st.success("Patient added successfully!")
                    st.rerun()

    add_patient_dialog()

st.write("")

# Filtering Logic
filtered_patients = st.session_state.patients_master

if search_q:
    filtered_patients = [p for p in filtered_patients if search_q.lower() in p["name"].lower() or search_q.lower() in p["id"].lower() or search_q.lower() in p["disease"].lower()]

if selected_status != "All Status":
    filtered_patients = [p for p in filtered_patients if p["status"] == selected_status]

# Display Patient Records Table with Actions (CRUD: Read, Update, Delete)
headers = st.columns([1.2, 2.2, 1, 1.8, 2, 2, 1.5, 1.8])
headers[0].markdown("**Patient ID**")
headers[1].markdown("**Patient Name**")
headers[2].markdown("**Age/Gender**")
headers[3].markdown("**Phone**")
headers[4].markdown("**Disease**")
headers[5].markdown("**Doctor**")
headers[6].markdown("**Status**")
headers[7].markdown("**Action**")

st.divider()

for idx, pat in enumerate(filtered_patients):
    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns([1.2, 2.2, 1, 1.8, 2, 2, 1.5, 1.8])
    c1.write(pat["id"])
    c2.write(f"**{pat['name']}**")
    c3.write(f"{pat['age']} / {pat['gender'][0]}")
    c4.write(pat["phone"])
    c5.write(pat["disease"])
    c6.write(pat["doctor"])

    # Status Badges
    if pat["status"] == "Admitted":
        c7.markdown('<span class="badge-admitted">Admitted</span>', unsafe_allow_html=True)
    elif pat["status"] == "Outpatient":
        c7.markdown('<span class="badge-outpatient">Outpatient</span>', unsafe_allow_html=True)
    elif pat["status"] == "ICU":
        c7.markdown('<span class="badge-icu">ICU</span>', unsafe_allow_html=True)
    else:
        c7.markdown('<span class="badge-discharged">Discharged</span>', unsafe_allow_html=True)

    # Actions: Edit / Delete (CRUD)
    col_e, col_d = c8.columns(2)

    if col_e.button("✏️", key=f"edit_pat_{pat['id']}"):
        @st.dialog(f"Edit Patient: {pat['name']}")
        def edit_patient_dialog(p):
            with st.form("edit_patient_form"):
                n_name = st.text_input("Name", value=p["name"])
                c_a, c_g = st.columns(2)
                n_age = c_a.number_input("Age", value=int(p["age"]))
                n_gender = c_g.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(p["gender"]))
                n_phone = st.text_input("Phone", value=p["phone"])
                n_disease = st.text_input("Disease", value=p["disease"])
                n_doctor = st.text_input("Doctor", value=p["doctor"])
                n_status = st.selectbox("Status", ["Admitted", "Outpatient", "ICU", "Discharged"], index=["Admitted", "Outpatient", "ICU", "Discharged"].index(p["status"]))

                if st.form_submit_button("Update Patient"):
                    p["name"] = n_name
                    p["age"] = n_age
                    p["gender"] = n_gender
                    p["phone"] = n_phone
                    p["disease"] = n_disease
                    p["doctor"] = n_doctor
                    p["status"] = n_status
                    st.success("Patient Record Updated!")
                    st.rerun()

        edit_patient_dialog(pat)

    if col_d.button("🗑️", key=f"del_pat_{pat['id']}"):
        st.session_state.patients_master.remove(pat)
        st.success(f"{pat['name']} Record Deleted!")
        st.rerun()

st.caption(f"Showing {len(filtered_patients)} to {len(st.session_state.patients_master)} Patient Records")