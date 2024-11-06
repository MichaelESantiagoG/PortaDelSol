import json
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit_option_menu as st_option_menu
from Views.Clients import Clients
from Views.Dashboard import Dashboard
from Views.Employees import Employees
from Views.Log_in import Login
from Views.Profile import Profile
<<<<<<< HEAD
from Views.Services import Services
=======
from Views.Services import Servicios
from Views.Contracts import Contracts
from Views.Deceased import Deceased
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3

initial_layout = "centered"
initial_sidebar_state = "collapsed"
header = """<h1 style="text-align: center;"><span style="color: Black;">Porta del Sol</span></h1><h4 style="text-align: center;"</h4>"""
footer = """<style>
.css-h5rgaw{
    visibility:hidden;
    } 
.ea3mdgi1{
    visibility:hidden;
}
.css-cio0dv{
    visibility:hidden;
}
.css-1vbd788{
    visibility:hidden;
}
.egzxvld2{
    visibility:hidden;
}
.egzxvld1{
    visibility:hidden;
}
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: ;
color: grey;
text-align: left;
margin-left: 50px;
}
</style>
<div class="footer">
<p>Made by CapyCorp. Solutions</a></p>
</div>

"""
access = []

<<<<<<< HEAD
@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
=======

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3

def main():
    st.set_page_config(
        page_title="Porta del Sol Memorial",
        page_icon="⚰️",
        layout=st.session_state.user["layout"],
        initial_sidebar_state=st.session_state.user["sidebar_state"],
    )

    with st.sidebar:
        st.title("Porta del Sol")
        navigation = st_option_menu.option_menu(
            menu_title="Menu",
            default_index=0,
<<<<<<< HEAD
            options=["Panel", "Servicios","Clientes", "Empleados", "Ajustes"],
            icons=["house", "card-list","people", "person-vcard", "gear"],
            menu_icon="menu-up",)
        lottie = load_lottiefile("Media/rip.json")
        st_lottie(lottie,key='loc')

        st.markdown("""<style>.stButton > button {display: block;margin: 10px auto;}""", unsafe_allow_html=True)
        if st.sidebar.button("Cerrar Sesión", use_container_width=True): Login.logout()

    if navigation == "Panel":
        Dashboard.view()
    elif navigation == "Servicios":
        Services.view()
    elif navigation == "Clientes":
        Clients.view()
    elif navigation == "Empleados":
        Employees.view()
    elif navigation == "Ajustes":
        Profile.view()
    pass
=======
            options=[
                "Panel",
                "Empleados",
                "Servicios",
                "Clientes",
                "Difuntos",
                "Contratos",
                "Ajustes",
            ],
            icons=[
                "house",
                "person-vcard",
                "card-list",
                "people",
                "person-wheelchair",
                "card-list",
                "gear",
            ],
            menu_icon="menu-up",
        )
        lottie = load_lottiefile("Media/rip.json")
        st_lottie(lottie, key="loc")

        st.markdown(
            """<style>.stButton > button {display: block;margin: 10px auto;}""",
            unsafe_allow_html=True,
        )
        if st.sidebar.button("Cerrar Sesión", use_container_width=True):
            Login.logout()

    if navigation == "Panel":
        router("/panel").view()
    elif navigation == "Servicios":
        router("/servicios").view()
    elif navigation == "Clientes":
        router("/clientes").view()
    elif navigation == "Difuntos":
        router("/difuntos").view()
    elif navigation == "Empleados":
        router("/empleados").view()
    elif navigation == "Ajustes":
        router("/ajustes").view()
    elif navigation == "Contratos":
        router("/contratos").view()


def router(app_path: str):
    component_to_return = None

    if app_path == "/panel":
        component_to_return = Dashboard
        st.query_params.path = "/panel"

    elif app_path == "/servicios":
        component_to_return = Servicios
        st.query_params.path = "/services"

    elif app_path == "/clientes":
        component_to_return = Clients
        st.query_params.path = "/clients"

    elif app_path == "/difuntos":
        component_to_return = Deceased
        st.query_params.path = "/difuntos"

    elif app_path == "/empleados":
        component_to_return = Employees
        st.query_params.path = "/employees"

    elif app_path == "/contratos":
        component_to_return = Contracts
        st.query_params.path = "/contratos"

    elif app_path == "/ajustes":
        component_to_return = Profile
        st.query_params.path = "/profile"

    else:
        # default, no path, go to Panel
        component_to_return = Dashboard
        st.query_params.path = "/panel"

    # todo validation for invalid
    return component_to_return
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3


if __name__ == "__main__":
    if "user" not in st.session_state:
        st.session_state.user = {
            "user": None,
            "access": None,
            "logged": False,
            "layout": initial_layout,
            "sidebar_state": initial_sidebar_state,
        }

    if st.session_state.user["logged"]:
        main()
    if not st.session_state.user["logged"]:
        st.markdown(header, unsafe_allow_html=True)
        st.markdown(footer, unsafe_allow_html=True)
<<<<<<< HEAD
        Login.view()
=======
        Login.view()
>>>>>>> a9c36b6ec9d3069dfa991d761b00a4ff2f2af9b3
