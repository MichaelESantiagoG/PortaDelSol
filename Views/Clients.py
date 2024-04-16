import streamlit as st
import pandas as pd
import datetime
from datetime import datetime
from modules import conn

# select_clients = """
# SELECT [Cliente_ID]
#       ,[Nombre]
#       ,[Apellido_Paterno]
#       ,[Apellido_Materno]
#       ,[Fecha_De_Nacimiento]
#       ,[Lugar_De_Nacimiento]
#       ,[Genero]
#       ,[Celular]
#       ,[Celular_2]
#       ,[Direccion]
#       ,[Licencia]
#       ,[Seguro_Social]
#       ,[Numero_De_Servicio_Militar]
#       ,[Descripcion]
#   FROM [dbo].[Clientes]"""
# select_client = """
# SELECT [Cliente_ID]
#       ,[Nombre]
#       ,[Apellido_Paterno]
#       ,[Apellido_Materno]
#       ,[Fecha_De_Nacimiento]
#       ,[Lugar_De_Nacimiento]
#       ,[Genero]
#       ,[Celular]
#       ,[Celular_2]
#       ,[Direccion]
#       ,[Licencia]
#       ,[Seguro_Social]
#       ,[Numero_De_Servicio_Militar]
#       ,[Descripcion]
#   FROM [dbo].[Clientes]
#   WHERE [Cliente_ID] = {}"""
# insert_client = """
# INSERT INTO [dbo].[Clientes]
#            ([Nombre]
#            ,[Apellido_Paterno]
#            ,[Apellido_Materno]
#            ,[Fecha_De_Nacimiento]
#            ,[Lugar_De_Nacimiento]
#            ,[Genero]
#            ,[Celular]
#            ,[Celular_2]
#            ,[Direccion]
#            ,[Licencia]
#            ,[Seguro_Social]
#            ,[Numero_De_Servicio_Militar]
#            ,[Descripcion])
#      VALUES
#            ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')

# """
# edit_client = """
# UPDATE [dbo].[Clientes]
#    SET [Nombre] = '{}'
#       ,[Apellido_Paterno] = '{}'
#       ,[Apellido_Materno] = '{}'
#       ,[Fecha_De_Nacimiento] = '{}'
#       ,[Lugar_De_Nacimiento] = '{}'
#       ,[Genero] = '{}'
#       ,[Celular] = '{}'
#       ,[Celular_2] = '{}'
#       ,[Direccion] = '{}'
#       ,[Licencia] = '{}'
#       ,[Seguro_Social] = '{}'
#       ,[Numero_De_Servicio_Militar] = '{}'
#       ,[Descripcion] = '{}'
#   where[dbo].Clientes.Cliente_ID = {} """
# delete_client = """
# DELETE FROM [dbo].[Clientes]
#   WHERE [Cliente_ID] = {}"""

select_clients = """SELECT * FROM Clientes;"""
select_client = """ SELECT * FROM Clientes WHERE Cliente_ID = {};"""
insert_client = """ INSERT INTO Clientes (Nombre, Apellido_Paterno, Apellido_Materno, Fecha_De_Nacimiento, Lugar_De_Nacimiento, Genero, Celular, Celular_2, Direccion, Licencia, Seguro_Social, Numero_De_Servicio_Militar, Descripcion) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
update_client = """ UPDATE Clientes 
                    SET Nombre = '{}', 
                        Apellido_Paterno = '{}', 
                        Apellido_Materno = '{}', 
                        Fecha_De_Nacimiento = '{}', 
                        Lugar_De_Nacimiento = '{}', 
                        Genero = '{}', 
                        Celular = '{}', 
                        Celular_2 = '{}', 
                        Direccion = '{}', 
                        Licencia = '{}',
                        Seguro_Social = '{}',
                        Numero_De_Servicio_Militar = '{}',
                        Descripcion = '{}'
                    WHERE Cliente_ID = {};
                """
delete_client = """ DELETE FROM Clientes WHERE Cliente_ID = {};"""


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
        st.dataframe(conn.query1(select_clients), hide_index=True)

    def add_client_form():
        key, disabled = "add_client", False
        with st.form(key=key, clear_on_submit=False, border=False):
            col1, col2 = st.columns(2)
            with col1:
                nombre = st.text_input(
                    key=key + "nombre", label="Nombre", disabled=disabled
                )
                apellido_paterno = st.text_input(
                    key=key + "apellido_paterno",
                    label="Apellido Paterno",
                    disabled=disabled,
                )
                apellido_materno = st.text_input(
                    key=key + "apellido_materno",
                    label="Apellido Materno",
                    disabled=disabled,
                )
                fecha_de_nacimiento = st.date_input(
                    key=key + "fecha_de_nacimiento",
                    label="Fecha de Nacimiento",
                    min_value=None,
                    max_value=None,
                    disabled=disabled,
                ).strftime("%Y-%m-%d")

                lugar_de_nacimiento = st.text_input(
                    key=key + "lugar_de_nacimiento",
                    label="Lugar de Nacimiento",
                    disabled=disabled,
                )
                genero = st.selectbox(
                    key=key + "genero",
                    label="Género",
                    options=["Masculino", "Femenino"],
                    disabled=disabled,
                )
                descripcion = st.text_input(
                    key=key + "descripcion", label="Descripcion", disabled=disabled
                )

            with col2:
                celular = st.text_input(
                    key=key + "celular", label="Celular", disabled=disabled
                )
                celular2 = st.text_input(
                    key=key + "celular2", label="Celular 2", disabled=disabled
                )
                direccion = st.text_area(
                    key=key + "direccion", label="Dirección", disabled=disabled
                )
                numero_de_licencia = st.text_input(
                    key=key + "numero_de_licencia", label="Licencia", disabled=disabled
                )
                seguro_social = st.text_input(
                    key=key + "seguro_social",
                    label="Seguro Social",
                    disabled=disabled,
                )
                numero_servicio_militar = st.text_input(
                    key=key + "numero_servicio_militar",
                    label="Número de Servicio Militar",
                    disabled=disabled,
                )

            if st.form_submit_button(
                label="Añadir", type="secondary", use_container_width=True
            ):
                try:
                    conn.query2(
                        insert_client.format(
                            nombre,
                            apellido_paterno,
                            apellido_materno,
                            fecha_de_nacimiento,
                            lugar_de_nacimiento,
                            genero,
                            celular,
                            celular2,
                            direccion,
                            numero_de_licencia,
                            seguro_social,
                            numero_servicio_militar,
                            descripcion,
                        )
                    )
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
                    nombre = st.text_input(
                        key=key + "nombre",
                        label="Nombre",
                        value=client_info["Nombre"],
                        disabled=disabled,
                    )
                    apellido_paterno = st.text_input(
                        key=key + "apellido_paterno",
                        label="Apellido Paterno",
                        value=client_info["Apellido_Paterno"],
                        disabled=disabled,
                    )
                    apellido_materno = st.text_input(
                        key=key + "apellido_materno",
                        label="Apellido Materno",
                        value=client_info["Apellido_Materno"],
                        disabled=disabled,
                    )
                    # Convert the date string to a datetime object
                    date_obj = datetime.strptime(
                        client_info["Fecha_De_Nacimiento"], "%Y-%m-%d"
                    ).date()

                    # Use the datetime object as the value for the date input
                    fecha_de_nacimiento = st.date_input(
                        key=key + "fecha_de_nacimiento",
                        label="Fecha de Nacimiento",
                        value=date_obj,
                        min_value=None,
                        max_value=None,
                        disabled=disabled,
                    )
                    lugar_de_nacimiento = st.text_input(
                        key=key + "lugar_de_nacimiento",
                        label="Lugar de Nacimiento",
                        value=client_info["Lugar_De_Nacimiento"],
                        disabled=disabled,
                    )
                    genero = st.selectbox(
                        key=key + "genero",
                        label="Género",
                        options=["Masculino", "Femenino"],
                        index=0 if client_info["Genero"] == "Masculino" else 1,
                        disabled=disabled,
                    )
                    descripcion = st.text_input(
                        key=key + "descripcion",
                        label="Descripcion",
                        value=client_info["Descripcion"],
                        disabled=disabled,
                    )

                with col2:
                    celular = st.text_input(
                        key=key + "celular",
                        label="Celular",
                        value=client_info["Celular"],
                        disabled=disabled,
                    )
                    celular2 = st.text_input(
                        key=key + "celular2",
                        label="Celular 2",
                        value=client_info["Celular_2"],
                        disabled=disabled,
                    )
                    direccion = st.text_area(
                        key=key + "direccion",
                        label="Dirección",
                        value=client_info["Direccion"],
                        disabled=disabled,
                    )
                    numero_de_licencia = st.text_input(
                        key=key + "numero_de_licencia",
                        label="Licencia",
                        value=client_info["Licencia"],
                        disabled=disabled,
                    )
                    seguro_social = st.text_input(
                        key=key + "seguro_social",
                        label="Seguro Social",
                        value=client_info["Seguro_Social"],
                        disabled=disabled,
                    )
                    numero_servicio_militar = st.text_input(
                        key=key + "numero_servicio_militar",
                        label="Número de Servicio Militar",
                        value=client_info["Numero_De_Servicio_Militar"],
                        disabled=disabled,
                    )

                if st.form_submit_button(
                    label="Actualizar", disabled=disabled, use_container_width=True
                ):
                    try:
                        query = update_client.format(
                            nombre,
                            apellido_paterno,
                            apellido_materno,
                            fecha_de_nacimiento,
                            lugar_de_nacimiento,
                            genero,
                            celular,
                            celular2,
                            direccion,
                            numero_de_licencia,
                            seguro_social,
                            numero_servicio_militar,
                            descripcion,
                            search_id,
                        )
                        conn.query2(query=query)
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
                    nombre = st.text_input(
                        key=key + "nombre",
                        label="Nombre",
                        value=client_info["Nombre"],
                        disabled=disabled,
                    )
                    apellido_paterno = st.text_input(
                        key=key + "apellido_paterno",
                        label="Apellido Paterno",
                        value=client_info["Apellido_Paterno"],
                        disabled=disabled,
                    )
                    apellido_materno = st.text_input(
                        key=key + "apellido_materno",
                        label="Apellido Materno",
                        value=client_info["Apellido_Materno"],
                        disabled=disabled,
                    )
                    date_obj = datetime.strptime(
                        client_info["Fecha_De_Nacimiento"], "%Y-%m-%d"
                    ).date()
                    fecha_de_nacimiento = st.date_input(
                        key=key + "fecha_de_nacimiento",
                        label="Fecha de Nacimiento",
                        value=date_obj,
                        min_value=None,
                        max_value=None,
                        disabled=disabled,
                    )
                    lugar_de_nacimiento = st.text_input(
                        key=key + "lugar_de_nacimiento",
                        label="Lugar de Nacimiento",
                        value=client_info["Lugar_De_Nacimiento"],
                        disabled=disabled,
                    )
                    genero = st.selectbox(
                        key=key + "genero",
                        label="Género",
                        options=["Masculino", "Femenino"],
                        index=0 if client_info["Genero"] == "Masculino" else 1,
                        disabled=disabled,
                    )
                    descripcion = st.text_input(
                        key=key + "descripcion",
                        label="Descripcion",
                        value=client_info["Descripcion"],
                        disabled=disabled,
                    )

                with col2:
                    celular = st.text_input(
                        key=key + "celular",
                        label="Celular",
                        value=client_info["Celular"],
                        disabled=disabled,
                    )
                    celular2 = st.text_input(
                        key=key + "celular2",
                        label="Celular 2",
                        value=client_info["Celular_2"],
                        disabled=disabled,
                    )
                    direccion = st.text_area(
                        key=key + "direccion",
                        label="Dirección",
                        value=client_info["Direccion"],
                        disabled=disabled,
                    )
                    numero_de_licencia = st.text_input(
                        key=key + "numero_de_licencia",
                        label="Licencia",
                        value=client_info["Licencia"],
                        disabled=disabled,
                    )
                    seguro_social = st.text_input(
                        key=key + "seguro_social",
                        label="Seguro Social",
                        value=client_info["Seguro_Social"],
                        disabled=disabled,
                    )
                    numero_servicio_militar = st.text_input(
                        key=key + "numero_servicio_militar",
                        label="Número de Servicio Militar",
                        value=client_info["Numero_De_Servicio_Militar"],
                        disabled=disabled,
                    )

                if st.form_submit_button(
                    label="Eliminar", disabled=False, use_container_width=True
                ):
                    try:
                        conn.query2(query=delete_client.format(search_id))
                        st.success("Cliente Eliminado")
                    except:
                        st.warning("No se pudo eliminar el cliente")
        else:
            st.warning("Cliente no existe")

    def select_client(search_id):
        try:
            # client = conn.Connections.query1(select_client.format(search_id))
            client = conn.query1(select_client.format(search_id))
            client_info = {
                "Cliente_ID": client.iloc[0, 0],  # row, column
                "Nombre": client.iloc[0, 1],
                "Apellido_Paterno": client.iloc[0, 2],
                "Apellido_Materno": client.iloc[0, 3],
                "Fecha_De_Nacimiento": client.iloc[0, 4],
                "Lugar_De_Nacimiento": client.iloc[0, 5],
                "Genero": client.iloc[0, 6],
                "Celular": client.iloc[0, 7],
                "Celular_2": client.iloc[0, 8],
                "Direccion": client.iloc[0, 9],
                "Licencia": client.iloc[0, 10],
                "Seguro_Social": client.iloc[0, 11],
                "Numero_De_Servicio_Militar": client.iloc[0, 12],
                "Descripcion": client.iloc[0, 13],
            }
            return client_info
        except:
            return False

    def select_mock_data():
        client_info = {
            "Nombre": "Juan",
            "Apellido_Paterno": "Gonzalez",
            "Apellido_Materno": "Perez",
            "Fecha_De_Nacimiento": datetime(1990, 5, 15),
            "Lugar_De_Nacimiento": "Ciudad de Mexico",
            "Genero": "Masculino",
            "Celular": "5551234567",
            "Celular_2": "5551112233",
            "Direccion": "Calle 123",
            "Licencia": "L123456",
            "Seguro_Social": "1234567890",
            "Numero_De_Servicio_Militar": "S12345",
        }
        return client_info
