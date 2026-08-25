import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Assign Product", page_icon="📦", layout="wide")

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
    
    .card-box { 
        background: #ffffff; 
        border-radius: 10px; 
        padding: 20px; 
        border: 1px solid #e2e8f0; 
        margin-bottom: 15px; 
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

# Session State for Assigned Products
if "assigned_products_list" not in st.session_state:
    st.session_state.assigned_products_list = [
        {"product": "Paracetamol 650mg", "category": "Tablet", "company": "MedPlus", "date": "24 May 2026"},
        {"product": "Aspirin 75mg", "category": "Tablet", "company": "HealthCare", "date": "20 May 2026"},
        {"product": "Atorvastatin 10mg", "category": "Tablet", "company": "Sun Pharma", "date": "18 May 2026"}
    ]

st.markdown("## 📦 Assign Product to Doctor")

# Selectors Row
col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Select Doctor")
    selected_doctor = st.selectbox(
        "Doctor", 
        ["Dr. Amit Sharma (Cardiology)", "Dr. Sneha Joshi (Neurology)", "Dr. Raj Mehta (Orthopedics)"],
        label_visibility="collapsed"
    )

with col2:
    st.markdown("##### Select Product")
    selected_product = st.selectbox(
        "Product", 
        ["Paracetamol 650mg", "Amoxicillin 500mg", "Azithromycin 500mg", "Omeprazole 20mg"],
        label_visibility="collapsed"
    )

st.write("")

# Details Grid Row
info_col1, info_col2 = st.columns(2)

# Doctor Info Card
with info_col1:
    doc_name = selected_doctor.split('(')[0].strip()
    doc_spec = selected_doctor.split('(')[1].replace(')', '').strip()
    
    st.markdown(f"""
    <div class="card-box">
        <b style="font-size: 16px;">Doctor Information</b>
        <hr style="margin: 10px 0; border: 0; border-top: 1px solid #e2e8f0;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 40px;">👨‍⚕️</div>
            <div>
                <div style="font-weight: bold; font-size: 16px;">{doc_name}</div>
                <div style="color: #64748b; font-size: 14px;">Specialty: {doc_spec}</div>
                <div style="font-size: 13px; margin-top: 4px;">Experience: 12 Years</div>
                <div style="font-size: 13px;">Contact: 9823456799</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Product Info Card
with info_col2:
    st.markdown(f"""
    <div class="card-box">
        <b style="font-size: 16px;">Product Information</b>
        <hr style="margin: 10px 0; border: 0; border-top: 1px solid #e2e8f0;">
        <div style="font-weight: bold; font-size: 16px; margin-bottom: 4px;">Medicine: {selected_product}</div>
        <div style="font-size: 13px; color: #475569;">Category: Tablet</div>
        <div style="font-size: 13px; color: #475569;">Company: MedPlus Pharmaceuticals</div>
        <div style="font-size: 13px; color: #475569;">Available Stock: 1200 Units</div>
        <div style="font-size: 13px; color: #475569;">Expiry: 30 Jun 2027</div>
    </div>
    """, unsafe_allow_html=True)

# Assign Action Button
if st.button("Assign Product", type="primary", use_container_width=True):
    st.session_state.assigned_products_list.insert(0, {
        "product": selected_product,
        "category": "Tablet",
        "company": "MedPlus",
        "date": datetime.now().strftime("%d %b %Y")
    })
    st.success(f"Successfully assigned {selected_product} to {selected_doctor.split('(')[0]}!")
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