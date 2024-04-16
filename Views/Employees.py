import streamlit as st
import pandas as pd
from modules import conn
from datetime import datetime

# select_employees = """
#     SELECT [Empleado_ID]
#         ,[Nombre]
#         ,[Apellido_Paterno]
#         ,[Apellido_Materno]
#         ,[Celular]
#         ,[Celular_2]
#         ,[Direccion]
#         ,[Ocupacion]
#         ,[Seguro_Social]
#         ,[Correo_Electronico]
#         ,[Fecha_De_Nacimiento]
#         ,[Licencia]
#         ,[Estado_Civil]
#         ,[EstadoDeEmpleo]
#     FROM [Empleados]
#     """
# select_employee = """
# SELECT [Empleado_ID]
#         ,[Nombre]
#         ,[Apellido_Paterno]
#         ,[Apellido_Materno]
#         ,[Celular]
#         ,[Celular_2]
#         ,[Direccion]
#         ,[Ocupacion]
#         ,[Seguro_Social]
#         ,[Correo_Electronico]
#         ,[Fecha_De_Nacimiento]
#         ,[Licencia]
#         ,[Estado_Civil]
#         ,[EstadoDeEmpleo]
#     FROM [dbo].[Empleados]
#     WHERE [dbo].[Empleados].[Empleado_ID] = {}"""
# insert_employee = """
# INSERT INTO [dbo].[Empleados]
#            ([Nombre]
#            ,[Apellido_Paterno]
#            ,[Apellido_Materno]
#            ,[Celular]
#            ,[Celular_2]
#            ,[Direccion]
#            ,[Ocupacion]
#            ,[Seguro_Social]
#            ,[Correo_Electronico]
#            ,[Fecha_De_Nacimiento]
#            ,[Licencia]
#            ,[Estado_Civil]
#            ,[EstadoDeEmpleo])
#      VALUES
#            ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"""
# edit_employee = """"""
# delete_employee = """"""

