import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊", layout="wide")

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
    
    .kpi-card { background: #ffffff; border-radius: 10px; padding: 14px; border: 1px solid #e2e8f0; }
    .kpi-title { font-size: 13px; color: #64748b; font-weight: 600; }
    .kpi-val { font-size: 24px; font-weight: 800; color: #0f172a; margin: 2px 0; }
    .badge-green { color: #16a34a; font-size: 11px; font-weight: 600; }
    .box-card { background: #ffffff; border-radius: 10px; padding: 18px; border: 1px solid #e2e8f0; margin-top: 15px; }
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


# Top Header Bar
h1, h2 = st.columns([3, 1])
with h1:
    st.markdown("## 📊 Analytics Dashboard")
with h2:
    st.selectbox("Timeframe", ["This Month", "Last Month", "This Year"], label_visibility="collapsed")

# Top KPI Metric Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Total Patients</div><div class="kpi-val">1,452</div><span class="badge-green">▲ 115.3%</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Appointments</div><div class="kpi-val">562</div><span class="badge-green">▲ 112.3%</span></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Bed Occupancy</div><div class="kpi-val">57%</div><span class="badge-green">▲ 5.4%</span></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="kpi-card"><div class="kpi-title">Revenue</div><div class="kpi-val">₹ 18,75,000</div><span class="badge-green">▲ 115.3%</span></div>', unsafe_allow_html=True)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# Row 1: Patient Growth & Appointment Analytics
col_a, col_b = st.columns(2)

with col_a:
    st.markdown('<div class="box-card"><b>Patient Growth</b>', unsafe_allow_html=True)
    fig_growth = go.Figure()
    fig_growth.add_trace(go.Scatter(
        x=months, y=[400, 800, 1200, 1600, 2000],
        mode='lines+markers',
        line=dict(color='#0284c7', width=3),
        marker=dict(size=8)
    ))
    fig_growth.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=230, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_growth, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="box-card"><b>Appointment Analytics</b>', unsafe_allow_html=True)
    fig_app = go.Figure()
    fig_app.add_trace(go.Bar(
        x=months, y=[300, 450, 600, 500, 650],
        marker_color='#6366f1',
        marker_line=dict(color='#4f46e5', width=1.5)
    ))
    fig_app.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=230, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_app, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2: Gender Pie Chart, Bed Occupancy Pie Chart & Dotted Revenue Overview
g1, g2, g3 = st.columns(3)

with g1:
    st.markdown('<div class="box-card"><b>Patient by Gender</b>', unsafe_allow_html=True)
    fig_gender = px.pie(
        names=['Male', 'Female'],
        values=[836, 616],
        hole=0.5,
        color_discrete_sequence=['#2563eb', '#ec4899']
    )
    fig_gender.update_traces(textinfo='percent+label', hoverinfo='label+value')
    fig_gender.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=220, showlegend=False)
    st.plotly_chart(fig_gender, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with g2:
    st.markdown('<div class="box-card"><b>Bed Occupancy</b>', unsafe_allow_html=True)
    fig_bed = px.pie(
        names=['Occupied', 'Available'],
        values=[114, 86],
        hole=0.5,
        color_discrete_sequence=['#f59e0b', '#10b981']
    )
    fig_bed.update_traces(textinfo='percent+label', hoverinfo='label+value')
    fig_bed.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=220, showlegend=False)
    st.plotly_chart(fig_bed, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with g3:
    st.markdown('<div class="box-card"><b>Revenue Overview (₹ Lakhs)</b>', unsafe_allow_html=True)
    fig_rev = go.Figure()
    fig_rev.add_trace(go.Scatter(
        x=months, y=[5, 8, 12, 15, 18.75],
        mode='lines+markers',
        line=dict(color='#16a34a', width=3, dash='dot'),
        marker=dict(size=8, color='#15803d')
    ))
    fig_rev.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=220, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_rev, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)