import streamlit as st
import numpy as np
import pandas as pd
import streamlit_extras as st_extras
import streamlit_option_menu as st_option_menu
from streamlit_pandas_profiling import st_profile_report
import random
import datetime
from faker import Faker


class Login:

    def __init__(self, pin) -> None:
        self.pin = pin

    def login():
        st.markdown(
            """<h2 style="text-align: center;"> Iniciar sesión</h2> """, unsafe_allow_html=True
        )
        with st.form("auth"):
            pin = st.text_input(
                label="Pin", max_chars=4, type="password", label_visibility="visible"
            )
            if st.form_submit_button(
                label="Iniciar sesión", type="primary", use_container_width=True
            ):
                if Login.auth(pin):
                    st.rerun()
                else:
                    st.warning(
                        body="Acceso denegado", icon="⛔"
                    )

            st.markdown(
                """<p style="text-align: center;"><span style="color: #999999;"><a style="color: #999999; text-decoration: underline;" title="Recuperación de contraseña" href="mailto:?subject=Contraseña&amp;body=Hola, he olvidado mi contraseña">¿Olvidaste tu contraseña?</a></span></p>""",
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
            st.session_state.user["layout"] = "wide"
            st.session_state.user["sidebar_state"] = "expanded"
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
                <h1>Bienvenidos a Porta del Sol Memorial</h1>
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

class Services:
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
                <h2>Servicios</h2>
            </div>
            """
        st.markdown(header, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            search = st.text_input(label="Buscar", placeholder="Buscar")
        with col2:
            with st.container():
                st.markdown(
                    """
                    <style>
                    .stButton > button {
                    margin-top:10px; 
                    float:right;               
                    }
                    </style>

                    """,
                    unsafe_allow_html=True,
                )          
                if st.button(label="Más +", type="primary"): pass
                    # more_btn_session_state['more_opitions'] = not more_btn_session_state.get('more_opitions', False)
        # Crear el DataFrame con los datos de los servicios
        datos_servicios = {
            'Servicio': ['Cremación', 'Entierro tradicional', 'Funeral religioso', 'Servicio de urna', 'Pre-arreglos funerarios'],
            'Disponibilidad': ['Ofrecido', 'Ofrecido', 'Ofrecido', 'Por ofrecer', 'Por ofrecer'],
            'Precio': ['$1000', '$2000', '$1500', 'N/A', 'N/A'],
            'Duración': ['2 horas', '4 horas', '3 horas', 'N/A', 'N/A'],
            'Incluye': ['Urna básica', 'Ataúd, sala de velatorio', 'Servicio religioso', 'N/A', 'N/A']
        }

        # Replicar los datos 50 veces
        datos_repetidos = {k: v * 50 for k, v in datos_servicios.items()}

        # Crear el DataFrame con los datos repetidos
        df_servicios = pd.DataFrame(datos_repetidos)

        # Mostrar el DataFrame en Streamlit
        st.title('Servicios de la Funeraria')
        st.dataframe(df_servicios)

        
class Client:
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
                    margin-top:10px; 
                    float:right;               
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
                Client.add_client_form()

            with tab2:
                Client.edit_client_form()

            with tab3:
                Client.delete_client_form()

        
        
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
        Client.display_client_form(Client.find_client(), False)


    @staticmethod
    def display_client_form(client, disabled):
        if disabled: key = "delete_client"
        else: key = "edit_client"
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
        return Client('Michael', 'Santiago', '939-287-3001', 'mickey@disney.com', '123 Main St', datetime.date(2022, 5, 16), 'Funeral', 'Capybaras', 1500)

    @staticmethod
    def delete_client_form():
        search = st.text_input(label="Buscar")
        if search is not None:
            Client.display_client_form(Client.find_client(),True)

class Employee:
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
                    .stButton > button {
                    margin-top:10px; 
                    float:right;               
                    }
                    </style>

                    """,
                    unsafe_allow_html=True,
                )          
                if st.button(label="Más +", type="primary"): pass
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
                <h2>Perfil</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.container():
            st.markdown(
                """
                <style>
                .stButton > button {
                    display: block;
                    margin: 20px auto;        
                }
                .st-emotion-cache-r421ms {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px);
                    width: 70%;
                    margin: 0 auto; /* Center horizontally */
                }

                </style>
                """,
                unsafe_allow_html=True,
            )
            with st.form(key="profile", clear_on_submit=True):
                col1,col2 = st.columns(2)
                with col1:
                    first_name = st.text_input(label="Nombre")
                    email = st.text_input(label="Correo")

                with col2:
                    last_name = st.text_input(label="Apellidos")
                    phone = st.text_input(label="Telefono")
  
                address = st.text_input(label="Dirección")
                col1,col2 = st.columns(2)
                with col1:
                    username = st.text_input(label="Usuario")
                    start_date = st.date_input(label="Fecha de comienzo")
                with col2:
                    password = st.text_input(label="Contraseña",type="password")
                    end_date = st.date_input(label="End Date")
                st.form_submit_button(label="Submit",type="primary")
                pass

            # pass
