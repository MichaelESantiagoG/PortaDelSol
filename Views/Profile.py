import streamlit as st

class Profile:
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
                <h2>Perfil</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.container():
            st.markdown(
                """
                <style>
                .stButton > button {
                    display: block;
                }
                .st-emotion-cache-r421ms {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: calc(1em - 1px);
                    width: 70%;
                    margin: 0 auto; /* Center horizontally */
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
            with st.form(key="profile", clear_on_submit=True):
                col1,col2 = st.columns(2)
                with col1:
                    first_name = st.text_input(label="Nombre")
                    email = st.text_input(label="Correo")

                with col2:
                    last_name = st.text_input(label="Apellidos")
                    phone = st.text_input(label="Telefono")
  
                address = st.text_input(label="Dirección")
                col1,col2 = st.columns(2)
                with col1:
                    username = st.text_input(label="Usuario")
                    start_date = st.date_input(label="Fecha de comienzo")
                with col2:
                    password = st.text_input(label="Contraseña",type="password")
                    end_date = st.date_input(label="End Date")
                if st.form_submit_button(label="Actualizar",type="primary"): st.success('Perfil actualizado')
                pass