import streamlit as st
from multiapp import MultiApp
from apps import Kardex, administrativo, familia, terapeuta # import your app modules here
st.set_page_config(layout="wide")
app = MultiApp()

# Add all your application here
app.add_app("Terapeuta", terapeuta.app)          
app.add_app("Alumno/Familia", familia.app)
app.add_app("Administrativo", administrativo.app)
app.add_app("Kardex KPIs", Kardex.app)

# The main app
app.run()