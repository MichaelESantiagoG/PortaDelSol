import streamlit as st
import pandas as pd

class Services:
    @staticmethod
    def view():
        header = """
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
                <h2>Servicios</h2>
            </div>
            """
        st.markdown(header, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            search = st.text_input(label="Buscar", placeholder="Buscar")
        with col2:
            services_add_container =  st.container()
            with services_add_container:
                st.markdown(
                    """
                    <style>
                    .stButton > button {
                    margin-top:10px; 
                    float:right;               
                    }
                    </style>

                    """,
                    unsafe_allow_html=True,
                )          
                if st.button(label="Más +", type="primary"): pass
                    # more_btn_session_state['more_opitions'] = not more_btn_session_state.get('more_opitions', False)
        # Crear el DataFrame con los datos de los servicios
        datos_servicios = {
            'Servicio': ['Cremación', 'Entierro tradicional', 'Funeral religioso', 'Servicio de urna', 'Pre-arreglos funerarios'],
            'Disponibilidad': ['Ofrecido', 'Ofrecido', 'Ofrecido', 'Por ofrecer', 'Por ofrecer'],
            'Precio': ['$1000', '$2000', '$1500', 'N/A', 'N/A'],
            'Duración': ['2 horas', '4 horas', '3 horas', 'N/A', 'N/A'],
            'Incluye': ['Urna básica', 'Ataúd, sala de velatorio', 'Servicio religioso', 'N/A', 'N/A']
        }

        # Replicar los datos 50 veces
        datos_repetidos = {k: v * 50 for k, v in datos_servicios.items()}

        # Crear el DataFrame con los datos repetidos
        df_servicios = pd.DataFrame(datos_repetidos)

        # Mostrar el DataFrame en Streamlit
        st.title('Servicios de la Funeraria')
        st.dataframe(df_servicios)

    