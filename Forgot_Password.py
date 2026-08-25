import streamlit as st

from models.auth_model import (
    user_exists_by_email,
    reset_password
)


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Forgot Password | MediCare",
    page_icon="🔑",
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

    .forgot-title {
        text-align: center;
        color: #172033;
        font-size: 32px;
        font-weight: 700;
    }

    .forgot-caption {
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
    <div class="forgot-title">
        🏥 MediCare
    </div>

    <div class="forgot-caption">
        Reset your account password
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================================
# FORGOT PASSWORD FORM
# =====================================================

with st.container(border=True):

    st.subheader("🔑 Forgot Password")

    email = st.text_input(
        "Registered Email",
        placeholder="Enter your registered email",
        key="forgot_email"
    )

    new_password = st.text_input(
        "New Password",
        type="password",
        placeholder="Enter new password",
        key="forgot_new_password"
    )

    confirm_password = st.text_input(
        "Confirm New Password",
        type="password",
        placeholder="Re-enter new password",
        key="forgot_confirm_password"
    )

    st.write("")


    # =================================================
    # RESET PASSWORD BUTTON
    # =================================================

    if st.button(
        "🔑 Reset Password",
        type="primary",
        use_container_width=True,
        key="reset_password_button"
    ):

        if email.strip() == "":

            st.error(
                "Please enter your registered email."
            )

        elif new_password == "":

            st.error(
                "Please enter a new password."
            )

        elif confirm_password == "":

            st.error(
                "Please confirm your new password."
            )

        elif new_password != confirm_password:

            st.error(
                "Passwords do not match."
            )

        elif len(new_password) < 6:

            st.error(
                "Password must contain at least 6 characters."
            )

        else:

            # -----------------------------------------
            # CHECK EMAIL
            # -----------------------------------------

            email_exists = user_exists_by_email(
                email.strip()
            )


            if not email_exists:

                st.error(
                    "No account found with this email."
                )

            else:

                # -------------------------------------
                # RESET PASSWORD
                # -------------------------------------

                result = reset_password(
                    email.strip(),
                    new_password
                )


                if result:

                    st.success(
                        "Password reset successfully!"
                    )

                    st.info(
                        "You can now login using your new password."
                    )

                else:

                    st.error(
                        "Unable to reset password."
                    )


# =====================================================
# LOGIN LINK
# =====================================================

st.write("")


st.page_link(
    "pages/Login.py",
    label="🔐 Back to Login"
)


# =====================================================
# REGISTER LINK
# =====================================================

st.write("")


st.page_link(
    "pages/Register.py",
    label="📝 Create New Account"
)