select_employees = """SELECT * FROM Empleados;"""
select_employee = """SELECT * FROM Empleados WHERE Empleado_ID = {};"""
insert_employee = """
INSERT INTO Empleados (Nombre, Apellido_Paterno, Apellido_Materno, Celular, Celular_2, Direccion, Ocupacion, Seguro_Social, Correo_Electronico, Fecha_De_Nacimiento, Licencia, Estado_Civil, EstadoDeEmpleo)
VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"""
update_employee = """
UPDATE Empleados
SET Nombre = '{}',
    Apellido_Paterno = '{}',
    Apellido_Materno = '{}',
    Celular = '{}',
    Celular_2 = '{}',
    Direccion = '{}',
    Ocupacion = '{}',
    Seguro_Social = '{}',
    Correo_Electronico = '{}',
    Fecha_De_Nacimiento = '{}',
    Licencia = '{}',
    Estado_Civil = '{}',
    EstadoDeEmpleo = '{}'
WHERE Empleado_ID = {};"""
delete_employee = """DELETE FROM Empleados WHERE Empleado_ID = '{}'"""


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
            </style>
            <div class="middle-center">
                <h1>Porta del Sol</h1>
                <h2>Empleados</h2>
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
        st.dataframe(conn.query1(select_employees), hide_index=True)

    @staticmethod
    def add_employee_form():
        key, disabled = "add_employee", False
        with st.form(key=key, clear_on_submit=False, border=False):
            col1, col2 = st.columns(2)
            with col1:
                nombre = st.text_input(
                    key=key + "Nombre", label="Nombre", disabled=False
                )
                apellido_paterno = st.text_input(
                    key=key + "Apellido_Paterno",
                    label="Apellido Paterno",
                    disabled=disabled,
                )
                apellido_materno = st.text_input(
                    key=key + "Apellido_Materno",
                    label="Apellido Materno",
                    disabled=disabled,
                )
                celular = st.text_input(
                    key=key + "Celular",
                    label="Celular",
                    disabled=disabled,
                )
                celular_2 = st.text_input(
                    key=key + "Celular_2",
                    label="Celular 2",
                    disabled=disabled,
                )
                direccion = st.text_input(
                    key=key + "Direccion",
                    label="Direccion",
                    disabled=disabled,
                )
                ocupacion = st.text_input(
                    key=key + "Ocupacion",
                    label="Ocupacion",
                    disabled=disabled,
                )
            with col2:
                seguro_social = st.text_input(
                    key=key + "Seguro_Social",
                    label="Seguro Social",
                    disabled=disabled,
                )
                correo_electronico = st.text_input(
                    key=key + "Correo_Electronico",
                    label="Correo Electronico",
                    disabled=disabled,
                )
                fecha_de_nacimiento = st.date_input(
                    key=key + "Fecha_De_Nacimiento",
                    label="Fecha de Nacimiento",
                    min_value=None,
                    max_value=None,
                    disabled=disabled,
                ).strftime("%Y-%m-%d")
                licencia = st.text_input(
                    key=key + "Licencia",
                    label="Licencia",
                    disabled=disabled,
                )
                estado_civil = st.text_input(
                    key=key + "Estado_Civil",
                    label="Estado Civil",
                    disabled=disabled,
                )
                estado_de_empleo = st.selectbox(
                    key=key + "EstadoDeEmpleo",
                    label="Estado de Empleo",
                    options=["Activo", "Inactivo"],
                    disabled=disabled,
                )

            if st.form_submit_button(
                label="Añadir", type="secondary", use_container_width=True
            ):
                try:
                    query = insert_employee.format(
                        nombre,
                        apellido_paterno,
                        apellido_materno,
                        celular,
                        celular_2,
                        direccion,
                        ocupacion,
                        seguro_social,
                        correo_electronico,
                        fecha_de_nacimiento,
                        licencia,
                        estado_civil,
                        estado_de_empleo,
                    )
                    conn.query2(query=query)
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
                    nombre = st.text_input(
                        key=key + "Nombre",
                        label="Nombre",
                        disabled=disabled,
                        value=employee_info["Nombre"],
                    )
                    apellido_paterno = st.text_input(
                        key=key + "Apellido_Paterno",
                        label="Apellido Paterno",
                        disabled=disabled,
                        value=employee_info["Apellido_Paterno"],
                    )
                    apellido_materno = st.text_input(
                        key=key + "Apellido_Materno",
                        label="Apellido Materno",
                        disabled=disabled,
                        value=employee_info["Apellido_Materno"],
                    )
                    celular = st.text_input(
                        key=key + "Celular",
                        label="Celular",
                        disabled=disabled,
                        value=employee_info["Celular"],
                    )
                    celular_2 = st.text_input(
                        key=key + "Celular_2",
                        label="Celular 2",
                        disabled=disabled,
                        value=employee_info["Celular_2"],
                    )
                    direccion = st.text_input(
                        key=key + "Direccion",
                        label="Direccion",
                        disabled=disabled,
                        value=employee_info["Direccion"],
                    )
                    ocupacion = st.text_input(
                        key=key + "Ocupacion",
                        label="Ocupacion",
                        disabled=disabled,
                        value=employee_info["Ocupacion"],
                    )
                with col2:
                    seguro_social = st.text_input(
                        key=key + "Seguro_Social",
                        label="Seguro Social",
                        disabled=disabled,
                        value=employee_info["Seguro_Social"],
                    )
                    correo_electronico = st.text_input(
                        key=key + "Correo_Electronico",
                        label="Correo Electronico",
                        disabled=disabled,
                        value=employee_info["Correo_Electronico"],
                    )
                    date_obj = datetime.strptime(
                        employee_info["Fecha_De_Nacimiento"], "%Y-%m-%d"
                    ).date()
                    fecha_de_nacimiento = st.date_input(
                        key=key + "Fecha_De_Nacimiento",
                        label="Fecha de Nacimiento",
                        min_value=None,
                        max_value=None,
                        disabled=disabled,
                        value=date_obj,
                    )
                    licencia = st.text_input(
                        key=key + "Licencia",
                        label="Licencia",
                        disabled=disabled,
                        value=employee_info["Licencia"],
                    )
                    estado_civil = st.text_input(
                        key=key + "Estado_Civil",
                        label="Estado Civil",
                        disabled=disabled,
                        value=employee_info["Estado_Civil"],
                    )
                    estado_de_empleo = st.selectbox(
                        key=key + "EstadoDeEmpleo",
                        label="Estado de Empleo",
                        disabled=disabled,
                        options=["Activo", "Inactivo"],
                        index=0 if employee_info["EstadoDeEmpleo"] == "Activo" else 1,
                    )

                if st.form_submit_button(
                    label="Añadir", type="secondary", use_container_width=True
                ):
                    try:
                        query = update_employee.format(
                            nombre,
                            apellido_paterno,
                            apellido_materno,
                            celular,
                            celular_2,
                            direccion,
                            ocupacion,
                            seguro_social,
                            correo_electronico,
                            fecha_de_nacimiento,
                            licencia,
                            estado_civil,
                            estado_de_empleo,
                            search_id,
                        )
                        conn.query2(query=query)
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
                    nombre = st.text_input(
                        key=key + "Nombre",
                        label="Nombre",
                        disabled=disabled,
                        value=employee_info["Nombre"],
                    )
                    apellido_paterno = st.text_input(
                        key=key + "Apellido_Paterno",
                        label="Apellido Paterno",
                        disabled=disabled,
                        value=employee_info["Apellido_Paterno"],
                    )
                    apellido_materno = st.text_input(
                        key=key + "Apellido_Materno",
                        label="Apellido Materno",
                        disabled=disabled,
                        value=employee_info["Apellido_Materno"],
                    )
                    celular = st.text_input(
                        key=key + "Celular",
                        label="Celular",
                        disabled=disabled,
                        value=employee_info["Celular"],
                    )
                    celular_2 = st.text_input(
                        key=key + "Celular_2",
                        label="Celular 2",
                        disabled=disabled,
                        value=employee_info["Celular_2"],
                    )
                    direccion = st.text_input(
                        key=key + "Direccion",
                        label="Direccion",
                        disabled=disabled,
                        value=employee_info["Direccion"],
                    )
                    ocupacion = st.text_input(
                        key=key + "Ocupacion",
                        label="Ocupacion",
                        disabled=disabled,
                        value=employee_info["Ocupacion"],
                    )
                with col2:
                    seguro_social = st.text_input(
                        key=key + "Seguro_Social",
                        label="Seguro Social",
                        disabled=disabled,
                        value=employee_info["Seguro_Social"],
                    )
                    correo_electronico = st.text_input(
                        key=key + "Correo_Electronico",
                        label="Correo Electronico",
                        disabled=disabled,
                        value=employee_info["Correo_Electronico"],
                    )
                    date_obj = datetime.strptime(
                        employee_info["Fecha_De_Nacimiento"], "%Y-%m-%d"
                    ).date()
                    fecha_de_nacimiento = st.date_input(
                        key=key + "Fecha_De_Nacimiento",
                        label="Fecha de Nacimiento",
                        min_value=None,
                        max_value=None,
                        disabled=disabled,
                        value=date_obj,
                    )
                    licencia = st.text_input(
                        key=key + "Licencia",
                        label="Licencia",
                        disabled=disabled,
                        value=employee_info["Licencia"],
                    )
                    estado_civil = st.text_input(
                        key=key + "Estado_Civil",
                        label="Estado Civil",
                        disabled=disabled,
                        value=employee_info["Estado_Civil"],
                    )
                    estado_de_empleo = st.selectbox(
                        key=key + "EstadoDeEmpleo",
                        label="Estado de Empleo",
                        disabled=disabled,
                        options=["Activo", "Inactivo"],
                        index=0 if employee_info["EstadoDeEmpleo"] == "Activo" else 1,
                    )

                if st.form_submit_button(
                    label="Añadir", type="secondary", use_container_width=True
                ):
                    try:
                        query = delete_employee.format(
                            search_id,
                        )
                        conn.query2(query=query)
                        st.success("Empleado Eliminado")
                    except:
                        st.warning("No se pudo eliminar el Empleado")
        else:
            st.warning("Empleado no existe")

        pass

    def select_employee(search_id):
        try:
            employee = conn.query1(select_employee.format(search_id))
            employee_info = {
                "Empleado_ID": employee.iloc[0, 0],  # row, column
                "Nombre": employee.iloc[0, 1],
                "Apellido_Paterno": employee.iloc[0, 2],
                "Apellido_Materno": employee.iloc[0, 3],
                "Celular": employee.iloc[0, 4],
                "Celular_2": employee.iloc[0, 5],
                "Direccion": employee.iloc[0, 6],
                "Ocupacion": employee.iloc[0, 7],
                "Seguro_Social": employee.iloc[0, 8],
                "Correo_Electronico": employee.iloc[0, 9],
                "Fecha_De_Nacimiento": employee.iloc[0, 10],
                "Licencia": employee.iloc[0, 11],
                "Estado_Civil": employee.iloc[0, 12],
                "EstadoDeEmpleo": employee.iloc[0, 13],
            }
            return employee_info
        except:
            return False
