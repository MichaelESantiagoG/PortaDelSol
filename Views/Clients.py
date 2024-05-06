import streamlit as st
import pandas as pd
import datetime
from datetime import datetime
from modules import conn


class Clients:

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
                <h2>Clientes</h2>
            </div>
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
