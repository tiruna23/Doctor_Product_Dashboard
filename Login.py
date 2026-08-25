import streamlit as st

# Custom Styling for Clean Professional Look
st.markdown(
    """
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .stApp {
            background-color: #f1f5f9;
        }

        /* Modern Card Styling */
        [data-testid="stForm"] {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 2.2rem 2rem;
            box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.1), 0 8px 10px -6px rgba(15, 23, 42, 0.04);
            border: 1px solid #e2e8f0;
        }

        /* Primary Button Adjustments */
        div[data-testid="stForm"] button[kind="primary"] {
            background-color: #2563eb !important;
            border-color: #2563eb !important;
            color: #ffffff !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            height: 44px !important;
            margin-top: 10px !important;
        }

        div[data-testid="stForm"] button[kind="primary"]:hover {
            background-color: #1d4ed8 !important;
        }

        label {
            color: #334155 !important;
            font-size: 13px !important;
            font-weight: 600 !important;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Centering container using Streamlit Columns (Fixes Wide Layout)
col1, col2, col3 = st.columns([1, 1.1, 1])

with col2:
  st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

  # Premium Medical Shield Icon Header
  st.markdown(
      """
        <div style="text-align: center; margin-bottom: 24px;">
            <div style="display: inline-flex; align-items: center; justify-content: center; width: 56px; height: 56px; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); border-radius: 14px; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); margin-bottom: 12px;">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                    <path d="M12 8v8"></path>
                    <path d="M8 12h8"></path>
                </svg>
            </div>
            <h2 style="color: #0f172a; margin: 0; font-size: 24px; font-weight: 700; letter-spacing: -0.5px;">MediCare</h2>
            <p style="color: #64748b; font-size: 13px; margin-top: 4px;">Hospital Management Portal</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # Compact Login Form
  with st.form("login_form", clear_on_submit=False):
    st.markdown(
        '<h4 style="color: #1e293b; margin-top:0; margin-bottom: 20px;'
        ' font-size: 16px; font-weight: 600; text-align: center;">Sign in to'
        " your account</h4>",
        unsafe_allow_html=True,
    )

    username = st.text_input(
        "Username", placeholder="Enter username", key="login_username"
    )
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password",
        key="login_password",
    )

    submit = st.form_submit_button(
        "Sign In", type="primary", use_container_width=True
    )

    if submit:
      if username.strip() != "" and password.strip() != "":
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.rerun()
      else:
        st.error("Please enter both username and password.")

  # Minimal Footer
  st.markdown(
      """
        <div style="text-align: center; margin-top: 24px;">
            <p style="color: #94a3b8; font-size: 11px;">© 2026 MediCare Inc. All rights reserved.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )