import streamlit as st
from datetime import datetime
from modules import conn


class Deceased:

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
            .st-fq {
                width: 500px;
            }
            </style>
            <div class="middle-center">
                <h1>Porta del Sol</h1>
                <h2>Difuntos</h2>
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
                    Deceased.add_deceased()
                with tab2:
                    Deceased.edit_deceased()
                with tab3:
                    Deceased.delete_deceased()
        st.write("***")
        # st.dataframe(conn.Connections.query1(select_clients))
        st.dataframe(conn.Select_All.Difuntos(), hide_index=True)

    def add_deceased():
        difunto = Deceased.form("add", "Añadir", False)
        if difunto:
            try:
                conn.Insert.Difunto(difunto)
                st.success("Registro del difunto Añadido")
            except:
                st.warning(
                    "Registro del difunto no ha podido ser añadido\n Intente más tarde"
                )

    def edit_deceased():
        search_id = st.number_input(
            key="update_search_id", label="ID de Cliente", min_value=1, step=1
        )
        try:
            difunto = conn.Select.Difunto(search_id)
            try:
                updated_difunto = Deceased.form(
                    "edit", "Editar", False, default=difunto
                )
                if updated_difunto:
                    conn.Update.Difunto(search_id, updated_difunto)
                    st.success("Registro Actualizado")
            except:
                st.warning(
                    "No se ha podido actualizar el registro\nFavor trate más tarde"
                )

        except:
            st.warning(f"Record #{search_id} no existe")

    def delete_deceased():
        search_id = st.number_input(
            key="delete_search_id", label="ID de Cliente", min_value=1, step=1
        )
        try:
            difunto = conn.Select.Difunto(search_id)
            try:
                if Deceased.form(
                    "delete", "Eliminar", True, default=conn.Select.Difunto(search_id)
                ):
                    conn.Delete.Difunto(search_id)
                    st.success("Registro eliminado")
            except:
                st.warning("Registro no eliminado")
        except:
            st.warning(f"Record #{search_id} no existe")

    def form(key: str, label: str, disabled: bool, default: dict = None):
        with st.form(key=key, clear_on_submit=False, border=False):
            col1, col2 = st.columns(2)
            with col1:
                Nombre = st.text_input(
                    label="Nombre",
                    key=key + "Nombre",
                    disabled=disabled,
                    value=(
                        default["Nombre"] if default and "Nombre" in default else ""
                    ),
                )
                Apellido_Paterno = st.text_input(
                    label="Apellido Paterno",
                    key=key + "Apellido Paterno",
                    disabled=disabled,
                    value=(
                        default["Apellido_Paterno"]
                        if default and "Apellido_Paterno" in default
                        else ""
                    ),
                )
                Apellidp_Materno = st.text_input(
                    label="Apellido Materno",
                    key=key + "Apellido Materno",
                    disabled=disabled,
                    value=(
                        default["Apellidp_Materno"]
                        if default and "Apellidp_Materno" in default
                        else ""
                    ),
                )
                Genero = st.selectbox(
                    key=key + "Genero",
                    label="Género",
                    options=["Masculino", "Femenino"],
                    disabled=disabled,
                    index=(
                        0
                        if default
                        and "Genero" in default
                        and default["Genero"] == "Masculino"
                        else 1
                    ),
                )
                Estado_Civil = st.selectbox(
                    key=key + "Estado_Civil",
                    label="Estado Civil",
                    disabled=disabled,
                    options=["Soltero", "Casado", "Divorciado", "Viudo"],
                    index=(
                        ["Soltero", "Casado", "Divorciado", "Viudo"].index(
                            default["Estado_Civil"]
                        )
                        if default and "Estado_Civil" in default
                        else 0
                    ),
                )
                Nombre_Padre = st.text_input(
                    label="Nombre del Padre",
                    key=key + "Nombre_Padre",
                    disabled=disabled,
                    value=(
                        default["Nombre_Padre"]
                        if default and "Nombre_Padre" in default
                        else ""
                    ),
                )
                Nombre_Madre = st.text_input(
                    label="Nombre del Madre",
                    key=key + "Nombre_Madre",
                    disabled=disabled,
                    value=(
                        default["Nombre_Madre"]
                        if default and "Nombre_Madre" in default
                        else ""
                    ),
                )
            with col2:
                Seguro_Social = st.text_input(
                    key=key + "Seguro_Social",
                    label="Seguro Social",
                    disabled=disabled,
                    value=(
                        default["Seguro_Social"]
                        if default and "Seguro_Social" in default
                        else ""
                    ),
                )
                Servicio_Militar = st.text_input(
                    key=key + "Servicio_Militar",
                    label="Número de Servicio Militar",
                    disabled=disabled,
                    value=(
                        default["Servicio_Militar"]
                        if default and "Servicio_Militar" in default
                        else ""
                    ),
                )
                Lugar_Nacimiento = st.text_input(
                    key=key + "Lugar_Nacimiento",
                    label="Lugar de Nacimiento",
                    disabled=disabled,
                    value=(
                        default["Lugar_Nacimiento"]
                        if default and "Lugar_Nacimiento" in default
                        else ""
                    ),
                )
                Edad = st.number_input(
                    label="Edad",
                    key=key + "Edad",
                    disabled=disabled,
                    min_value=0,
                    value=default["Edad"] if default and "Edad" in default else 0,
                )

                Fecha_Nacimiento_default = (
                    "today"
                    if not default or "Fecha_Nacimiento" not in default
                    else datetime.strptime(
                        default["Fecha_Nacimiento"], "%Y-%m-%d"
                    ).date()
                )
                Fecha_Nacimiento = st.date_input(
                    key=key + "Fecha_Nacimiento",
                    label="Fecha de Nacimiento",
                    min_value=None,
                    max_value=None,
                    disabled=disabled,
                    value=Fecha_Nacimiento_default,
                ).strftime("%Y-%m-%d")

                Fecha_Defuncion_default = (
                    "today"
                    if not default or "Fecha_Defuncion" not in default
                    else datetime.strptime(
                        default["Fecha_Defuncion"], "%Y-%m-%d"
                    ).date()
                )
                Fecha_Defuncion = st.date_input(
                    key=key + "Fecha_Defuncion",
                    label="Fecha de Defunción",
                    min_value=None,
                    max_value=None,
                    disabled=disabled,
                    value=Fecha_Defuncion_default,
                ).strftime("%Y-%m-%d")

            if st.form_submit_button(
                label=label,
                use_container_width=True,
            ):
                difunto = {
                    "Nombre": Nombre,
                    "Apellido_Paterno": Apellido_Paterno,
                    "Apellidp_Materno": Apellidp_Materno,
                    "Genero": Genero,
                    "Estado_Civil": Estado_Civil,
                    "Nombre_Padre": Nombre_Padre,
                    "Nombre_Madre": Nombre_Madre,
                    "Seguro_Social": Seguro_Social,
                    "Servicio_Militar": Servicio_Militar,
                    "Edad": Edad,
                    "Lugar_Nacimiento": Lugar_Nacimiento,
                    "Fecha_Nacimiento": Fecha_Nacimiento,
                    "Fecha_Defuncion": Fecha_Defuncion,
                }
                return difunto
