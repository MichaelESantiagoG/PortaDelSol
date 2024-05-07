import streamlit as st
import pandas as pd
from datetime import datetime
from modules import conn


class Contracts:
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
                <h2>Contratos</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # col1, col2 = st.columns(2)
        # with col1:
        #     st.text_input("Search")
        # with col2:
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
            with st.popover(label="Más+", use_container_width=False):
                tab1, tab2, tab3 = st.tabs(["Añadir", "Editar", "Borrar"])

                with tab1:
                    Contracts.add_contract()
                with tab2:
                    Contracts.edit_contract()
                with tab3:
                    Contracts.delete_contract()
        st.write("***")
        # st.dataframe(conn.Connections.query1(select_contracts))
        st.dataframe(conn.Select_All.Contratos(1), hide_index=True)

    def add_contract():
        try:
            contrato = Contracts.form(key="add", label="Añadir", disabled=False)
            if contrato:
                try:
                    # conn.Insert.Contrato(contrato)
                    st.success("Contrato Añadido")
                except:
                    st.warning(
                        "Contrato no se pudo Añadir.\nFavor intente mas tarde o notifique al departamento de I.T."
                    )
        except:
            pass

    def edit_contract():
        search_id = st.number_input(
            key="update_search_id", label="ID de Contrato", min_value=1, step=1
        )
        try:
            contrato = Contracts.form(
                key="edit",
                label="Editar",
                disabled=False,
                # default=conn.Select.Contrato(search_id),
            )
            if contrato:
                try:
                    # conn.Update.Contrato(contrato)
                    st.success("Contrato Actualizado")
                except:
                    st.warning(
                        "Contrato no se pudo Actualizar.\nFavor intente mas tarde o notifique al departamento de I.T."
                    )
        except:
            pass

    def delete_contract():
        search_id = st.number_input(
            key="delete_search_id", label="ID de Contrato", min_value=1, step=1
        )
        try:
            contrato = Contracts.form(key="delete", label="Eliminar", disabled=True)
            if contrato:
                try:
                    # conn.Delete.Contrato(contrato)
                    st.success("Contrato Eliminado")
                except:
                    st.warning(
                        "Contrato no se pudo Eliminado.\nFavor intente mas tarde o notifique al departamento de I.T."
                    )
        except:
            pass

    def form(key: str, label: str, disabled: bool, default: dict = None):
        Detalles_Servicios = [
            "Embalming service for preservation of the deceased",
            "Viewing service for family and friends to pay respects",
            "Design and printing of personalized funeral programs",
            "Arrangement of floral displays for the funeral service",
            "Production of a memorial video to honor the deceased",
            "Handcrafted wooden urn with floral engravings",
            "Marble urn with intricate designs",
            "Brass urn with personalized inscription",
            "Ceramic urn with hand-painted motif",
            "Biodegradable urn made from eco-friendly materials",
            "Traditional coffin made from solid wood",
            "Casket with plush interior lining",
            "Steel coffin with reinforced structure",
            "Cardboard coffin with biodegradable lining",
            "Wicker coffin with natural finish",
            "Fiberglass coffin with sleek modern design",
            "Eco-friendly coffin made from sustainable materials",
            "Glass coffin for a unique display",
            "Customized coffin tailored to specific preferences",
            "Vintage-style coffin with ornate details",
            "Metallic coffin with polished finish",
            "Wooden coffin crafted from high-quality timber",
            "Pine coffin with minimalist design",
            "Mahogany coffin with rich, dark finish",
            "Bamboo coffin with eco-conscious construction",
        ]
        Parentesco = [
            "",
            "Madre",
            "Padre",
            "Hijo/a",
            "Abuelo/a",
            "Bisabuelo/a",
            "Tatarabuelo/a",
            "Sobrino/a",
            "Primo/a",
            "Tio/a",
            "Orto",
        ]
        Pago_Metodos = [
            "",
            "Efectivo",
            "Cheque",
            "Tarjeta - Credito",
            "Tarjeta - Debito",
        ]

        with st.form(key=key, clear_on_submit=False, border=False):
            col1, col2 = st.columns(2)
            with col1:
                Empleado_ID = st.selectbox(
                    label="Empleado",
                    key=key + "Empleado_ID",
                    disabled=disabled,
                    options=conn.Select_All.Empleados(1),
                    index=(
                        default["Empleado_ID"]
                        if default and "Empleado_ID" in default
                        else None
                    ),
                )
                Cliente_ID = st.selectbox(
                    label="Cliente",
                    key=key + "Cliente_ID",
                    disabled=disabled,
                    options=conn.Select_All.CLientes(1),
                    index=(
                        default["Cliente_ID"]
                        if default and "Cliente_ID" in default
                        else None
                    ),
                )
                Servicios = (
                    st.multiselect(
                        label="Servicios",
                        key=key + "Servicio_ID",
                        disabled=disabled,
                        options=conn.Select_All.Servicios(1),
                        default=(
                            default["Servicio_ID"]
                            if default and "Servicio_ID" in default
                            else []
                        ),
                    ),
                )
                Servicio_Detalles = st.text_input(
                    label="Detalles de servicios",
                    key=key + "Servicio_Detalles",
                    disabled=disabled,
                    placeholder="Detalles...",
                    value=(
                        default["Servicio_Detalles"]
                        if default and "Servicio_Detalles" in default
                        else ""
                    ),
                )
                Difunto_ID = st.selectbox(
                    label="Difunto",
                    key=key + "Difunto_ID",
                    disabled=disabled,
                    options=conn.Select_All.Difuntos(1),
                    index=(
                        default["Difunto_ID"]
                        if default and "Difunto_ID" in default
                        else None
                    ),
                )
                Certificado_Defuncion = st.selectbox(
                    label="Tipo de certificado de defunción",
                    key=key + "Certificado_Defuncion",
                    disabled=disabled,
                    options=[
                        "Certificado Estándar de Muerte",
                        "Certificado Coroner's de Muerte",
                    ],
                    index=(
                        default["Certificado_Defuncion"]
                        if default and "Certificado_Defuncion" in default
                        else 0
                    ),
                )
            with col2:
                Parentesco_Difunto = st.selectbox(
                    label="Parentesco",
                    key=key + "Parentesco_Difunto",
                    disabled=disabled,
                    options=Parentesco,
                    index=(
                        default["Certificado_Defuncion"]
                        if default and "Certificado_Defuncion" in default
                        else 0
                    ),
                )
                Fecha_Contrato_default = (
                    "today"
                    if not default or "Fecha_Contrato" not in default
                    else datetime.strptime(default["Fecha_Contrato"], "%Y-%m-%d").date()
                )
                Fecha_Contrato = st.date_input(
                    key=key + "Fecha_Contrato",
                    label="Fecha de Contrato",
                    min_value=None,
                    max_value=None,
                    disabled=disabled,
                    value=Fecha_Contrato_default,
                ).strftime("%Y-%m-%d")

                Fecha_Servicio_default = (
                    "today"
                    if not default or "Fecha_Servicio" not in default
                    else datetime.strptime(default["Fecha_Servicio"], "%Y-%m-%d").date()
                )
                Fecha_Servicio = st.date_input(
                    key=key + "Fecha_Servicio",
                    label="Fecha de Servicio",
                    min_value=None,
                    max_value=None,
                    disabled=disabled,
                    value=Fecha_Servicio_default,
                ).strftime("%Y-%m-%d")

                # Ensure default is not None and "Metodo_Pago" key exists
                if default and "Metodo_Pago" in default:
                    # Convert the value to an integer
                    try:
                        index = int(default["Metodo_Pago"])
                    except ValueError:
                        # Handle the case where the value cannot be converted to an integer
                        index = 0
                else:
                    index = 0

                # Pass the integer index to the selectbox
                Metodo_Pago = st.selectbox(
                    label="Metodo pago",
                    key=key + "Metodo_Pago",
                    disabled=disabled,
                    options=Pago_Metodos,
                    index=index,
                )

                Monto_Total = st.number_input(
                    label="Monto Total",
                    key=key + "Monto_Total",
                    step=0.01,
                    min_value=0.0,
                    disabled=disabled,
                    value=(
                        float(
                            default["Monto_Total"]
                        )  # Ensure default["Monto_Total"] is converted to float
                        if default and "Monto_Total" in default
                        else 0.0  # Ensure default value is a float
                    ),
                )
                Autorizacion_Cremacion = st.checkbox(
                    label="Autorizacion de cremacion",
                    key=key + "Autorizacion_Cremacion",
                    value=(
                        default["Autorizacion_Cremacion"]
                        if default and "Autorizacion_Cremacion" in default
                        else None
                    ),
                )
                Permiso_Cremacion = st.checkbox(
                    label="Permiso de cremacion",
                    key=key + "Permiso_Cremacion",
                    value=(
                        default["Permiso_Cremacion"]
                        if default and "Permiso_Cremacion" in default
                        else None
                    ),
                )

            if st.form_submit_button(
                label=label,
                use_container_width=True,
            ):
                # d = [item.split(":")[0] for item in Servicios]
                Contrato = {
                    "Empleado_ID": int(Empleado_ID.split(":")[0]),
                    "Cliente_ID": int(Cliente_ID.split(":")[0]),
                    "Difunto_ID": int(Difunto_ID.split(":")[0]),
                    "Parentesco_Difunto": Parentesco_Difunto,
                    "Fecha_Contrato": Fecha_Contrato,
                    "Fecha_Servicio": Fecha_Servicio,
                    "Metodo_Pago": Metodo_Pago,
                    "Monto_Total": Monto_Total,
                    "Certificado_Defuncion": Certificado_Defuncion,
                    "Autorizacion_Cremacion": Autorizacion_Cremacion,
                    "Permiso_Cremacion": Permiso_Cremacion,
                    "Servicios": Servicios,
                    "Servicio_Detalles": Servicio_Detalles,
                }

                # __________________________________
                # Documentos = {
                #     "Certificado_Defuncion": Certificado_Defuncion,
                #     "Autorizacion_Cremacion": Autorizacion_Cremacion,
                #     "Permiso_Cremacion": Permiso_Cremacion,
                # }
                # Servicios_Elegidos = {
                #     "Servicios": Servicios,
                #     "Servicio_Detalles": Servicio_Detalles,
                # }
                # Contrato = {
                #     "Empleado_ID": Empleado_ID.split(":")[0],
                #     "Cliente_ID": Cliente_ID.split(":")[0],
                #     "Servicios_Elegido_ID": Servicios_Elegido_ID,
                #     "Difunto_ID": Difunto_ID,
                #     "Documentos_ID": Documentos_ID,
                #     "Parentesco_Difunto": Parentesco_Difunto,
                #     "Fecha_Contrato": Fecha_Contrato,
                #     "Fecha_Servicio": Fecha_Servicio,
                #     "Metodo_Pago": Metodo_Pago,
                #     "Servicio_Detalles": Servicio_Detalles,
                #     "Monto_Total": Monto_Total,
                # }

                pass
