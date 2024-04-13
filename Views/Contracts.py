import streamlit as st
import pandas as pd
from modules import conn

select_contracts="""
SELECT [Contrato_ID]
      ,[Empleado_ID]
      ,[Cliente_ID]
      ,[Difunto_ID]
  FROM [dbo].[Contratos]"""

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
            </style>
            <div class="middle-center">
                <h1>Porta del Sol</h1>
                <h2>Contratos</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
        data = {
            "Num. Contrato": [8672, 9647, 8934, 5514, 1257],
            "Documentos EG": ["Procesados", "Procesando", "No Proesados", "Procesados", "Procesados"],
            "Cliente": ["Eduardo G. Martinez", "Gabriel Ramirez", "Antonia Lopez", "José Rodriguez", "Carlos Sanrtana"],
            "Descripcion": ["Su Pre-Arreglo Funebre", "Arreglo Funebre Familiar Fallecido", "Su Pre-Arreglo Funebre", "Arreglo Funebre Familiar Fallecido", "Arreglo Funebre Familiar Fallecido"],
            "Servicios Solicitados": ["Cremación", "Velatorio Funebre", "Cremación", "Cremación", "Velatorio Funebre"],
            "Empleados Asignados": [2, 8, 2, 2, 5]
        }

        col1, col2 = st.columns(2)
        with col1: st.text_input('Search')
        with col2:
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

                    with tab1:pass
                    with tab2:pass
                    with tab3:pass
        st.write('***')
        #st.dataframe(conn.Connections.query1(select_contracts))
        st.dataframe(data)
