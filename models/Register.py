import streamlit as st

from models.auth_model import register_user


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Register | MediCare",
    page_icon="📝",
    layout="centered"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f8fc;
    }

    .register-box {
        background-color: white;
        padding: 35px;
        border-radius: 18px;
        border: 1px solid #e1e7ed;
        box-shadow: 0 4px 18px rgba(0,0,0,0.06);
    }

    .register-title {
        text-align: center;
        color: #172033;
        font-size: 32px;
        font-weight: 700;
    }

    .register-caption {
        text-align: center;
        color: #687386;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <div class="register-title">
        🏥 MediCare
    </div>

    <div class="register-caption">
        Create your account
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================================
# REGISTER FORM
# =====================================================

with st.container(border=True):

    st.subheader("📝 Register")

    username = st.text_input(
        "Username",
        placeholder="Enter username",
        key="register_username"
    )

    email = st.text_input(
        "Email",
        placeholder="Enter email address",
        key="register_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password",
        key="register_password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        placeholder="Re-enter password",
        key="register_confirm_password"
    )


    st.write("")


    # =================================================
    # REGISTER BUTTON
    # =================================================

    if st.button(
        "📝 Create Account",
        type="primary",
        use_container_width=True,
        key="register_button"
    ):

        if username.strip() == "":

            st.error(
                "Please enter username."
            )

        elif email.strip() == "":

            st.error(
                "Please enter email."
            )

        elif password == "":

            st.error(
                "Please enter password."
            )

        elif confirm_password == "":

            st.error(
                "Please confirm your password."
            )

        elif password != confirm_password:

            st.error(
                "Passwords do not match."
            )

        elif len(password) < 6:

            st.error(
                "Password must contain at least 6 characters."
            )

        else:

            result = register_user(
                username.strip(),
                email.strip(),
                password
            )

            if result:

                st.success(
                    "Account created successfully!"
                )

                st.info(
                    "You can now login to MediCare."
                )

            else:

                st.error(
                    "Username or email already exists."
                )


# =====================================================
# LOGIN LINK
# =====================================================

st.write("")


st.page_link(
    "pages/Login.py",
    label="Already have an account? Login"
)