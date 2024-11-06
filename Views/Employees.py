import streamlit as st
<<<<<<< HEAD
import pandas as pd
import random
from faker import Faker

=======
from modules import conn
from datetime import datetime
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3

class Employees:
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
<<<<<<< HEAD
=======
            .st-fq {
                width: 500px;
            }
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
            </style>
            <div class="middle-center">
                <h1>Porta del Sol</h1>
                <h2>Empleados</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
<<<<<<< HEAD
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
                    </style>

                    """,
                    unsafe_allow_html=True,
                )          
                if st.button(label="Más +", type="primary"): pass
        fake = Faker()

        data = {
            "first_name": [fake.first_name() for _ in range(50)],
            "last_name": [fake.last_name() for _ in range(50)],
            "address": [fake.address().replace("\n", ", ") for _ in range(50)],
            "phone": [fake.phone_number() for _ in range(50)],
            "email": [fake.email() for _ in range(50)],
            "username": [fake.user_name() for _ in range(50)],
            "password": [fake.password() for _ in range(50)],
            "start_date": [
                fake.date_between(start_date="-1y", end_date="today") for _ in range(50)
            ],
            "end_date": [
                fake.date_between(start_date="today", end_date="+1y") for _ in range(50)
            ],
            "active": [random.choice([True, False]) for _ in range(50)],
        }

        df = pd.DataFrame(data)

        st.dataframe(df)
        pass

=======
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
                    Employees.add_employee_form()
                with tab2:
                    Employees.edit_employee_form()
                with tab3:
                    Employees.delete_employee_form()

        st.write("***")
        # st.dataframe(conn.Connections.query1(select_employees))
        st.dataframe(conn.Select_All.Empleados(), hide_index=True)

    def add_employee_form():
        key, disabled = "add_employee", False
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
                    label="Direccion",
                    disabled=disabled,
                )
                Estado_Civil = st.selectbox(
                    key=key + "Estado_Civil",
                    label="Estado Civil",
                    disabled=disabled,
                    options=["Soltero", "Casado", "Divorciado", "Viudo"],
                )

            with col2:
                Posicion = st.text_input(
                    key=key + "Posicion",
                    label="Posicion",
                    disabled=disabled,
                )
                Estado_Empleo = st.selectbox(
                    key=key + "Estado_Empleo",
                    label="Estado de Empleo",
                    options=["Activo", "Inactivo"],
                    disabled=disabled,
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
                    key=key + "Lugar_Nacimiento",
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
                    Empleado = {
                        "Posicion": Posicion,
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
                        "Estado_Empleo": Estado_Empleo,
                    }
                    conn.Insert.Empleado(Empleado)
                    st.success("Empleado añadido")

                except:
                    st.warning("Empleado NO se pudo añadir")

    def edit_employee_form():
        key, disabled = "update_employee", False

        search_id = st.number_input(
            key=key + "search_id", label="ID del Empleado", min_value=0, step=1
        )
        employee_info = Employees.select_employee(search_id)
        if employee_info:
            with st.form(key=key, clear_on_submit=False, border=False):
                col1, col2 = st.columns(2)
                with col1:
                    Nombre = st.text_input(
                        key=key + "Nombre",
                        label="Nombre",
                        disabled=disabled,
                        value=employee_info["Nombre"],
                    )
                    Apellido_Paterno = st.text_input(
                        key=key + "Apellido_Paterno",
                        label="Apellido Paterno",
                        disabled=disabled,
                        value=employee_info["Apellido_Paterno"],
                    )
                    Apellido_Materno = st.text_input(
                        key=key + "Apellido_Materno",
                        label="Apellido Materno",
                        disabled=disabled,
                        value=employee_info["Apellido_Materno"],
                    )
                    Genero = st.selectbox(
                        key=key + "Genero",
                        label="Género",
                        options=["Masculino", "Femenino"],
                        disabled=disabled,
                        index=0 if employee_info["Genero"] == "Masculino" else 1,
                    )
                    Celular = st.text_input(
                        key=key + "Celular",
                        label="Celular",
                        disabled=disabled,
                        value=employee_info["Celular"],
                    )
                    Celular_2 = st.text_input(
                        key=key + "Celular_2",
                        label="Celular 2",
                        disabled=disabled,
                        value=employee_info["Celular_2"],
                    )
                    Direccion = st.text_input(
                        key=key + "Direccion",
                        label="Direccion",
                        disabled=disabled,
                        value=employee_info["Direccion"],
                    )
                    # Define the options
                    options = ["Soltero", "Casado", "Divorciado", "Viudo"]

                    # Set the default index to None initially
                    default_index = None

                    # Check if the value from employee_info["Estado_Civil"] matches any option
                    if employee_info["Estado_Civil"] in options:
                        default_index = options.index(employee_info["Estado_Civil"])

                    # Create the select box with the correct default index
                    Estado_Civil = st.selectbox(
                        key=key + "Estado_Civil",
                        label="Estado Civil",
                        disabled=disabled,
                        options=options,
                        index=default_index,
                    )

                with col2:
                    Posicion = st.text_input(
                        key=key + "Posicion",
                        label="Posicion",
                        disabled=disabled,
                        value=employee_info["Posicion"],
                    )
                    Estado_Empleo = st.selectbox(
                        key=key + "Estado_Empleo",
                        label="Estado de Empleo",
                        options=["Activo", "Inactivo"],
                        disabled=disabled,
                        index=0 if employee_info["Estado_Empleo"] == "Activo" else 1,
                    )
                    Seguro_Social = st.text_input(
                        key=key + "Seguro_Social",
                        label="Seguro Social",
                        disabled=disabled,
                        value=employee_info["Seguro_Social"],
                    )
                    Correo_Electronico = st.text_input(
                        key=key + "Correo_Electronico",
                        label="Correo Electronico",
                        disabled=disabled,
                        value=employee_info["Correo_Electronico"],
                    )
                    date_obj = datetime.strptime(
                        employee_info["Fecha_Nacimiento"], "%Y-%m-%d"
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
                        key=key + "Lugar_Nacimiento",
                        label="Lugar de Nacimiento",
                        disabled=disabled,
                        value=employee_info["Lugar_Nacimiento"],
                    )
                    Licencia = st.text_input(
                        key=key + "Licencia",
                        label="Licencia",
                        disabled=disabled,
                        value=employee_info["Licencia"],
                    )
                    Servicio_Militar = st.text_input(
                        key=key + "Servicio_Militar",
                        label="Número de Servicio Militar",
                        disabled=disabled,
                        value=employee_info["Servicio_Militar"],
                    )

                if st.form_submit_button(
                    label="Editar", type="secondary", use_container_width=True
                ):
                    try:
                        Empleado = {
                            "Posicion": Posicion,
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
                            "Estado_Empleo": Estado_Empleo,
                        }
                        conn.Update.Empleado(id=search_id, data=Empleado)
                        st.success("Empleado Actualizado")
                    except:
                        st.warning("No se pudo actualizar el Empleado")
        else:
            st.warning("Empleado no existe")

    def delete_employee_form():
        key, disabled = "delete_employee", True

        search_id = st.number_input(
            key=key + "search_id", label="ID del Empleado", min_value=0, step=1
        )
        employee_info = Employees.select_employee(search_id)
        if employee_info:
            with st.form(key=key, clear_on_submit=False, border=False):
                col1, col2 = st.columns(2)
                with col1:
                    Nombre = st.text_input(
                        key=key + "Nombre",
                        label="Nombre",
                        disabled=disabled,
                        value=employee_info["Nombre"],
                    )
                    Apellido_Paterno = st.text_input(
                        key=key + "Apellido_Paterno",
                        label="Apellido Paterno",
                        disabled=disabled,
                        value=employee_info["Apellido_Paterno"],
                    )
                    Apellido_Materno = st.text_input(
                        key=key + "Apellido_Materno",
                        label="Apellido Materno",
                        disabled=disabled,
                        value=employee_info["Apellido_Materno"],
                    )
                    Genero = st.selectbox(
                        key=key + "Genero",
                        label="Género",
                        options=["Masculino", "Femenino"],
                        disabled=disabled,
                        index=0 if employee_info["Genero"] == "Masculino" else 1,
                    )
                    Celular = st.text_input(
                        key=key + "Celular",
                        label="Celular",
                        disabled=disabled,
                        value=employee_info["Celular"],
                    )
                    Celular_2 = st.text_input(
                        key=key + "Celular_2",
                        label="Celular 2",
                        disabled=disabled,
                        value=employee_info["Celular_2"],
                    )
                    Direccion = st.text_input(
                        key=key + "Direccion",
                        label="Direccion",
                        disabled=disabled,
                        value=employee_info["Direccion"],
                    )
                    # Define the options
                    options = ["Soltero", "Casado", "Divorciado", "Viudo"]

                    # Set the default index to None initially
                    default_index = None

                    # Check if the value from employee_info["Estado_Civil"] matches any option
                    if employee_info["Estado_Civil"] in options:
                        default_index = options.index(employee_info["Estado_Civil"])

                    # Create the select box with the correct default index
                    Estado_Civil = st.selectbox(
                        key=key + "Estado_Civil",
                        label="Estado Civil",
                        disabled=disabled,
                        options=options,
                        index=default_index,
                    )

                with col2:
                    Posicion = st.text_input(
                        key=key + "Posicion",
                        label="Posicion",
                        disabled=disabled,
                        value=employee_info["Posicion"],
                    )
                    Estado_Empleo = st.selectbox(
                        key=key + "Estado_Empleo",
                        label="Estado de Empleo",
                        options=["Activo", "Inactivo"],
                        disabled=disabled,
                        index=0 if employee_info["Estado_Empleo"] == "Activo" else 1,
                    )
                    Seguro_Social = st.text_input(
                        key=key + "Seguro_Social",
                        label="Seguro Social",
                        disabled=disabled,
                        value=employee_info["Seguro_Social"],
                    )
                    Correo_Electronico = st.text_input(
                        key=key + "Correo_Electronico",
                        label="Correo Electronico",
                        disabled=disabled,
                        value=employee_info["Correo_Electronico"],
                    )
                    date_obj = datetime.strptime(
                        employee_info["Fecha_Nacimiento"], "%Y-%m-%d"
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
                        key=key + "Lugar_Nacimiento",
                        label="Lugar de Nacimiento",
                        disabled=disabled,
                        value=employee_info["Lugar_Nacimiento"],
                    )
                    Licencia = st.text_input(
                        key=key + "Licencia",
                        label="Licencia",
                        disabled=disabled,
                        value=employee_info["Licencia"],
                    )
                    Servicio_Militar = st.text_input(
                        key=key + "Servicio_Militar",
                        label="Número de Servicio Militar",
                        disabled=disabled,
                        value=employee_info["Servicio_Militar"],
                    )

                if st.form_submit_button(
                    label="Eliminar", type="secondary", use_container_width=True
                ):
                    try:
                        conn.Delete.Empleado(search_id)
                        st.success("Empleado Eliminado")
                    except:
                        st.warning("No se pudo eliminar el Empleado")
        else:
            st.warning("Empleado no existe")

        pass

    def select_employee(id):
        try:
            employee_info = conn.Select.Empleado(id)
            employee_info1 = {
                "Empleado_ID": employee_info["Empleado_ID"],  # row, column
                "Posicion": employee_info["Posicion"],
                "Nombre": employee_info["Nombre"],
                "Apellido_Paterno": employee_info["Apellido_Paterno"],
                "Apellido_Materno": employee_info["Apellido_Materno"],
                "Genero": employee_info["Genero"],
                "Correo_Electronico": employee_info["Correo_Electronico"],
                "Celular": employee_info["Celular"],
                "Celular_2": employee_info["Celular_2"],
                "Direccion": employee_info["Direccion"],
                "Fecha_Nacimiento": employee_info["Fecha_Nacimiento"],
                "Lugar_Nacimiento": employee_info["Lugar_Nacimiento"],
                "Seguro_Social": employee_info["Seguro_Social"],
                "Licencia": employee_info["Licencia"],
                "Servicio_Militar": employee_info["Servicio_Militar"],
                "Estado_Civil": employee_info["Estado_Civil"],
                "Estado_Empleo": employee_info["Estado_Empleo"],
            }
            return employee_info1
        except:
            return False
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
