import streamlit as st
import numpy as np
import pandas as pd
import streamlit_extras as st_extras
import streamlit_option_menu as st_option_menu
from streamlit_pandas_profiling import st_profile_report
import random
from faker import Faker


class Login:

    def __init__(self, pin) -> None:
        self.pin = pin

    def login():
        st.markdown(
            """<h2 style="text-align: center;"> Login</h2> """, unsafe_allow_html=True
        )
        with st.form("auth"):
            pin = st.text_input(
                label="Pin", max_chars=4, type="password", label_visibility="visible"
            )
            if st.form_submit_button(
                label="Login", type="primary", use_container_width=True
            ):
                if Login.auth(pin):
                    st.rerun()
                else:
                    st.warning(
                        body="Access denied, or pin number not assigned", icon="⛔"
                    )

            st.markdown(
                """<p style="text-align: center;"><span style="color: #999999;"><a style="color: #999999; text-decoration: underline;" title="ticket" href="mailto:ithelpdesk@amphenol-sensors.com?subject=Forgot NC Pin Number&amp;body=Hi, I forgot my pin for Non Conformance System">Forgot Pin</a></span></p>""",
                unsafe_allow_html=True,
            )
        pass

    def auth(pin):
        if pin == "9999":
            st.session_state.user = {
                "user": "Admin",
                "access": 0,
                "logged": True,
                "layout": "wide",
                "sidebar_state": "expanded",
            }
            return True


class Home:
    def view():
        header = st.empty()
        header.markdown(
            """
            <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            .middle-center {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100%;
                padding-bottom: 50px;
            }
            </style>
            <div class="middle-center">
                <h1>Welcome to Porta del Sol Memorial</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns(2)
        with col1:
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data)
        with col2:
            df = pd.read_csv(
                "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
            )
            st.dataframe(df)

    pass


class Client:
    def view():
        header = st.empty()
        header.markdown(
            """
            <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            .middle-center {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100%;
                padding-bottom: 50px;
            }
            </style>
            <div class="middle-center">
                <h1>Porta del Sol</h1>
                <h2>Client Management</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        container = st.container()
        with container:
            st.markdown(
                """
                <style>
                .stButton > button {
                margin-top:30px; 
                float:right;               
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
            col1, col2 = st.columns(2)
            with col1:
                search = st.text_input(label="Search", placeholder="Search")
            with col2:
                add_btn = st.button(label="Add", type="primary")
        fake = Faker()
        data = {
            "Nombre": [fake.name() for _ in range(50)],
            "Dirección": [fake.address() for _ in range(50)],
            "Teléfono": [fake.phone_number() for _ in range(50)],
            "Email": [fake.email() for _ in range(50)],
            "Fecha de visita/orientación": [
                fake.date_between(start_date="-1y", end_date="today") for _ in range(50)
            ],
            "Servicio solicitado": [
                fake.random_element(
                    elements=("Consultoría", "Asesoramiento", "Soporte técnico")
                )
                for _ in range(50)
            ],
            "Detalle de los servicios cotizados": [
                fake.sentence(nb_words=6) for _ in range(50)
            ],
            "Precio cotizado": [round(random.uniform(100, 1000), 2) for _ in range(50)],
        }

        # Create DataFrame
        df = pd.DataFrame(data)

        # Display DataFrame in Streamlit
        st.dataframe(df)


class Employee:
    def view():
        header = st.empty()
        header.markdown(
            """
            <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            .middle-center {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100%;
                padding-bottom: 50px;
            }
            </style>
            <div class="middle-center">
                <h1>Porta del Sol</h1>
                <h2>Employee Management</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        container = st.container()
        with container:
            st.markdown(
                """
                <style>
                .stButton > button {
                margin-top:30px; 
                float:right;               
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
            col1, col2 = st.columns(2)
            with col1:
                search = st.text_input(label="Search", placeholder="Search")
            with col2:
                add_btn = st.button(label="Add", type="primary")
        fake = Faker()

        data = {
            "first_name": [fake.first_name() for _ in range(50)],
            "last_name": [fake.last_name() for _ in range(50)],
            "address": [fake.address().replace("\n", ", ") for _ in range(50)],
            "phone": [fake.phone_number() for _ in range(50)],
            "email": [fake.email() for _ in range(50)],
            "username": [fake.user_name() for _ in range(50)],
            "password": [fake.password() for _ in range(50)],
            "start_date": [
                fake.date_between(start_date="-1y", end_date="today") for _ in range(50)
            ],
            "end_date": [
                fake.date_between(start_date="today", end_date="+1y") for _ in range(50)
            ],
            "active": [random.choice([True, False]) for _ in range(50)],
        }

        df = pd.DataFrame(data)

        st.dataframe(df)
        pass


class Profile:
    def view():
        with st.form(key="profile"):
            st.text_input("First Name")
            st.text_input("Last Name")
            st.text_input("Address")
            st.text_input("Phone")
            st.text_input("Email")
            st.text_input("Username")
            st.text_input("Password")
            st.date_input("Start Date")
            st.date_input("End Date")
            st.checkbox("Active")
            st.form_submit_button("Submit")
            pass

        # pass