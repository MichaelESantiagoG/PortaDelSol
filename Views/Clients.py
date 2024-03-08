import streamlit as st
import pandas as pd
import random
import datetime
from faker import Faker
        
class Clients:
    clients = set()

    def __init__(self, first_name, last_name, phone, email, address, visit_date, service, details, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        self.visit_date = visit_date
        self.service = service
        self.details = details
        self.price = balance
        
    @staticmethod
    def view():
        header = """
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
                <h2>Clientes</h2>
            </div>
            """
        st.markdown(header, unsafe_allow_html=True)

        more_btn_session_state = st.session_state.setdefault('more_opitions', {})
        col1, col2 = st.columns(2)
        with col1:
            search = st.text_input(label="Buscar", placeholder="Buscar")
        with col2:
            with st.container():
                st.markdown(
                    """
                    <style>
                        .stButton > button {
                            float:right;               
                        }
                        .row-widget {
                            margin-top:auto; 
                            float:left;               
                        }
                    </style>

                    """,
                    unsafe_allow_html=True,
                )          
                if st.button(label="Más +", type="primary"): 
                    more_btn_session_state['more_opitions'] = not more_btn_session_state.get('more_opitions', False)

        if more_btn_session_state.get('more_opitions', False):
            tab1, tab2, tab3 = st.tabs(["Añadir", "Editar", "Borrar"])

            with tab1:
                Clients.add_client_form()

            with tab2:
                Clients.edit_client_form()

            with tab3:
                Clients.delete_client_form()

        
        
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
        st.dataframe(pd.DataFrame(data))

    @staticmethod
    def add_client_form():
        with st.form(key="add_client", clear_on_submit=False):
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input(label="Nombre")
                phone = st.text_input(label="Telefono")
                address = st.text_input(label="Dirección")
                visit_date = st.date_input(label="Fecha de Orientación")
            with col2:
                last_name = st.text_input(label="Apellidos")
                email = st.text_input(label="Correo")
                service = st.text_input(label="Servicio solicitado")
                details = st.text_input(label="Detalles de cotización")
                price = st.number_input(label="Precio cotizado")

            if st.form_submit_button(label="Actualizar", type="secondary", use_container_width=True):
                client_updated_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone': phone,
                    'email': email,
                    'address': address,
                    'visit_date': visit_date.strftime("%Y-%m-%d"),
                    'service': service,
                    'details': details,
                    'price': price
                }
                st.success("Cliente añadido.")


    @staticmethod
    def edit_client_form():
        Clients.display_client_form(Clients.find_client(), False)


    @staticmethod
    def display_client_form(client, disabled):
        if disabled: key = "delete_client"
        else: key = "edit_client"
        search = st.text_input(label="Buscar", placeholder="Buscar", key=key)
        with st.form(key=key, clear_on_submit=False):
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input(label="Nombre", value=client.first_name, disabled=disabled)
                phone = st.text_input(label="Telefono", value=client.phone, disabled=disabled)
                address = st.text_input(label="Dirección", value=client.address, disabled=disabled)
                visit_date = st.date_input(label="Fecha de Orientación", value=client.visit_date, disabled=disabled)
            with col2:
                last_name = st.text_input(label="Apellidos", value=client.last_name, disabled=disabled)
                email = st.text_input(label="Correo", value=client.email, disabled=disabled)
                service = st.text_input(label="Servicio solicitado", value=client.service, disabled=disabled)
                details = st.text_input(label="Detalles de cotización", value=client.details, disabled=disabled)
                price = st.number_input(label="Precio cotizado", value=client.price, disabled=disabled)

            if disabled: label = "Eliminar"
            else:  label = "Actualizar"
            if st.form_submit_button(label=label, type="secondary", use_container_width=True):
                client_updated_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone': phone,
                    'email': email,
                    'address': address,
                    'visit_date': visit_date.strftime("%Y-%m-%d"),
                    'service': service,
                    'details': details,
                    'price': price
                }
                st.success("Informacion del cliente actualizada.")

    @staticmethod
    def find_client():
        # Here you would retrieve the existing client information from the database based on the provided ID
        # For now, returning a hardcoded client
        return Clients('Michael', 'Santiago', '939-287-3001', 'mickey@disney.com', '123 Main St', datetime.date(2022, 5, 16), 'Funeral', 'Capybaras', 1500)

    @staticmethod
    def delete_client_form():
        Clients.display_client_form(Clients.find_client(),True)

