import streamlit as st
import pandas as pd

st.set_page_config(page_title="Billing & Invoicing", page_icon="💳", layout="wide")

# Custom Styling matching Theme & Dark Navy Blue Sidebar
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
    .badge-paid { background-color: #dcfce7; color: #16a34a; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
    .badge-unpaid { background-color: #fee2e2; color: #dc2626; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
    .badge-pending { background-color: #fef3c7; color: #d97706; padding: 3px 10px; border-radius: 12px; font-weight: 600; font-size: 11px; }
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

# Session State for Billing Data Master
if "billing_master" not in st.session_state:
    st.session_state.billing_master = [
        {"inv": "INV-1001", "patient": "Rahul Patil", "date": "2026-08-24", "amount": 12500, "status": "Paid", "method": "UPI / Online"},
        {"inv": "INV-1002", "patient": "Priya Deshmukh", "date": "2026-08-24", "amount": 4200, "status": "Unpaid", "method": "Pending"},
        {"inv": "INV-1003", "patient": "Karan Singh", "date": "2026-08-23", "amount": 28900, "status": "Paid", "method": "Credit Card"},
        {"inv": "INV-1004", "patient": "Anjali Desai", "date": "2026-08-22", "amount": 1500, "status": "Paid", "method": "Cash"},
        {"inv": "INV-1005", "patient": "Vikram Joshi", "date": "2026-08-21", "amount": 65000, "status": "Pending", "method": "Insurance"}
    ]

# Header
st.markdown("## 💳 Billing & Invoicing")

# Calculate Metrics
total_rev = sum([item["amount"] for item in st.session_state.billing_master if item["status"] == "Paid"])
unpaid_rev = sum([item["amount"] for item in st.session_state.billing_master if item["status"] == "Unpaid"])
pending_rev = sum([item["amount"] for item in st.session_state.billing_master if item["status"] == "Pending"])

# Summary Cards Row
c1, c2, c3, c4 = st.columns(4)
c1.markdown(f'<div class="kpi-card"><div class="kpi-title">Total Revenue Collected</div><div class="kpi-val" style="color:#16a34a;">₹{total_rev:,}</div></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="kpi-card"><div class="kpi-title">Unpaid Revenue</div><div class="kpi-val" style="color:#dc2626;">₹{unpaid_rev:,}</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="kpi-card"><div class="kpi-title">Pending Claims / Insurance</div><div class="kpi-val" style="color:#d97706;">₹{pending_rev:,}</div></div>', unsafe_allow_html=True)
c4.markdown(f'<div class="kpi-card"><div class="kpi-title">Total Invoices</div><div class="kpi-val">{len(st.session_state.billing_master)}</div></div>', unsafe_allow_html=True)

st.write("")

# Actions & Search Bar
col_s, col_st, col_b = st.columns([4, 3, 2])

with col_s:
    search_q = st.text_input("Search Invoice", placeholder="Search by patient name or invoice ID...", label_visibility="collapsed")

with col_st:
    selected_status = st.selectbox("Status Filter", ["All Status", "Paid", "Unpaid", "Pending"], label_visibility="collapsed")

with col_b:
    add_btn = st.button("➕ Generate Invoice", type="primary", use_container_width=True)

# Dialog for Generating New Invoice (CRUD: Create)
if add_btn:
    @st.dialog("➕ Create New Invoice")
    def add_invoice_dialog():
        with st.form("new_inv_form"):
            inv_id = f"INV-{1001 + len(st.session_state.billing_master)}"
            p_name = st.text_input("Patient Name")
            amt = st.number_input("Bill Amount (₹)", min_value=100, value=2500, step=500)
            inv_date = st.date_input("Invoice Date")
            p_status = st.selectbox("Payment Status", ["Paid", "Unpaid", "Pending"])
            p_method = st.selectbox("Payment Method", ["Cash", "UPI / Online", "Credit Card", "Insurance", "Pending"])

            if st.form_submit_button("Generate Bill", use_container_width=True):
                if p_name:
                    st.session_state.billing_master.insert(0, {
                        "inv": inv_id, "patient": p_name, "date": str(inv_date),
                        "amount": amt, "status": p_status, "method": p_method
                    })
                    st.success("Invoice generated successfully!")
                    st.rerun()

    add_invoice_dialog()

st.write("")

# Filtering Data
filtered_bills = st.session_state.billing_master

if search_q:
    filtered_bills = [b for b in filtered_bills if search_q.lower() in b["patient"].lower() or search_q.lower() in b["inv"].lower()]

if selected_status != "All Status":
    filtered_bills = [b for b in filtered_bills if b["status"] == selected_status]

# Table Header
headers = st.columns([1.5, 2.5, 1.8, 1.8, 1.8, 1.5, 1.8])
headers[0].markdown("**Invoice ID**")
headers[1].markdown("**Patient Name**")
headers[2].markdown("**Date**")
headers[3].markdown("**Amount**")
headers[4].markdown("**Payment Method**")
headers[5].markdown("**Status**")
headers[6].markdown("**Action**")

st.divider()

# Invoice Table Records (CRUD: Read, Update, Delete)
for idx, bill in enumerate(filtered_bills):
    c1, c2, c3, c4, c5, c6, c7 = st.columns([1.5, 2.5, 1.8, 1.8, 1.8, 1.5, 1.8])
    c1.write(bill["inv"])
    c2.write(f"**{bill['patient']}**")
    c3.write(bill["date"])
    c4.write(f"**₹{bill['amount']:,}**")
    c5.write(bill["method"])

    # Badges
    if bill["status"] == "Paid":
        c6.markdown('<span class="badge-paid">Paid</span>', unsafe_allow_html=True)
    elif bill["status"] == "Unpaid":
        c6.markdown('<span class="badge-unpaid">Unpaid</span>', unsafe_allow_html=True)
    else:
        c6.markdown('<span class="badge-pending">Pending</span>', unsafe_allow_html=True)

    # Actions: Edit / Delete
    col_e, col_d = c7.columns(2)

    if col_e.button("✏️", key=f"edit_inv_{bill['inv']}"):
        @st.dialog(f"Edit Invoice: {bill['inv']}")
        def edit_inv_dialog(b):
            with st.form("edit_inv_form"):
                n_pat = st.text_input("Patient", value=b["patient"])
                n_amt = st.number_input("Amount (₹)", value=int(b["amount"]))
                n_date = st.text_input("Date", value=b["date"])
                n_status = st.selectbox("Status", ["Paid", "Unpaid", "Pending"], index=["Paid", "Unpaid", "Pending"].index(b["status"]))
                n_method = st.selectbox("Payment Method", ["Cash", "UPI / Online", "Credit Card", "Insurance", "Pending"], index=["Cash", "UPI / Online", "Credit Card", "Insurance", "Pending"].index(b["method"]) if b["method"] in ["Cash", "UPI / Online", "Credit Card", "Insurance", "Pending"] else 0)

                if st.form_submit_button("Update Invoice"):
                    b["patient"] = n_pat
                    b["amount"] = n_amt
                    b["date"] = n_date
                    b["status"] = n_status
                    b["method"] = n_method
                    st.success("Invoice Updated!")
                    st.rerun()

        edit_inv_dialog(bill)

    if col_d.button("🗑️", key=f"del_inv_{bill['inv']}"):
        st.session_state.billing_master.remove(bill)
        st.success("Invoice Deleted!")
        st.rerun()

st.caption(f"Showing {len(filtered_bills)} Invoices")