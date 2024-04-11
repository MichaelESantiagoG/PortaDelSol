import streamlit as st
import pandas as pd
from modules import conn


select_employees ="""
    SELECT [Empleado_ID]
        ,[Nombre]
        ,[Apellido_Paterno]
        ,[Apellido_Materno]
        ,[Celular]
        ,[Celular_2]
        ,[Direccion]
        ,[Ocupacion]
        ,[Seguro_Social]
        ,[Correo_Electronico]
        ,[Fecha_De_Nacimiento]
        ,[Licencia]
        ,[Estado_Civil]
        ,[EstadoDeEmpleo]
    FROM [dbo].[Empleados]
    """
select_employee="""
SELECT [Empleado_ID]
        ,[Nombre]
        ,[Apellido_Paterno]
        ,[Apellido_Materno]
        ,[Celular]
        ,[Celular_2]
        ,[Direccion]
        ,[Ocupacion]
        ,[Seguro_Social]
        ,[Correo_Electronico]
        ,[Fecha_De_Nacimiento]
        ,[Licencia]
        ,[Estado_Civil]
        ,[EstadoDeEmpleo]
    FROM [dbo].[Empleados]
    WHERE [dbo].[Empleados].[Empleado_ID] = {}"""
insert_employee="""
INSERT INTO [dbo].[Empleados]
           ([Nombre]
           ,[Apellido_Paterno]
           ,[Apellido_Materno]
           ,[Celular]
           ,[Celular_2]
           ,[Direccion]
           ,[Ocupacion]
           ,[Seguro_Social]
           ,[Correo_Electronico]
           ,[Fecha_De_Nacimiento]
           ,[Licencia]
           ,[Estado_Civil]
           ,[EstadoDeEmpleo])
     VALUES
           ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"""
edit_employee=""""""
delete_employee=""""""

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
                    .st-emotion-cache-1i4zmrw{
                        float:right;
                        margin-top: 13px;
                        }
                </style>

                """,
                unsafe_allow_html=True,
            )
            with st.popover(label="Más+", use_container_width=False):
                tab1, tab2, tab3 = st.tabs(["Añadir", "Editar", "Borrar"])

                with tab1:Employees.add_employee_form()
                with tab2:Employees.edit_employee_form()
                with tab3:Employees.delete_employee_form()

        st.write('***')
        st.dataframe(conn.Connections.query1(select_employees))

    @staticmethod
    def add_employee_form():
        key, disabled = 'add_employee', False
        with st.form(key=key, clear_on_submit=False, border=False):
            col1, col2 = st.columns(2)
            with col1:
                nombre = st.text_input(key=key+'Nombre', label="Nombre", disabled=False)
                apellido_paterno = st.text_input(key=key+'Apellido_Paterno', label="Apellido Paterno", disabled=False)
                apellido_materno = st.text_input(key=key+'Apellido_Materno', label="Apellido Materno", disabled=False)
                celular = st.text_input(key=key+'Celular', label="Celular", disabled=False)
                celular_2 = st.text_input(key=key+'Celular_2', label="Celular 2", disabled=False)
                direccion = st.text_input(key=key+'Direccion', label="Direccion", disabled=False)
                ocupacion = st.text_input(key=key+'Ocupacion', label="Ocupacion", disabled=False)
            with col2:
                seguro_social = st.text_input(key=key+'Seguro_Social', label="Seguro Social", disabled=False)
                correo_electronico = st.text_input(key=key+'Correo_Electronico', label="Correo Electronico", disabled=False)
                fecha_de_nacimiento = st.date_input(key=key+'Fecha_De_Nacimiento', label="Fecha de Nacimiento", min_value=None, max_value=None,disabled=False)
                licencia = st.text_input(key=key+'Licencia', label="Licencia", disabled=False)
                estado_civil = st.text_input(key=key+'Estado_Civil', label="Estado Civil", disabled=False)
                estado_de_empleo = st.selectbox(key=key+'EstadoDeEmpleo', label="Estado de Empleo", options=['Activo', 'Inactivo'], disabled=False)
            if st.form_submit_button(label="Añadir", type="secondary", use_container_width=True):
                try:
                    query = insert_employee.format(nombre, apellido_paterno, apellido_materno, celular,celular_2, direccion, ocupacion, seguro_social, correo_electronico, fecha_de_nacimiento,licencia, estado_civil, estado_de_empleo )
                    conn.Connections.query2(query=query)
                    st.success("Empleado añadido")

                except:
                    st.warning('Empleado NO se pudo añadir')

    def edit_employee_form():pass
    def delete_employee_form():pass
    def select_employee(search_id):pass