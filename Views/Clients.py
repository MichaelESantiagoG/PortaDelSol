import streamlit as st
import pandas as pd
import datetime
from datetime import datetime
from modules import conn

select_clients = """
SELECT [Cliente_ID]
      ,[Nombre]
      ,[Apellido_Paterno]
      ,[Apellido_Materno]
      ,[Fecha_De_Nacimiento]
      ,[Lugar_De_Nacimiento]
      ,[Genero]
      ,[Celular]
      ,[Celular_2]
      ,[Direccion]
      ,[Licencia]
      ,[Seguro_Social]
      ,[Numero_De_Servicio_Militar]
      ,[Descripcion]
  FROM [dbo].[Clientes]"""
select_client = """
SELECT [Cliente_ID]
      ,[Nombre]
      ,[Apellido_Paterno]
      ,[Apellido_Materno]
      ,[Fecha_De_Nacimiento]
      ,[Lugar_De_Nacimiento]
      ,[Genero]
      ,[Celular]
      ,[Celular_2]
      ,[Direccion]
      ,[Licencia]
      ,[Seguro_Social]
      ,[Numero_De_Servicio_Militar]
      ,[Descripcion]
  FROM [dbo].[Clientes]
  WHERE [Cliente_ID] = {}"""
insert_client = """
INSERT INTO [dbo].[Clientes]
           ([Nombre]
           ,[Apellido_Paterno]
           ,[Apellido_Materno]
           ,[Fecha_De_Nacimiento]
           ,[Lugar_De_Nacimiento]
           ,[Genero]
           ,[Celular]
           ,[Celular_2]
           ,[Direccion]
           ,[Licencia]
           ,[Seguro_Social]
           ,[Numero_De_Servicio_Militar]
           ,[Descripcion])
     VALUES
           ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')

"""
edit_client = """
UPDATE [dbo].[Clientes]
   SET [Nombre] = '{}'
      ,[Apellido_Paterno] = '{}'
      ,[Apellido_Materno] = '{}'
      ,[Fecha_De_Nacimiento] = '{}'
      ,[Lugar_De_Nacimiento] = '{}'
      ,[Genero] = '{}'
      ,[Celular] = '{}'
      ,[Celular_2] = '{}'
      ,[Direccion] = '{}'
      ,[Licencia] = '{}'
      ,[Seguro_Social] = '{}'
      ,[Numero_De_Servicio_Militar] = '{}'
      ,[Descripcion] = '{}'
  where[dbo].Clientes.Cliente_ID = {} """
