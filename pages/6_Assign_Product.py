import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Assign Product", page_icon="📦", layout="wide")

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
    
    /* Page Specific Cards */
    .card-box { 
        background: #ffffff; 
        border-radius: 10px; 
        padding: 20px; 
        border: 1px solid #e2e8f0; 
        margin-bottom: 15px; 
    }
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
    
    # 🚪 GUARANTEED WORKING LOGOUT
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.switch_page("app.py")

# ----------------- DATA DICTIONARIES (DYNAMIC DATA) -----------------
doctors_db = {
    "Dr. Amit Sharma (Cardiology)": {
        "name": "Dr. Amit Sharma",
        "specialty": "Cardiology",
        "exp": "15 Years",
        "contact": "9876543210",
        "icon": "👨‍⚕️"
    },
    "Dr. Sneha Joshi (Neurology)": {
        "name": "Dr. Sneha Joshi",
        "specialty": "Neurology",
        "exp": "10 Years",
        "contact": "9812345678",
        "icon": "👩‍⚕️"
    },
    "Dr. Raj Mehta (Orthopedics)": {
        "name": "Dr. Raj Mehta",
        "specialty": "Orthopedics",
        "exp": "12 Years",
        "contact": "9823456799",
        "icon": "👨‍⚕️"
    }
}

products_db = {
    "Paracetamol 650mg": {
        "category": "Tablet",
        "company": "MedPlus Pharmaceuticals",
        "stock": "1500 Units",
        "expiry": "15 Dec 2026"
    },
    "Amoxicillin 500mg": {
        "category": "Capsule",
        "company": "Sun Pharma",
        "stock": "800 Units",
        "expiry": "20 Oct 2026"
    },
    "Azithromycin 500mg": {
        "category": "Tablet",
        "company": "Cipla Ltd",
        "stock": "1200 Units",
        "expiry": "30 Jun 2027"
    },
    "Omeprazole 20mg": {
        "category": "Capsule",
        "company": "Dr. Reddy's",
        "stock": "650 Units",
        "expiry": "10 Aug 2027"
    }
}

# Session State for Assigned Products
if "assigned_products_list" not in st.session_state:
    st.session_state.assigned_products_list = [
        {"product": "Paracetamol 650mg", "category": "Tablet", "company": "MedPlus Pharmaceuticals", "date": "24 May 2026"},
        {"product": "Aspirin 75mg", "category": "Tablet", "company": "HealthCare", "date": "20 May 2026"},
        {"product": "Atorvastatin 10mg", "category": "Tablet", "company": "Sun Pharma", "date": "18 May 2026"}
    ]

st.markdown("## 📦 Assign Product to Doctor")

# Selectors Row
col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Select Doctor")
    selected_doctor_key = st.selectbox(
        "Doctor", 
        list(doctors_db.keys()),
        label_visibility="collapsed"
    )

with col2:
    st.markdown("##### Select Product")
    selected_product_key = st.selectbox(
        "Product", 
        list(products_db.keys()),
        label_visibility="collapsed"
    )

# Get selected data object dynamically
current_doc = doctors_db[selected_doctor_key]
current_prod = products_db[selected_product_key]

st.write("")

# Details Grid Row (DYNAMICALLY UPDATING CARDS)
info_col1, info_col2 = st.columns(2)

# Dynamic Doctor Info Card
with info_col1:
    st.markdown(f"""
    <div class="card-box">
        <b style="font-size: 16px;">Doctor Information</b>
        <hr style="margin: 10px 0; border: 0; border-top: 1px solid #e2e8f0;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 40px;">{current_doc['icon']}</div>
            <div>
                <div style="font-weight: bold; font-size: 16px;">{current_doc['name']}</div>
                <div style="color: #64748b; font-size: 14px;">Specialty: {current_doc['specialty']}</div>
                <div style="font-size: 13px; margin-top: 4px;">Experience: {current_doc['exp']}</div>
                <div style="font-size: 13px;">Contact: {current_doc['contact']}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Dynamic Product Info Card
with info_col2:
    st.markdown(f"""
    <div class="card-box">
        <b style="font-size: 16px;">Product Information</b>
        <hr style="margin: 10px 0; border: 0; border-top: 1px solid #e2e8f0;">
        <div style="font-weight: bold; font-size: 16px; margin-bottom: 4px;">Medicine: {selected_product_key}</div>
        <div style="font-size: 13px; color: #475569;">Category: {current_prod['category']}</div>
        <div style="font-size: 13px; color: #475569;">Company: {current_prod['company']}</div>
        <div style="font-size: 13px; color: #475569;">Available Stock: {current_prod['stock']}</div>
        <div style="font-size: 13px; color: #475569;">Expiry: {current_prod['expiry']}</div>
    </div>
    """, unsafe_allow_html=True)

# Assign Action Button
if st.button("Assign Product", type="primary", use_container_width=True):
    st.session_state.assigned_products_list.insert(0, {
        "product": selected_product_key,
        "category": current_prod['category'],
        "company": current_prod['company'],
        "date": datetime.now().strftime("%d %b %Y")
    })
    st.success(f"Successfully assigned {selected_product_key} to {current_doc['name']}!")
    st.rerun()

st.write("---")

# Assigned Products Table (CRUD View & Delete)
st.markdown("### Assigned Products History")

headers = st.columns([2.5, 2, 2, 2, 1.5])
headers[0].markdown("**Product Name**")
headers[1].markdown("**Category**")
headers[2].markdown("**Company**")
headers[3].markdown("**Assigned Date**")
headers[4].markdown("**Action**")

st.divider()

for idx, item in enumerate(st.session_state.assigned_products_list):
    c1, c2, c3, c4, c5 = st.columns([2.5, 2, 2, 2, 1.5])
    c1.write(f"**{item['product']}**")
    c2.write(item["category"])
    c3.write(item["company"])
    c4.write(item["date"])
    
    if c5.button("🗑️ Delete", key=f"del_assign_{idx}"):
        st.session_state.assigned_products_list.pop(idx)
        st.success("Assignment removed!")
        st.rerun()

st.caption(f"Showing {len(st.session_state.assigned_products_list)} Assigned Records")