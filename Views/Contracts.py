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
        st.write('***')
        st.dataframe(conn.Connections.query1(select_contracts))
