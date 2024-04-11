import streamlit as st
import pandas as pd
from modules import conn

select_services = """
    SELECT TOP (1000) [Servicio_ID]
        ,[Servicio_Nombre]
        ,[Servicio_Precio]
    FROM [dbo].[Servicios]
    """

select_service = """
    SELECT [Servicio_ID]
        ,[Servicio_Nombre]
        ,[Servicio_Precio]
    FROM [dbo].[Servicios]
    WHERE [dbo].[Servicios].[Servicio_ID] = {}
    """

insert_service = """
INSERT INTO [dbo].[Servicios]
           ([Servicio_Nombre]
           ,[Servicio_Precio])
     VALUES
           ('{}',{})"""

update_service = """
    UPDATE [dbo].[Servicios]
    SET [Servicio_Nombre] = '{}'
        ,[Servicio_Precio] = {}
    WHERE [dbo].[Servicios].[Servicio_ID] = {}
    """

delete_service = """
    DELETE FROM [dbo].[Servicios]
        WHERE [dbo].[Servicios].[Servicio_ID] = {}
    GO
    """

class Servicios:

    def __init__(self, nombre_de_servcicio, precio_de_servicio ) -> None:
        self.nombre_de_servcicio = nombre_de_servcicio
        self.precio_de_servicio = precio_de_servicio
        pass


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
        
        # Crear el DataFrame con los datos de los servicios
        datos_servicios = {
            'Servicio': ['Cremación', 'Entierro tradicional', 'Funeral religioso', 'Servicio de urna', 'Pre-arreglos funerarios'],
            'Precio': ['$1000', '$2000', '$1500', 'N/A', 'N/A'],
        }

        # Replicar los datos 50 veces
        datos_repetidos = {k: v * 50 for k, v in datos_servicios.items()}
        df_servicios = pd.DataFrame(datos_repetidos)

        col1, col2 = st.columns([30,50])
        with col1: 
            st.dataframe(data=conn.Connections.query1(select_services), hide_index=True)
            #st.dataframe(data=df_servicios, hide_index=False)

        with col2: 
            with st.container(border=True):
                tab1, tab2, tab3 = st.tabs(['Añadir', 'Editar', 'Eliminar'])
                with tab1: Servicios.add_service_form()
                with tab2: Servicios.edit_service_form()
                with tab3: Servicios.delete_service_form()

    @staticmethod
    def Buscar_Servicio(id):
        try: 
            servicio = conn.Connections.query1(select_service.format(id))
            if not servicio.empty:
                nombre = servicio['Servicio_Nombre'].iloc[0]
                precio = servicio['Servicio_Precio'].iloc[0]
                return nombre, precio
            else:
                st.warning("Servicio no existe")
                return None, None
        except Exception as e:
            st.error(f"Error al buscar servicio: {e}")
            return None, None

    def add_service_form():
        key, disable = 'Añadir', False
        with st.form(key=key, border=False, clear_on_submit=True):
            nombre_de_servcicio = st.text_input(key= key + 'nombre_de_servcicio' , label='Tipo de Servicio', disabled=disable)
            precio_de_servicio = st.number_input(key= key + 'precio_de_servicio', label='Precio de Servicio', step= 0.01, min_value=0.0, disabled=disable)
            servicio = Servicios(nombre_de_servcicio=nombre_de_servcicio, precio_de_servicio=precio_de_servicio)
            if st.form_submit_button(label=key): 
                try:
                    if servicio.nombre_de_servcicio == '' or servicio.precio_de_servicio == 0: return st.warning("Favor y llenar todos los elementos")
                    conn.Connections.query2(insert_service.format(servicio.nombre_de_servcicio, servicio.precio_de_servicio))
                    st.success('Servicio Añadido {}: {}'.format(servicio.nombre_de_servcicio, servicio.precio_de_servicio))
                except: st.warning('Servicio No Añadido')
                
    def edit_service_form():
        key, disable = 'Editar', False
        id = st.number_input(key = key + 'search', label='Buscar ID', min_value=0, step=1)
        servicio = Servicios.Buscar_Servicio(id)
        nombre, precio = servicio[0], servicio[1]
        with st.form(key=key, border=False, clear_on_submit=True):
            nombre_de_servcicio = st.text_input(value=nombre, key=key + 'nombre_de_servcicio' , label='Tipo de Servicio', disabled=disable)
            precio_de_servicio = st.number_input(value=precio, key=key + 'precio_de_servicio', label='Precio de Servicio', step= 0.01, min_value=0.0, disabled=disable)
            servicio = Servicios(nombre_de_servcicio=nombre_de_servcicio, precio_de_servicio=precio_de_servicio)
            if st.form_submit_button(label=key): 
                try:
                    conn.Connections.query2(update_service.format(servicio.nombre_de_servcicio, servicio.precio_de_servicio, id))
                    st.warning('Servicio Actualizado')
                except: st.error('Error al Actualizar')

    def delete_service_form():
        key, disable = 'Eliminar', True
        id = st.number_input(key = key + 'search', label='Buscar ID',min_value=0, step=1)
        servicio = Servicios.Buscar_Servicio(id)
        nombre, precio = servicio[0], servicio[1]
        with st.form(key=key, border=False, clear_on_submit=True):
            nombre_de_servcicio = st.text_input(value=nombre, key=key + 'nombre_de_servcicio', label='Tipo de Servicio', disabled=disable)
            precio_de_servicio = st.number_input(value=precio, key=key + 'precio_de_servicio', label='Precio de Servicio', step= 0.01, min_value=0.0, disabled=disable)
            servicio = Servicios(nombre_de_servcicio=nombre_de_servcicio, precio_de_servicio=precio_de_servicio)
            if st.form_submit_button(label=key): 
                try:
                    conn.Connections.query2(delete_service.format(id))
                    st.warning('Servicio Eliminado {}: {}'.format(servicio.nombre_de_servcicio, servicio.precio_de_servicio))
                except: st.error('Servicio No Eliminado')
