import streamlit as st
import plotly.express as px

from models.dashboard_model import (
    get_total_products,
    get_total_doctors,
    get_total_assignments,
    get_total_companies,
    get_recent_products,
    get_recent_doctors,
    get_recent_assignments,
    get_company_wise_products,
    get_specialty_wise_doctors
)

from models.schedule_model import get_total_schedules
from components.sidebar import show_sidebar

# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="MediCare Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Render Sidebar Component
show_sidebar()

# External CSS Import
try:
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# =====================================================
# PAGE HEADER
# =====================================================
st.markdown("""
    <div>
        <div class="welcome-title">🏥 <span>MediCare Dashboard</span></div>
        <div class="welcome-subtitle">Doctor Product Management & Analytics Overview</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# =====================================================
# LOAD DATA & KPI METRICS
# =====================================================
total_products = get_total_products()
total_doctors = get_total_doctors()
total_assignments = get_total_assignments()
total_companies = get_total_companies()
total_schedules = get_total_schedules()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon blue">💊</div>
            <div>
                <div class="kpi-label">Products</div>
                <div class="kpi-value">{total_products}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon green">👨‍⚕️</div>
            <div>
                <div class="kpi-label">Doctors</div>
                <div class="kpi-value">{total_doctors}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon purple">🔗</div>
            <div>
                <div class="kpi-label">Mappings</div>
                <div class="kpi-value">{total_assignments}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon yellow">🏢</div>
            <div>
                <div class="kpi-label">Companies</div>
                <div class="kpi-value">{total_companies}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon red">📅</div>
            <div>
                <div class="kpi-label">Appointments</div>
                <div class="kpi-value">{total_schedules}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# =====================================================
# QUICK ACCESS NAVIGATION
# =====================================================
st.markdown("<div class='chart-header'>⚡ Quick Access</div>", unsafe_allow_html=True)

quick1, quick2, quick3, quick4, quick5 = st.columns(5)

with quick1:
    with st.container():
        st.page_link("pages/Doctor_Master.py", label="👨‍⚕️ Doctors", use_container_width=True)

with quick2:
    with st.container():
        st.page_link("pages/Product_Master.py", label="💊 Products", use_container_width=True)

with quick3:
    with st.container():
        st.page_link("pages/Patient_Master.py", label="👤 Patients", use_container_width=True)

with quick4:
    with st.container():
        st.page_link("pages/Schedule.py", label="📅 Schedules", use_container_width=True)

with quick5:
    with st.container():
        st.page_link("pages/Assign_Product.py", label="🔗 Product Mapping", use_container_width=True)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# =====================================================
# ANALYTICS & CHARTS
# =====================================================
st.markdown("<div class='chart-header'>📈 System Analytics</div>", unsafe_allow_html=True)

left_chart, right_chart = st.columns(2)

with left_chart:
    st.caption("💊 Products Distribution by Company")
    company_df = get_company_wise_products()

    if not company_df.empty:
        fig_company = px.pie(
            company_df,
            names="company_name",
            values="Total",
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_company.update_traces(textinfo="percent+label")
        fig_company.update_layout(
            height=320,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False
        )
        st.plotly_chart(fig_company, use_container_width=True)
    else:
        st.info("No product analytics available.")

with right_chart:
    st.caption("👨‍⚕️ Doctors Count by Specialty")
    specialty_df = get_specialty_wise_doctors()

    if not specialty_df.empty:
        fig_specialty = px.bar(
            specialty_df,
            x="Total",
            y="specialty",
            orientation="h",
            color="specialty",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_specialty.update_layout(
            height=320,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False
        )
        st.plotly_chart(fig_specialty, use_container_width=True)
    else:
        st.info("No doctor analytics available.")

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# =====================================================
# RECENT ACTIVITY TABLES
# =====================================================
st.markdown("<div class='chart-header'>🕒 Recent Activity Records</div>", unsafe_allow_html=True)

left_table, right_table = st.columns(2)

with left_table:
    st.caption("Recent Products")
    products = get_recent_products()
    if not products.empty:
        st.dataframe(products, hide_index=True, use_container_width=True)
    else:
        st.info("No recent products.")

with right_table:
    st.caption("Recent Doctors")
    doctors = get_recent_doctors()
    if not doctors.empty:
        st.dataframe(doctors, hide_index=True, use_container_width=True)
    else:
        st.info("No recent doctors.")

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

st.caption("Recent Product Assignments")
assignments = get_recent_assignments()
if not assignments.empty:
    st.dataframe(assignments, hide_index=True, use_container_width=True)
else:
    st.info("No recent product mappings.")

# Footer
st.markdown('<div class="footer">MediCare Management Dashboard • Powered by Streamlit</div>', unsafe_allow_html=True)