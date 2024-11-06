import streamlit as st
import pandas as pd
<<<<<<< HEAD

class Services:
    @staticmethod
=======
from modules import conn
import time


class Servicios:
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
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

<<<<<<< HEAD
        col1, col2 = st.columns(2)
        with col1:
            search = st.text_input(label="Buscar", placeholder="Buscar")
        with col2:
            services_add_container =  st.container()
            with services_add_container:
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

    
=======
        col1, col2 = st.columns([50, 50])
        with col1:
            st.dataframe(data=conn.Select_All.Servicios(), hide_index=True)
            # st.dataframe(data=df_servicios, hide_index=False)

        with col2:
            with st.container(border=True):
                tab1, tab2, tab3 = st.tabs(["Añadir", "Editar", "Eliminar"])
                with tab1:
                    Servicios.add_service_form()
                with tab2:
                    Servicios.edit_service_form()
                with tab3:
                    Servicios.delete_service_form()

    def add_service_form():
        key, disable = "add_service", False
        with st.form(key=key, border=False, clear_on_submit=True):
            nombre_de_servcicio = st.text_input(
                key=key + "nombre_de_servcicio",
                label="Tipo de Servicio",
                disabled=disable,
            )
            Servicio_Precio = st.number_input(
                key=key + "Servicio_Precio",
                label="Precio de Servicio",
                step=0.01,
                min_value=0.0,
                disabled=disable,
            )

            if st.form_submit_button(
                label="Añadir", type="secondary", use_container_width=False
            ):
                try:
                    Servicio = {
                        "Servicio_Nombre": nombre_de_servcicio,
                        "Servicio_Precio": Servicio_Precio,
                    }
                    conn.Insert.Servicio(Servicio)
                    st.success("Servicio Añadido")
                    time.sleep(3)

                except:
                    st.warning("Servicio No se pudo añadir")
                    time.sleep(3)
                st.rerun()

    def edit_service_form():
        key, disable = "Editar", False
        search_id = st.number_input(
            key=key + "search", label="Buscar ID", min_value=0, step=1
        )
        service_info = Servicios.select_service(search_id)
        if service_info:
            with st.form(key=key, border=False, clear_on_submit=True):
                nombre_de_servcicio = st.text_input(
                    value=service_info["Servicio_Nombre"],
                    key=key + "nombre_de_servcicio",
                    label="Tipo de Servicio",
                    disabled=disable,
                )
                Servicio_Precio = st.number_input(
                    value=float(service_info["Servicio_Precio"]),
                    key=key + "Servicio_Precio",
                    label="Precio de Servicio",
                    step=0.01,
                    min_value=0.0,
                    disabled=disable,
                )

                if st.form_submit_button(
                    label="Actualizar", type="secondary", use_container_width=False
                ):
                    try:
                        Servicio = {
                            "Servicio_Nombre": nombre_de_servcicio,
                            "Servicio_Precio": Servicio_Precio,
                        }
                        conn.Update.Servicio(search_id, Servicio)
                        st.success("Servicio Actualizado")
                        time.sleep(3)
                    except:
                        st.error("Error al Actualizar")
                        time.sleep(3)
                    st.rerun()

        else:
            st.warning("Servicio no existe")

    def delete_service_form():
        key, disable = "Eliminar", True
        search_id = st.number_input(
            key=key + "search", label="Buscar ID", min_value=0, step=1
        )
        service_info = Servicios.select_service(search_id)
        if service_info:
            with st.form(key=key, border=False, clear_on_submit=True):
                nombre_de_servcicio = st.text_input(
                    value=service_info["Servicio_Nombre"],
                    key=key + "nombre_de_servcicio",
                    label="Tipo de Servicio",
                    disabled=disable,
                )
                Servicio_Precio = st.number_input(
                    value=service_info["Servicio_Precio"],
                    key=key + "Servicio_Precio",
                    label="Precio de Servicio",
                    step=0.01,
                    min_value=0.0,
                    disabled=disable,
                )

                if st.form_submit_button(
                    label="Eliminar", type="secondary", use_container_width=False
                ):
                    try:
                        conn.Delete.Servicio(search_id)
                        st.success("Servicio Eliminado")
                        time.sleep(3)
                    except:
                        st.warning("Servicio no se pudo eliminar")
                        time.sleep(3)
                    st.rerun()

        else:
            st.warning("Servicio no existe")

    def select_service(id):
        try:
            service = conn.Select.Servicio(id)
            service_info = {
                "Servicio_ID": service["Servicio_ID"],
                "Servicio_Nombre": service["Servicio_Nombre"],
                "Servicio_Precio": float(service["Servicio_Precio"]),
            }
            return service_info
        except:
            return False
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
