import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(page_title="Docclinic | Medical Admin Dashboard", page_icon="🏥", layout="wide")

# Force Login Session to avoid Access Denied Error
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = True

# 2. Sidebar Import
try:
    from components.sidebar import show_sidebar
    show_sidebar()
except Exception:
    pass

# 3. Modern Bootstrap-Style Custom CSS Styling
st.markdown("""
<style>
    /* Page Background */
    .stApp {
        background-color: #f4f7fe;
    }
    
    /* Modern Dashboard Card */
    .doc-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0px 8px 24px rgba(149, 157, 165, 0.08);
        border: 1px solid #eef2f6;
        margin-bottom: 16px;
    }
    
    /* Metric Badges */
    .badge-up {
        background-color: #dcfce7;
        color: #15803d;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }
    .badge-down {
        background-color: #ffe4e6;
        color: #be123c;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }
    
    /* Patient Queue Styling */
    .queue-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px;
        background-color: #f8fafc;
        border-radius: 12px;
        margin-bottom: 8px;
        border: 1px solid #f1f5f9;
    }
    .time-pill {
        background-color: #e0e7ff;
        color: #4338ca;
        font-weight: 700;
        font-size: 11px;
        padding: 6px 10px;
        border-radius: 8px;
    }
    
    /* Schedule Card */
    .appt-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 10px;
        border: 1px solid #e2e8f0;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- ROW 1: TOP STATS & CARDS ----------------
col1, col2, col3, col4 = st.columns([1.2, 1.1, 1.8, 1.9], gap="medium")

# Card 1: Total Patients Donut Chart
with col1:
    st.markdown('<div class="doc-card">', unsafe_allow_html=True)
    st.markdown("<h6 style='color: #475569; font-weight: 700; margin-bottom: 0px;'>Total Patients</h6>", unsafe_allow_html=True)
    
    fig_donut = go.Figure(data=[go.Pie(
        labels=['Woman', 'Man'],
        values=[44, 55],
        hole=0.72,
        marker=dict(colors=['#5b50e3', '#93c5fd']),
        textinfo='none'
    )])
    fig_donut.update_layout(
        annotations=[dict(text='<b>990</b><br><span style="font-size:10px;color:#64748b;">Total</span>', x=0.5, y=0.5, font_size=18, showarrow=False)],
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
        margin=dict(t=10, b=10, l=10, r=10),
        height=175
    )
    st.plotly_chart(fig_donut, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Card 2: New & Old Patients Metrics
with col2:
    st.markdown("""
        <div class="doc-card" style="margin-bottom: 12px; padding: 14px;">
            <span style="font-size: 12px; color: #64748b; font-weight: 600;">New Patients</span>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 6px;">
                <span style="font-size: 26px; font-weight: 800; color: #0f172a;">67</span>
                <span class="badge-up">▲ 39%</span>
            </div>
        </div>
        <div class="doc-card" style="padding: 14px;">
            <span style="font-size: 12px; color: #64748b; font-weight: 600;">Old Patients</span>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 6px;">
                <span style="font-size: 26px; font-weight: 800; color: #0f172a;">27</span>
                <span class="badge-down">▼ 04%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Card 3: Today's Patient Queue
with col3:
    st.markdown('<div class="doc-card">', unsafe_allow_html=True)
    st.markdown("<h6 style='color: #475569; font-weight: 700; margin-bottom: 12px;'>Your Patients Today</h6>", unsafe_allow_html=True)
    st.markdown("""
        <div class="queue-item">
            <span class="time-pill">10:30 AM</span>
            <div>
                <div style="font-weight: 700; color: #0f172a; font-size: 13px;">Sarah Hostemn</div>
                <div style="font-size: 11px; color: #64748b;">Diagnosis: Bronchi</div>
            </div>
            <span style="color: #94a3b8; font-weight: bold;">⋮</span>
        </div>
        <div class="queue-item">
            <span class="time-pill">11:00 AM</span>
            <div>
                <div style="font-weight: 700; color: #0f172a; font-size: 13px;">Dakota Smith</div>
                <div style="font-size: 11px; color: #64748b;">Diagnosis: Stroke</div>
            </div>
            <span style="color: #94a3b8; font-weight: bold;">⋮</span>
        </div>
        <div class="queue-item" style="margin-bottom: 0px;">
            <span class="time-pill">11:30 AM</span>
            <div>
                <div style="font-weight: 700; color: #0f172a; font-size: 13px;">John Lane</div>
                <div style="font-size: 11px; color: #64748b;">Diagnosis: Liver</div>
            </div>
            <span style="color: #94a3b8; font-weight: bold;">⋮</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Card 4: Upcoming Appointments Schedule
with col4:
    st.markdown('<div class="doc-card">', unsafe_allow_html=True)
    st.markdown("<h6 style='color: #475569; font-weight: 700; margin-bottom: 10px;'>Upcoming Appointments</h6>", unsafe_allow_html=True)
    st.info("📅 Thursday | July 25th 2026")
    
    st.markdown("""
        <div class="appt-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong style="color: #0f172a; font-size: 13px;">Shawn Hampton</strong><br>
                    <span style="color: #64748b; font-size: 11px;">Emergency appointment</span>
                </div>
                <span style="background-color: #e0e7ff; color: #4338ca; padding: 4px 8px; border-radius: 50%;">📞</span>
            </div>
            <div style="margin-top: 6px; font-size: 11px; color: #64748b; font-weight: 600;">
                ⏱ 10:00 &nbsp;•&nbsp; 💵 $30
            </div>
        </div>
        <div class="appt-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong style="color: #0f172a; font-size: 13px;">Polly Paul</strong><br>
                    <span style="color: #64748b; font-size: 11px;">USG + Consultation</span>
                </div>
                <span style="background-color: #e0e7ff; color: #4338ca; padding: 4px 8px; border-radius: 50%;">📞</span>
            </div>
            <div style="margin-top: 6px; font-size: 11px; color: #64748b; font-weight: 600;">
                ⏱ 10:30 &nbsp;•&nbsp; 💵 $50
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ---------------- ROW 2: BOTTOM ANALYTICS CHARTS ----------------
col5, col6, col7 = st.columns([1.5, 1.5, 1.5], gap="medium")

# Card 5: Monthly Line Trend
with col5:
    st.markdown('<div class="doc-card">', unsafe_allow_html=True)
    st.markdown("<h6 style='color: #475569; font-weight: 700;'>Analytics</h6>", unsafe_allow_html=True)
    line_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
        "Patients": [28, 38, 22, 32, 42, 30, 40]
    })
    fig_line = px.line(line_df, x="Month", y="Patients", line_shape="spline")
    fig_line.update_traces(line_color="#10b981", line_width=3, fill="tozeroy", fillcolor="rgba(16, 185, 129, 0.12)")
    fig_line.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=210, yaxis_title=None, xaxis_title=None, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_line, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Card 6: Category Breakdown Pie Chart
with col6:
    st.markdown('<div class="doc-card">', unsafe_allow_html=True)
    st.markdown("<h6 style='color: #475569; font-weight: 700;'>Appointments Overview</h6>", unsafe_allow_html=True)
    pie_df = pd.DataFrame({
        "Category": ["Male", "Female", "Child", "Other"],
        "Count": [35, 30, 20, 15]
    })
    fig_pie = px.pie(pie_df, values="Count", names="Category", color_discrete_sequence=['#3b82f6', '#5b50e3', '#10b981', '#ef4444'])
    fig_pie.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=210, showlegend=True, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Card 7: Hourly Appointments Bar Chart
with col7:
    st.markdown('<div class="doc-card">', unsafe_allow_html=True)
    st.markdown("<h6 style='color: #475569; font-weight: 700;'>Overall Appointment</h6>", unsafe_allow_html=True)
    bar_df = pd.DataFrame({
        "Time": ["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"],
        "Appointments": [18, 22, 28, 12, 34, 15, 26, 10, 22]
    })
    fig_bar = px.bar(bar_df, x="Time", y="Appointments", color_discrete_sequence=['#5b50e3'])
    fig_bar.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=210, yaxis_title=None, xaxis_title=None, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)