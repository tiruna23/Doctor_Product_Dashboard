import streamlit as st


# =====================================================
# COMMON PAGE STYLE
# =====================================================

def apply_page_style():

    st.markdown(
        """
        <style>

        /* =================================================
           GLOBAL APP
           ================================================= */

        .stApp {
            background: #f4f8fc;
        }


        /* =================================================
           HIDE STREAMLIT DEFAULT NAVIGATION
           ================================================= */

        section[data-testid="stSidebar"]
        div[data-testid="stSidebarNav"] {
            display: none !important;
        }

        div[data-testid="stSidebarNav"] {
            display: none !important;
        }


        /* =================================================
           HIDE STREAMLIT DEFAULT HEADER
           ================================================= */

        [data-testid="stHeader"] {
            background: transparent;
        }


        /* =================================================
           MAIN CONTENT
           ================================================= */

        .main .block-container {

            max-width: 1500px;

            padding-top: 30px;
            padding-bottom: 40px;
            padding-left: 38px;
            padding-right: 38px;

        }


        /* =================================================
           GENERAL TYPOGRAPHY
           ================================================= */

        html,
        body,
        [class*="css"] {

            font-family:
                Arial,
                Helvetica,
                sans-serif;

        }


        /* =================================================
           BUTTONS
           ================================================= */

        .stButton > button {

            border-radius: 9px;

            font-weight: 600;

            min-height: 40px;

        }


        /* =================================================
           REMOVE DEFAULT FOOTER
           ================================================= */

        footer {
            visibility: hidden;
        }


        /* =================================================
           HIDE MAIN MENU
           ================================================= */

        #MainMenu {
            visibility: hidden;
        }


        /* =================================================
           RESPONSIVE
           ================================================= */

        @media (max-width: 900px) {

            .main .block-container {

                padding-left: 18px;
                padding-right: 18px;

            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )