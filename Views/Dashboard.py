import streamlit as st
import pandas as pd
import numpy as np


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
        col1.metric("Ingreso", f"${400}")  # La suma de los montos totales
        col2.metric("Wind", "9 mph", "-8%")  # count de certificados de defuncion
        col3.metric("Humidity", "86%", "4%")  # count de contratos

        df1 = pd.DataFrame(
            np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
        )

        my_table = st.table(df1)

        df2 = pd.DataFrame(
            np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
        )

        my_table.add_rows(df2)
        my_chart = st.line_chart(df1)
        # my_chart.add_rows(df2)
        # my_chart = (
        #     st.vega_lite_chart(
        #         {
        #             "mark": "line",
        #             "encoding": {"x": "a", "y": "b"},
        #             "datasets": {
        #                 "some_fancy_name": df1,  # <-- named dataset
        #             },
        #             "data": {"name": "some_fancy_name"},
        #         }
        #     ),
        # )
        # my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword

        # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        # st.line_chart(chart_data)

        # df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
        # st.dataframe(df)
