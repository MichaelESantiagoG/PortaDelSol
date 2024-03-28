import streamlit as st
import pandas as pd
from modules import conn

select_services = """
    SELECT TOP (1000) [Servicio_ID]
        ,[Servicio_Nombre]
        ,[Servicio_Precio]
    FROM [dbo].[Servicios]
    """
select_service = """"""
insert_services = """"""
delete_service = """"""

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
# {
        # datos_servicios = {
        #     'Servicio': ['Cremación', 'Entierro tradicional', 'Funeral religioso', 'Servicio de urna', 'Pre-arreglos funerarios'],
        #     'Precio': ['$1000', '$2000', '$1500', 'N/A', 'N/A'],
        #     'Incluye': ['Urna básica', 'Ataúd, sala de velatorio', 'Servicio religioso', 'N/A', 'N/A']
        # }

        # # Replicar los datos 50 veces
        # datos_repetidos = {k: v * 50 for k, v in datos_servicios.items()}

        # # Crear el DataFrame con los datos repetidos
        # df_servicios = pd.DataFrame(datos_repetidos)
# }

        # Mostrar el DataFrame en Streamlit
       
        col1, col2 = st.columns([30,50])
        with col1: st.dataframe(data=conn.Connections.query1(select_services), hide_index=True)
        with col2: 
            with st.container(border=True):
                tab1, tab2, tab3 = st.tabs(['Añadir', 'Editar', 'Eliminar'])
                with tab1: Servicios.Servicios_Formulario('Añadir', False)
                with tab2: Servicios.Servicios_Formulario('Editar', True)
                with tab3: Servicios.Servicios_Formulario('Eliminar', True)

    @staticmethod
    def Servicios_Formulario(mode: str, disable: bool):
        option_types = ['Velorio','Entierro','Cremación']
        if mode != "Añadir": 
            st.text_input(key = mode + 'search', label='Buscar ID')
        if mode == "Añadir": pass
        if mode == "Editar": pass
            # option_types = searched
        if mode == "Eliminar": pass
            # option_types = searched
        with st.form(key=mode, border=False):
            nombre_de_servcicio = st.selectbox(key= mode + 'nombre_de_servcicio' , label='Tipo de Servicio', options=option_types, disabled=disable)
            precio_de_servicio = st.number_input(key= mode + 'precio_de_servicio', label='Precio de Servicio', step= 0.01, min_value=0.0, disabled=disable)
            servicio = Servicios(nombre_de_servcicio=nombre_de_servcicio, precio_de_servicio=precio_de_servicio)
            if st.form_submit_button(label=mode): 
                if mode == "Añadir": 
                    try: 
                        Servicios.Añadir_Servicio(servicio)
                        st.success('Exitoso')
                    except: st.error('Fracaso')
                if mode == "Editar": 
                    try: 
                        Servicios.Editar_Servicio(servicio)
                        st.warning('Actualizado')
                    except: st.error('Fracaso al actualizar')
                if mode == "Eliminar": 
                    try: 
                        Servicios.Eliminar_Servicio(servicio)
                        st.warning('Eliminado')
                    except: st.error('Fracaso al actualizar')

    def Buscar_Servicio(Servicio): pass
    def Añadir_Servicio(Servicio): pass
    def Editar_Servicio(Servicio): pass
    def Eliminar_Servicio(Servicio): pass


