import streamlit as st
<<<<<<< HEAD
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
=======
import datetime
from datetime import datetime
from modules import conn


class Clients:

    @staticmethod
    def view():
        header = st.empty()
        header.markdown(
            """
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
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
<<<<<<< HEAD
=======
            .st-fq {
                width: 500px;
            }
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
            </style>
            <div class="middle-center">
                <h1>Porta del Sol</h1>
                <h2>Clientes</h2>
            </div>
<<<<<<< HEAD
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

=======
            """,
            unsafe_allow_html=True,
        )
        with st.container():
            st.markdown(
                """
                <style>
                    .st-emotion-cache-9snfwb{
                        float:right;
                        margin-top: 13px;
                        }
                </style>

                """,
                unsafe_allow_html=True,
            )
            with st.popover(
                label="Más+",
                use_container_width=False,
            ):
                tab1, tab2, tab3 = st.tabs(["Añadir", "Editar", "Borrar"])

                with tab1:
                    Clients.add_client_form()
                with tab2:
                    Clients.edit_client_form()
                with tab3:
                    Clients.delete_client_form()

        st.write("***")
        # st.dataframe(conn.Connections.query1(select_clients))
        st.dataframe(conn.Select_All.CLientes(), hide_index=True)

    def add_client_form():
        key, disabled = "add_client", False
        with st.form(key=key, clear_on_submit=False, border=False):
            col1, col2 = st.columns(2)
            with col1:
                Nombre = st.text_input(
                    key=key + "Nombre",
                    label="Nombre",
                    disabled=disabled,
                )
                Apellido_Paterno = st.text_input(
                    key=key + "Apellido_Paterno",
                    label="Apellido Paterno",
                    disabled=disabled,
                )
                Apellido_Materno = st.text_input(
                    key=key + "Apellido_Materno",
                    label="Apellido Materno",
                    disabled=disabled,
                )
                Correo_Electronico = st.text_input(
                    key=key + "Correo_Electronico",
                    label="Correo Electronico",
                    disabled=disabled,
                )
                Celular = st.text_input(
                    key=key + "Celular",
                    label="Celular",
                    disabled=disabled,
                )
                Celular_2 = st.text_input(
                    key=key + "Celular_2",
                    label="Celular 2",
                    disabled=disabled,
                )

                Direccion = st.text_input(
                    key=key + "Direccion",
                    label="Dirección",
                    disabled=disabled,
                )
                Estado_Civil = st.selectbox(
                    key=key + "Estado_Civil",
                    label="Estado Civil",
                    disabled=disabled,
                    options=["Soltero", "Casado", "Divorciado", "Viudo"],
                )
            with col2:
                Ocupacion = st.text_input(
                    key=key + "Ocupacion",
                    label="Ocupacion",
                    disabled=disabled,
                )
                Descripcion = st.text_input(
                    key=key + "Descripcion", label="Descripcion", disabled=disabled
                )
                Seguro_Social = st.text_input(
                    key=key + "Seguro_Social",
                    label="Seguro Social",
                    disabled=disabled,
                )
                Genero = st.selectbox(
                    key=key + "Genero",
                    label="Género",
                    options=["Masculino", "Femenino"],
                    disabled=disabled,
                )
                Fecha_Nacimiento = st.date_input(
                    key=key + "Fecha_Nacimiento",
                    label="Fecha de Nacimiento",
                    min_value=None,
                    max_value=None,
                    disabled=disabled,
                ).strftime("%Y-%m-%d")

                Lugar_Nacimiento = st.text_input(
                    key=key + "Lugar_Nacimiento,",
                    label="Lugar de Nacimiento",
                    disabled=disabled,
                )
                Licencia = st.text_input(
                    key=key + "Licencia",
                    label="Licencia",
                    disabled=disabled,
                )

                Servicio_Militar = st.text_input(
                    key=key + "Servicio_Militar",
                    label="Número de Servicio Militar",
                    disabled=disabled,
                )

            if st.form_submit_button(
                label="Añadir", type="secondary", use_container_width=True
            ):
                try:
                    Cliente = {
                        "Ocupacion": Ocupacion,
                        "Nombre": Nombre,
                        "Apellido_Paterno": Apellido_Paterno,
                        "Apellido_Materno": Apellido_Materno,
                        "Genero": Genero,
                        "Correo_Electronico": Correo_Electronico,
                        "Celular": Celular,
                        "Celular_2": Celular_2,
                        "Direccion": Direccion,
                        "Fecha_Nacimiento": Fecha_Nacimiento,
                        "Lugar_Nacimiento": Lugar_Nacimiento,
                        "Seguro_Social": Seguro_Social,
                        "Licencia": Licencia,
                        "Servicio_Militar": Servicio_Militar,
                        "Estado_Civil": Estado_Civil,
                        "Descripcion": Descripcion,
                    }
                    conn.Insert.Cliente(Cliente)
                    st.success("Cliente añadido")

                except:
                    st.warning("Cliente NO se pudo añadir")

    def edit_client_form():
        key, disabled = "update_client", False
        search_id = st.number_input(
            key=key + "search_id", label="ID de Cliente", min_value=0, step=1
        )
        client_info = Clients.select_client(search_id)
        if client_info:
            with st.form(key=key + "form", clear_on_submit=False, border=False):
                col1, col2 = st.columns(2)
                with col1:
                    Nombre = st.text_input(
                        key=key + "Nombre",
                        label="Nombre",
                        disabled=disabled,
                        value=client_info["Nombre"],
                    )
                    Apellido_Paterno = st.text_input(
                        key=key + "Apellido_Paterno",
                        label="Apellido Paterno",
                        disabled=disabled,
                        value=client_info["Apellido_Paterno"],
                    )
                    Apellido_Materno = st.text_input(
                        key=key + "Apellido_Materno",
                        label="Apellido Materno",
                        disabled=disabled,
                        value=client_info["Apellido_Materno"],
                    )
                    Correo_Electronico = st.text_input(
                        key=key + "Correo_Electronico",
                        label="Correo Electronico",
                        disabled=disabled,
                        value=client_info["Correo_Electronico"],
                    )
                    Celular = st.text_input(
                        key=key + "Celular",
                        label="Celular",
                        disabled=disabled,
                        value=client_info["Celular"],
                    )
                    Celular_2 = st.text_input(
                        key=key + "Celular_2",
                        label="Celular 2",
                        disabled=disabled,
                        value=client_info["Celular_2"],
                    )

                    Direccion = st.text_input(
                        key=key + "Direccion",
                        label="Dirección",
                        disabled=disabled,
                        value=client_info["Direccion"],
                    )
                    # Define the options
                    options = ["Soltero", "Casado", "Divorciado", "Viudo"]

                    # Set the default index to None initially
                    default_index = None

                    # Check if the value from client_info["Estado_Civil"] matches any option
                    if client_info["Estado_Civil"] in options:
                        default_index = options.index(client_info["Estado_Civil"])

                    # Create the select box with the correct default index
                    Estado_Civil = st.selectbox(
                        key=key + "Estado_Civil",
                        label="Estado Civil",
                        disabled=disabled,
                        options=options,
                        index=default_index,
                    )
                with col2:
                    Ocupacion = st.text_input(
                        key=key + "Ocupacion",
                        label="Ocupacion",
                        disabled=disabled,
                        value=client_info["Ocupacion"],
                    )
                    Descripcion = st.text_input(
                        key=key + "Descripcion",
                        label="Descripcion",
                        disabled=disabled,
                        value=client_info["Descripcion"],
                    )
                    Seguro_Social = st.text_input(
                        key=key + "Seguro_Social",
                        label="Seguro Social",
                        disabled=disabled,
                        value=client_info["Seguro_Social"],
                    )
                    Genero = st.selectbox(
                        key=key + "Genero",
                        label="Género",
                        options=["Masculino", "Femenino"],
                        disabled=disabled,
                        index=0 if client_info["Genero"] == "Activo" else 1,
                    )
                    date_obj = datetime.strptime(
                        client_info["Fecha_Nacimiento"], "%Y-%m-%d"
                    ).date()
                    Fecha_Nacimiento = st.date_input(
                        key=key + "Fecha_Nacimiento",
                        label="Fecha de Nacimiento",
                        value=date_obj,
                        min_value=None,
                        max_value=None,
                        disabled=disabled,
                    )

                    Lugar_Nacimiento = st.text_input(
                        key=key + "Lugar_Nacimiento,",
                        label="Lugar de Nacimiento",
                        disabled=disabled,
                        value=client_info["Lugar_Nacimiento"],
                    )
                    Licencia = st.text_input(
                        key=key + "Licencia",
                        label="Licencia",
                        disabled=disabled,
                        value=client_info["Licencia"],
                    )

                    Servicio_Militar = st.text_input(
                        key=key + "Servicio_Militar",
                        label="Número de Servicio Militar",
                        disabled=disabled,
                        value=client_info["Servicio_Militar"],
                    )

                if st.form_submit_button(
                    label="Actualizar",
                    disabled=disabled,
                    use_container_width=True,
                ):
                    try:
                        Cliente = {
                            "Ocupacion": Ocupacion,
                            "Nombre": Nombre,
                            "Apellido_Paterno": Apellido_Paterno,
                            "Apellido_Materno": Apellido_Materno,
                            "Genero": Genero,
                            "Correo_Electronico": Correo_Electronico,
                            "Celular": Celular,
                            "Celular_2": Celular_2,
                            "Direccion": Direccion,
                            "Fecha_Nacimiento": Fecha_Nacimiento,
                            "Lugar_Nacimiento": Lugar_Nacimiento,
                            "Seguro_Social": Seguro_Social,
                            "Licencia": Licencia,
                            "Servicio_Militar": Servicio_Militar,
                            "Estado_Civil": Estado_Civil,
                            "Descripcion": Descripcion,
                        }
                        conn.Update.Cliente(search_id, Cliente)
                        st.success("Cliente actualizado")
                    except:
                        st.warning("No se pudo actualizar el cliente")
        else:
            st.warning("Cliente no existe")

    def delete_client_form():
        key, disabled = "delete_client", True
        search_id = st.number_input(
            key=key + "search_id", label="ID de Cliente", min_value=0, step=1
        )
        client_info = Clients.select_client(search_id)
        if client_info:
            with st.form(key=key + "form", clear_on_submit=True, border=False):
                col1, col2 = st.columns(2)
                with col1:
                    Nombre = st.text_input(
                        key=key + "Nombre",
                        label="Nombre",
                        disabled=disabled,
                        value=client_info["Nombre"],
                    )
                    Apellido_Paterno = st.text_input(
                        key=key + "Apellido_Paterno",
                        label="Apellido Paterno",
                        disabled=disabled,
                        value=client_info["Apellido_Paterno"],
                    )
                    Apellido_Materno = st.text_input(
                        key=key + "Apellido_Materno",
                        label="Apellido Materno",
                        disabled=disabled,
                        value=client_info["Apellido_Materno"],
                    )
                    Correo_Electronico = st.text_input(
                        key=key + "Correo_Electronico",
                        label="Correo Electronico",
                        disabled=disabled,
                        value=client_info["Correo_Electronico"],
                    )
                    Celular = st.text_input(
                        key=key + "Celular",
                        label="Celular",
                        disabled=disabled,
                        value=client_info["Celular"],
                    )
                    Celular_2 = st.text_input(
                        key=key + "Celular_2",
                        label="Celular 2",
                        disabled=disabled,
                        value=client_info["Celular_2"],
                    )

                    Direccion = st.text_input(
                        key=key + "Direccion",
                        label="Dirección",
                        disabled=disabled,
                        value=client_info["Direccion"],
                    )
                    # Define the options
                    options = ["Soltero", "Casado", "Divorciado", "Viudo"]

                    # Set the default index to None initially
                    default_index = None

                    # Check if the value from client_info["Estado_Civil"] matches any option
                    if client_info["Estado_Civil"] in options:
                        default_index = options.index(client_info["Estado_Civil"])

                    # Create the select box with the correct default index
                    Estado_Civil = st.selectbox(
                        key=key + "Estado_Civil",
                        label="Estado Civil",
                        disabled=disabled,
                        options=options,
                        index=default_index,
                    )
                with col2:
                    Ocupacion = st.text_input(
                        key=key + "Ocupacion",
                        label="Ocupacion",
                        disabled=disabled,
                        value=client_info["Ocupacion"],
                    )
                    Descripcion = st.text_input(
                        key=key + "Descripcion",
                        label="Descripcion",
                        disabled=disabled,
                        value=client_info["Descripcion"],
                    )
                    Seguro_Social = st.text_input(
                        key=key + "Seguro_Social",
                        label="Seguro Social",
                        disabled=disabled,
                        value=client_info["Seguro_Social"],
                    )
                    Genero = st.selectbox(
                        key=key + "Genero",
                        label="Género",
                        options=["Masculino", "Femenino"],
                        disabled=disabled,
                        index=0 if client_info["Genero"] == "Activo" else 1,
                    )
                    date_obj = datetime.strptime(
                        client_info["Fecha_Nacimiento"], "%Y-%m-%d"
                    ).date()
                    Fecha_Nacimiento = st.date_input(
                        key=key + "Fecha_Nacimiento",
                        label="Fecha de Nacimiento",
                        value=date_obj,
                        min_value=None,
                        max_value=None,
                        disabled=disabled,
                    )

                    Lugar_Nacimiento = st.text_input(
                        key=key + "Lugar_Nacimiento,",
                        label="Lugar de Nacimiento",
                        disabled=disabled,
                        value=client_info["Lugar_Nacimiento"],
                    )
                    Licencia = st.text_input(
                        key=key + "Licencia",
                        label="Licencia",
                        disabled=disabled,
                        value=client_info["Licencia"],
                    )

                    Servicio_Militar = st.text_input(
                        key=key + "Servicio_Militar",
                        label="Número de Servicio Militar",
                        disabled=disabled,
                        value=client_info["Servicio_Militar"],
                    )

                if st.form_submit_button(
                    label="Eliminar", disabled=False, use_container_width=True
                ):
                    try:
                        conn.Delete.Cliente(search_id)
                        st.success("Cliente Eliminado")
                    except:
                        st.warning("No se pudo eliminar el cliente")
        else:
            st.warning("Cliente no existe")

    def select_client(search_id):
        try:
            # client = conn.Connections.query1(select_client.format(search_id))
            client = conn.Select.CLiente(search_id)
            client_info = {
                "Ocupacion": client["Ocupacion"],
                "Nombre": client["Nombre"],
                "Apellido_Paterno": client["Apellido_Paterno"],
                "Apellido_Materno": client["Apellido_Materno"],
                "Genero": client["Genero"],
                "Correo_Electronico": client["Correo_Electronico"],
                "Celular": client["Celular"],
                "Celular_2": client["Celular_2"],
                "Direccion": client["Direccion"],
                "Fecha_Nacimiento": client["Fecha_Nacimiento"],
                "Lugar_Nacimiento": client["Lugar_Nacimiento"],
                "Seguro_Social": client["Seguro_Social"],
                "Licencia": client["Licencia"],
                "Servicio_Militar": client["Servicio_Militar"],
                "Estado_Civil": client["Estado_Civil"],
                "Descripcion": client["Descripcion"],
            }
            return client_info
        except:
            return False
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
