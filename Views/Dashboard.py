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

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.line_chart(chart_data)

        df = pd.read_csv(
            "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
        )
        st.dataframe(df)