import streamlit as st
import pandas as pd
from modules import conn
import time

select_services = """SELECT * FROM Servicios;"""
select_service = """SELECT * FROM Servicios WHERE Servicio_ID = {} ;"""
insert_service = (
    """INSERT INTO Servicios (Servicio_Nombre, Servicio_Precio) VALUES ('{}', {});"""
)
update_service = """UPDATE Servicios SET Servicio_Nombre = '{}', Servicio_Precio = {} WHERE Servicio_ID = {};"""
delete_service = """DELETE FROM Servicios WHERE Servicio_ID = {};"""


class Servicios:
    def load_data():
        return conn.query1(select_services)

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

        col1, col2 = st.columns([50, 50])
        with col1:
            st.dataframe(data=Servicios.load_data(), hide_index=True)
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
            precio_de_servicio = st.number_input(
                key=key + "precio_de_servicio",
                label="Precio de Servicio",
                step=0.01,
                min_value=0.0,
                disabled=disable,
            )

            if st.form_submit_button(
                label="Añadir", type="secondary", use_container_width=False
            ):
                try:
                    conn.query2(
                        insert_service.format(nombre_de_servcicio, precio_de_servicio)
                    )
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
                    value=service_info["Nombre_De_Servicio"],
                    key=key + "nombre_de_servcicio",
                    label="Tipo de Servicio",
                    disabled=disable,
                )
                precio_de_servicio = st.number_input(
                    value=float(service_info["Precio_De_Servicio"]),
                    key=key + "precio_de_servicio",
                    label="Precio de Servicio",
                    step=0.01,
                    min_value=0.0,
                    disabled=disable,
                )

                if st.form_submit_button(
                    label="Actualizar", type="secondary", use_container_width=False
                ):
                    try:
                        conn.query2(
                            update_service.format(
                                nombre_de_servcicio,
                                precio_de_servicio,
                                search_id,
                            )
                        )
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
                    value=service_info["Nombre_De_Servicio"],
                    key=key + "nombre_de_servcicio",
                    label="Tipo de Servicio",
                    disabled=disable,
                )
                precio_de_servicio = st.number_input(
                    value=service_info["Precio_De_Servicio"],
                    key=key + "precio_de_servicio",
                    label="Precio de Servicio",
                    step=0.01,
                    min_value=0.0,
                    disabled=disable,
                )

                if st.form_submit_button(
                    label="Eliminar", type="secondary", use_container_width=False
                ):
                    try:
                        conn.query2(
                            delete_service.format(
                                search_id,
                            )
                        )
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
            service = conn.query1(select_service.format(id))
            service_info = {
                "Servicio_ID": service.iloc[0, 0],
                "Nombre_De_Servicio": service.iloc[0, 1],
                "Precio_De_Servicio": float(service.iloc[0, 2]),
            }
            return service_info
        except:
            return False
