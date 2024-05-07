import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from modules import conn


class Dashboard:
    def view():
        # print ('this is path', st.query_params.get('path'))
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
                justify-content: center;
                align-items: center;
                height: 100%;
                padding-bottom: 50px;
            }
            </style>
            <div class="middle-center">
                <h1>Bienvenidos a Porta del Sol Memorial</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns(3)
        col1.metric(
            "Numero de Contratos",
            f"{conn.Select_All.Contratos(2)['Total_Contratos']}",
        )
        col2.metric(
            "Ganacias",
            "${:,.2f}".format(round(conn.Select_All.Contratos(3)["Revenue"], 2)),
        )
        col3.metric(
            "Empleados Activos",
            f"{conn.Select_All.Empleados(2)['Activos']}",
        )
        st.write("***")

        df = pd.DataFrame(conn.Select_All.Contratos(6))
        st.bar_chart(df.set_index("Mes"))
        with st.expander("Reporte Mensual de Ingreso Bruto"):
            st.table(df)
        # ____________________________________________________________________________________________________________________
        df1 = pd.DataFrame(
            pd.DataFrame(conn.Select_All.Contratos(7)),
            columns=["Mes", "Tipo_Servicio", "Cantidad_Servicios"],
        )

        # Crear un gráfico de barras
        fig, ax = plt.subplots(figsize=(20, 6))
        df1.pivot(
            index="Mes", columns="Tipo_Servicio", values="Cantidad_Servicios"
        ).plot(kind="bar", stacked=True, ax=ax)
        ax.set_xlabel("Mes")
        ax.set_ylabel("Cantidad de Servicios")
        ax.set_title("Cantidad de Servicios Seleccionados por Mes y Tipo de Servicio")
        st.pyplot(fig)
        with st.expander("Reporte Mensual de Servicios Elegidos"):
            st.table(df1)
