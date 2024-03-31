import streamlit as st
import pandas as pd
import random
from faker import Faker

select_employees =""""""
select_employee=""""""
insert_employee=""""""
edit_employee=""""""
delete_employee=""""""

class Employees:
    @staticmethod
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
                <h2>Empleados</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, col2 = st.columns(2)
        with col1:
            search = st.text_input(label="Buscar", placeholder="Buscar")
        with col2:
            with st.container():
                st.markdown(
                    """
                    <style>
                        .st-emotion-cache-1i4zmrw{
                            float:right;
                            margin-top: 13px;
                            }
                    </style>

                    """,
                    unsafe_allow_html=True,
                )
            with st.popover(label="Más+"):
            # if more_btn_session_state.get('more_opitions', False):
                tab1, tab2, tab3 = st.tabs(["Añadir", "Editar", "Borrar"])

                with tab1:Employees.add_employee_form()
                with tab2:Employees.edit_employee_form()
                with tab3:Employees.delete_employee_form()

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

    def add_employee_form():pass
    def edit_employee_form():pass
    def delete_employee_form():pass