import streamlit as st


class Login:

    def __init__(self, pin) -> None:
        self.pin = pin

    @staticmethod
    def view():
        st.session_state.user["layout"] = "centered"
        st.markdown(
            """<h2 style="text-align: center;"> Iniciar sesión</h2> """,
            unsafe_allow_html=True,
        )
        with st.form("auth"):
            username = st.text_input(
                label="Username", max_chars=50, label_visibility="visible"
            )
            pin = st.text_input(
                label="Password",
                max_chars=4,
                type="password",
                label_visibility="visible",
            )
            if st.form_submit_button(
                label="Iniciar sesión", type="primary", use_container_width=True
            ):
                if Login.login(pin):
                    st.rerun()
                else:
                    st.warning(body="Acceso denegado", icon="⛔")

            st.markdown(
                """<p style="text-align: center;"><span style="color: #999999;"><a style="color: #999999; text-decoration: underline;" title="Recuperación de contraseña" href="mailto:?subject=Contraseña&amp;body=Hola, he olvidado mi contraseña">¿Olvidaste tu contraseña?</a></span></p>""",
                unsafe_allow_html=True,
            )
        pass

    def login(pin):
        if pin == "9999":
            st.session_state.user = {
                "user": "Admin",
                "access": 0,
                "logged": True,
                "layout": "wide",
                "sidebar_state": "expanded",
            }
            st.session_state.user["layout"] = "wide"
            st.session_state.user["sidebar_state"] = "expanded"
            return True

    def logout():
        st.session_state.clear()
        st.rerun()