delete_client = """
DELETE FROM [dbo].[Clientes]
  WHERE [Cliente_ID] = {}"""


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
                    .st-emotion-cache-1i4zmrw{
                        float:right;
                        margin-top: 13px;
                        }
                </style>

                """,
                unsafe_allow_html=True,
            )
            with st.popover(label="Más+", use_container_width=False, ):
                tab1, tab2, tab3 = st.tabs(["Añadir", "Editar", "Borrar"])

                with tab1:Clients.add_client_form()
                with tab2:Clients.edit_client_form()
                with tab3:Clients.delete_client_form()

        st.write('***')
        st.dataframe(conn.Connections.query1(select_clients))

    @staticmethod
    def add_client_form():
        key, disabled = 'add_client', False
        with st.form(key=key, clear_on_submit=False, border=False):
            col1, col2 = st.columns(2)
            with col1:
                nombre = st.text_input(key=key + 'first_name', label="Nombre", disabled=disabled)
                apellido_paterno = st.text_input(key= key + 'last_name', label="Apellido Paterno", disabled=disabled)
                apellido_materno = st.text_input(key= key + 'maternal_name', label="Apellido Materno", disabled=disabled)
                fecha_de_nacimiento = st.date_input(key= key + 'birth_date', label="Fecha de Nacimiento", min_value=None, max_value=None, disabled=disabled)
                lugar_de_nacimiento = st.text_input(key= key + 'birth_place', label="Lugar de Nacimiento", disabled=disabled)
                genero = st.selectbox(key= key + 'gender', label="Género", options=['Masculino', 'Femenino'], disabled=disabled)
                descripcion = st.text_input(key=key + 'descripcion', label="Descripcion", disabled=disabled)

            with col2:
                celular = st.text_input(key= key + 'phone_number', label="Celular", disabled=disabled)
                celular2 = st.text_input(key= key + 'phone_number2', label="Celular 2", disabled=disabled)
                direccion = st.text_area(key= key + 'address', label="Dirección", disabled=disabled)
                numero_de_licencia = st.text_input(key= key + 'license_number', label="Licencia", disabled=disabled)
                seguro_social = st.text_input(key= key + 'social_security', label="Seguro Social", disabled=disabled)
                numero_servicio_militar = st.text_input(key= key + 'military_service_number', label="Número de Servicio Militar", disabled=disabled)

            if st.form_submit_button(label="Añadir", type="secondary", use_container_width=True):
                try:
                    query = insert_client.format(nombre, apellido_paterno, apellido_materno, fecha_de_nacimiento, lugar_de_nacimiento, genero, celular, celular2, direccion, numero_de_licencia, seguro_social, numero_servicio_militar, descripcion)
                    conn.Connections.query2(query=query)
                    st.success("Cliente añadido")

                except:
                    st.warning('Cliente NO se pudo añadir')


    def edit_client_form():
            key, disabled = 'edit_client', False
            search_id = st.number_input(key=key + 'search_id', label="ID de Cliente", min_value=0, step=1)
            client_info = Clients.select_client(search_id)
            if client_info:
                with st.form(key = key+'form', clear_on_submit=True, border=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        first_name = st.text_input(key=key + 'first_name', label="Nombre", value=client_info['Nombre'], disabled=disabled)
                        last_name = st.text_input(key=key + 'last_name', label="Apellido Paterno", value=client_info['Apellido_Paterno'], disabled=disabled)
                        maternal_name = st.text_input(key=key + 'maternal_name', label="Apellido Materno", value=client_info['Apellido_Materno'], disabled=disabled)
                        birth_date = st.date_input(key=key + 'birth_date', label="Fecha de Nacimiento", value=client_info['Fecha_De_Nacimiento'], min_value=None, max_value=None, disabled=disabled)
                        birth_place = st.text_input(key=key + 'birth_place', label="Lugar de Nacimiento", value=client_info['Lugar_De_Nacimiento'], disabled=disabled)
                        gender = st.selectbox(key=key + 'gender', label="Género", options=['Masculino', 'Femenino'], index=0 if client_info['Genero'] == 'Masculino' else 1, disabled=disabled)
                        descripcion = st.text_input(key=key + 'descripcion', label="Descripcion", value=client_info['Descripcion'], disabled=disabled)

                    with col2:
                        phone_number = st.text_input(key=key + 'phone_number', label="Celular", value=client_info['Celular'], disabled=disabled)
                        phone_number2 = st.text_input(key=key + 'phone_number2', label="Celular 2", value=client_info['Celular_2'], disabled=disabled)
                        address = st.text_area(key=key + 'address', label="Dirección", value=client_info['Direccion'], disabled=disabled)
                        license_number = st.text_input(key=key + 'license_number', label="Licencia", value=client_info['Licencia'], disabled=disabled)
                        social_security = st.text_input(key=key + 'social_security', label="Seguro Social", value=client_info['Seguro_Social'], disabled=disabled)
                        military_service_number = st.text_input(key=key + 'military_service_number', label="Número de Servicio Militar", value=client_info['Numero_De_Servicio_Militar'], disabled=disabled)

                    if st.form_submit_button(label="Actualizar", disabled=disabled, use_container_width=True):
                        try:
                            query = edit_client.format(first_name, last_name, maternal_name, birth_date, birth_place, gender, phone_number, phone_number2, address, license_number, social_security, military_service_number, descripcion, search_id)
                            conn.Connections.query2(query=query)
                            st.success("Cliente actualizado")
                        except:
                            st.warning('No se pudo actualizar el cliente')
            else: st.warning('Cliente no existe')


    def delete_client_form():
            key, disabled = 'delete_client', True
            search_id = st.number_input(key=key + 'search_id', label="ID de Cliente", min_value=0, step=1)
            client_info = Clients.select_client(search_id)
            if client_info:
                with st.form(key = key+'form', clear_on_submit=True, border=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        first_name = st.text_input(key=key + 'first_name', label="Nombre", value=client_info['Nombre'], disabled=disabled)
                        last_name = st.text_input(key=key + 'last_name', label="Apellido Paterno", value=client_info['Apellido_Paterno'], disabled=disabled)
                        maternal_name = st.text_input(key=key + 'maternal_name', label="Apellido Materno", value=client_info['Apellido_Materno'], disabled=disabled)
                        birth_date = st.date_input(key=key + 'birth_date', label="Fecha de Nacimiento", value=client_info['Fecha_De_Nacimiento'], min_value=None, max_value=None, disabled=disabled)
                        birth_place = st.text_input(key=key + 'birth_place', label="Lugar de Nacimiento", value=client_info['Lugar_De_Nacimiento'], disabled=disabled)
                        gender = st.selectbox(key=key + 'gender', label="Género", options=['Masculino', 'Femenino'], index=0 if client_info['Genero'] == 'Masculino' else 1, disabled=disabled)
                        descripcion = st.text_input(key=key + 'descripcion', label="Descripcion", value=client_info['Descripcion'], disabled=disabled)

                    with col2:
                        phone_number = st.text_input(key=key + 'phone_number', label="Celular", value=client_info['Celular'], disabled=disabled)
                        phone_number2 = st.text_input(key=key + 'phone_number2', label="Celular 2", value=client_info['Celular_2'], disabled=disabled)
                        address = st.text_area(key=key + 'address', label="Dirección", value=client_info['Direccion'], disabled=disabled)
                        license_number = st.text_input(key=key + 'license_number', label="Licencia", value=client_info['Licencia'], disabled=disabled)
                        social_security = st.text_input(key=key + 'social_security', label="Seguro Social", value=client_info['Seguro_Social'], disabled=disabled)
                        military_service_number = st.text_input(key=key + 'military_service_number', label="Número de Servicio Militar", value=client_info['Numero_De_Servicio_Militar'], disabled=disabled)

                    if st.form_submit_button(label="Eliminar", disabled=False, use_container_width=True):
                        try:
                            query = delete_client.format(search_id)
                            conn.Connections.query2(query=query)
                            st.success("Cliente Eliminado")
                        except:
                            st.warning('No se pudo actualizar el cliente')
            else: st.warning('Cliente no existe')


    def select_client(search_id):
        try:
            client = conn.Connections.query1(select_client.format(search_id))
            client_info = {
                'Cliente_ID':client.iloc[0, 0],     # row, column
                'Nombre': client.iloc[0, 1],  
                'Apellido_Paterno': client.iloc[0, 2],
                'Apellido_Materno': client.iloc[0, 3],
                'Fecha_De_Nacimiento': client.iloc[0, 4],
                'Lugar_De_Nacimiento': client.iloc[0, 5],
                'Genero': client.iloc[0, 6],
                'Celular': client.iloc[0, 7],
                'Celular_2': client.iloc[0, 8],
                'Direccion': client.iloc[0, 9],
                'Licencia': client.iloc[0, 10],
                'Seguro_Social': client.iloc[0, 11],
                'Numero_De_Servicio_Militar': client.iloc[0, 12],
                'Descripcion': client.iloc[0, 13],

            }
            return client_info
        except: return False


    def select_mock_data():
        client_info = {
            'Nombre': 'Juan',
            'Apellido_Paterno': 'Gonzalez',
            'Apellido_Materno': 'Perez',
            'Fecha_De_Nacimiento': datetime(1990, 5, 15),
            'Lugar_De_Nacimiento': 'Ciudad de Mexico',
            'Genero': 'Masculino',
            'Celular': '5551234567',
            'Celular_2': '5551112233',
            'Direccion': 'Calle 123',
            'Licencia': 'L123456',
            'Seguro_Social': '1234567890',
            'Numero_De_Servicio_Militar': 'S12345'
            }
        return client_info