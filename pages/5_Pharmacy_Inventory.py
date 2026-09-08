import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pharmacy Inventory", page_icon="💊", layout="wide")

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
    
    /* Page Specific Custom Cards & Badges */
    .kpi-card { background: #ffffff; border-radius: 10px; padding: 14px 18px; border: 1px solid #e2e8f0; }
    .kpi-title { font-size: 13px; color: #64748b; font-weight: 600; }
    .kpi-val { font-size: 24px; font-weight: 800; color: #0f172a; margin: 2px 0; }
    .badge-instock { background-color: #dcfce7; color: #16a34a; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
    .badge-lowstock { background-color: #fef3c7; color: #d97706; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
    .badge-outstock { background-color: #fee2e2; color: #dc2626; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 12px; }
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

# Session State for Pharmacy Inventory (Master Data)
if "pharmacy_master" not in st.session_state:
    st.session_state.pharmacy_master = [
        {"name": "Paracetamol 650mg", "category": "Tablet", "batch": "B12345", "stock": 1200, "expiry": "30 Jun 2027", "status": "In Stock"},
        {"name": "Amoxicillin 500mg", "category": "Antibiotic", "batch": "B12346", "stock": 230, "expiry": "25 May 2027", "status": "Low Stock"},
        {"name": "Azithromycin 500mg", "category": "Antibiotic", "batch": "B12347", "stock": 50, "expiry": "10 May 2027", "status": "Low Stock"},
        {"name": "Omeprazole 20mg", "category": "Capsule", "batch": "B12348", "stock": 0, "expiry": "15 Apr 2027", "status": "Out of Stock"},
        {"name": "Cetirizine 10mg", "category": "Tablet", "batch": "B12349", "stock": 300, "expiry": "20 Jun 2027", "status": "In Stock"},
        {"name": "Diclofenac 50mg", "category": "Tablet", "batch": "B12350", "stock": 80, "expiry": "18 May 2027", "status": "Low Stock"}
    ]

# Header
st.markdown("## 💊 Pharmacy Inventory")

# Metric Summary Row
c1, c2, c3, c4, c5 = st.columns(5)
total_prods = len(st.session_state.pharmacy_master)
in_stock = len([m for m in st.session_state.pharmacy_master if m["status"] == "In Stock"])
low_stock = len([m for m in st.session_state.pharmacy_master if m["status"] == "Low Stock"])
out_stock = len([m for m in st.session_state.pharmacy_master if m["status"] == "Out of Stock"])

c1.markdown(f'<div class="kpi-card"><div class="kpi-title">Total Products</div><div class="kpi-val">{total_prods}</div></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="kpi-card"><div class="kpi-title">In Stock</div><div class="kpi-val" style="color:#16a34a;">{in_stock}</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="kpi-card"><div class="kpi-title">Low Stock</div><div class="kpi-val" style="color:#d97706;">{low_stock}</div></div>', unsafe_allow_html=True)
c4.markdown(f'<div class="kpi-card"><div class="kpi-title">Out of Stock</div><div class="kpi-val" style="color:#dc2626;">{out_stock}</div></div>', unsafe_allow_html=True)
c5.markdown('<div class="kpi-card"><div class="kpi-title">Expiring Soon</div><div class="kpi-val" style="color:#d97706;">12</div></div>', unsafe_allow_html=True)

st.write("")

# Search, Filter and Add Medicine Action
col_s, col_c, col_b = st.columns([4, 3, 2])

with col_s:
    search_q = st.text_input("Search Medicine", placeholder="Search medicine name, batch...", label_visibility="collapsed")

with col_c:
    selected_cat = st.selectbox("Category", ["All Categories", "Tablet", "Capsule", "Antibiotic", "Syrup", "Injection"], label_visibility="collapsed")

with col_b:
    add_btn = st.button("➕ Add Medicine", use_container_width=True, type="primary")

# Modal Dialog for Adding New Medicine (CRUD: Create)
if add_btn:
    @st.dialog("➕ Add New Medicine")
    def add_med_dialog():
        with st.form("new_med_form"):
            m_name = st.text_input("Medicine Name")
            m_cat = st.selectbox("Category", ["Tablet", "Capsule", "Antibiotic", "Syrup", "Injection"])
            m_batch = st.text_input("Batch No.", f"B{12350 + len(st.session_state.pharmacy_master)}")
            m_stock = st.number_input("Stock Quantity", min_value=0, value=100)
            m_expiry = st.text_input("Expiry Date", "30 Jun 2027")
            
            # Auto status logic
            m_status = "In Stock" if m_stock > 250 else ("Low Stock" if m_stock > 0 else "Out of Stock")

            if st.form_submit_button("Save Medicine", use_container_width=True):
                if m_name:
                    st.session_state.pharmacy_master.append({
                        "name": m_name, "category": m_cat, "batch": m_batch,
                        "stock": m_stock, "expiry": m_expiry, "status": m_status
                    })
                    st.success("Medicine added to inventory!")
                    st.rerun()

    add_med_dialog()

st.write("")

# Filtering Logic
filtered_meds = st.session_state.pharmacy_master

if search_q:
    filtered_meds = [m for m in filtered_meds if search_q.lower() in m["name"].lower() or search_q.lower() in m["batch"].lower()]

if selected_cat != "All Categories":
    filtered_meds = [m for m in filtered_meds if m["category"] == selected_cat]

# Display Table with Actions (CRUD: Read, Update, Delete)
headers = st.columns([2.5, 1.5, 1.5, 1.2, 1.8, 1.5, 1.8])
headers[0].markdown("**Medicine Name**")
headers[1].markdown("**Category**")
headers[2].markdown("**Batch No.**")
headers[3].markdown("**Stock**")
headers[4].markdown("**Expiry Date**")
headers[5].markdown("**Status**")
headers[6].markdown("**Action**")

st.divider()

for idx, med in enumerate(filtered_meds):
    c1, c2, c3, c4, c5, c6, c7 = st.columns([2.5, 1.5, 1.5, 1.2, 1.8, 1.5, 1.8])
    c1.write(f"**{med['name']}**")
    c2.write(med["category"])
    c3.write(med["batch"])
    c4.write(str(med["stock"]))
    c5.write(med["expiry"])

    # Badges
    if med["status"] == "In Stock":
        c6.markdown('<span class="badge-instock">In Stock</span>', unsafe_allow_html=True)
    elif med["status"] == "Low Stock":
        c6.markdown('<span class="badge-lowstock">Low Stock</span>', unsafe_allow_html=True)
    else:
        c6.markdown('<span class="badge-outstock">Out of Stock</span>', unsafe_allow_html=True)

    # Actions: Edit / Delete (CRUD)
    col_e, col_d = c7.columns(2)

    if col_e.button("✏️", key=f"edit_med_{idx}"):
        @st.dialog(f"Edit {med['name']}")
        def edit_med_dialog(m):
            with st.form("edit_med_form"):
                n_name = st.text_input("Name", value=m["name"])
                n_cat = st.selectbox("Category", ["Tablet", "Capsule", "Antibiotic", "Syrup", "Injection"], index=["Tablet", "Capsule", "Antibiotic", "Syrup", "Injection"].index(m["category"]))
                n_batch = st.text_input("Batch", value=m["batch"])
                n_stock = st.number_input("Stock", value=int(m["stock"]))
                n_expiry = st.text_input("Expiry Date", value=m["expiry"])
                
                n_status = "In Stock" if n_stock > 250 else ("Low Stock" if n_stock > 0 else "Out of Stock")

                if st.form_submit_button("Update Stock"):
                    m["name"] = n_name
                    m["category"] = n_cat
                    m["batch"] = n_batch
                    m["stock"] = n_stock
                    m["expiry"] = n_expiry
                    m["status"] = n_status
                    st.success("Stock updated!")
                    st.rerun()

        edit_med_dialog(med)

    if col_d.button("🗑️", key=f"del_med_{idx}"):
        st.session_state.pharmacy_master.remove(med)
        st.success(f"{med['name']} Removed!")
        st.rerun()

st.caption(f"Showing {len(filtered_meds)} Medicines")