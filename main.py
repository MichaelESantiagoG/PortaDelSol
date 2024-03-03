import streamlit as st
from views import *

initial_layout = "centered"
initial_sidebar_state = "collapsed"
header = """<h1 style="text-align: center;"><span style="color: #1A7BC1;">Porta del Sol</span></h1><h4 style="text-align: center;"</h4>"""
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
}
</style>
<div class="footer">
<p>Made by CapyCorp. Solutions</a></p>
</div>

"""

access = [0, 1]


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
            options=["Inicio", "Servicios","Clientes", "Empleados", "Ajustes"],
            icons=["house", "card-list","people", "person-vcard", "gear"],
            menu_icon="menu-up",
        )

    if navigation == "Inicio":
        Home.view()
    elif navigation == "Servicios":
        Services.view()
    elif navigation == "Clientes":
        Client.view()
    elif navigation == "Empleados":
        Employee.view()
    elif navigation == "Ajustes":
        Profile.view()
    pass


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
        Login.login()
