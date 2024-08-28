# -- modulo principal de la aplicación que estructura la aplicación en paginas y las llama para que se ejecuten---

# --Bibliotecas---
import streamlit as st


# --- Bloque de codigo que almacena en una variable la configuración de cada pagina para que pueda ser llamada o innvocada desde st.navigation---
about_page = st.Page(
    page = 'views/Inicio.py',
    title='Inicio',
    icon=':material/home:',
    default=True
)
app_1_page = st.Page(
    page = 'views/DataSet.py',
    title='1_._Cargar_DataSet_de_parámetros_de_perforación',
    icon=':material/upload:'
)
app_2_page = st.Page(
    page = 'views/Input_Data.py',
    title='2_._Crear_estado_mecánico_del_pozo',
    icon=':material/input:'
)
app_3_page = st.Page(
    page = 'views/Pressure_Analysis.py',
    title='3_._Análisis_de_presión_de_perforación_basado_en_Dataset',
    icon=':material/play_arrow:'
)
app_4_page = st.Page(
    page = 'views/pressure_simulation.py',
    title='4_._Simulación_de_presión_de_perforación',
    icon=':material/play_arrow:'
)
# --- navigation setup ---
# pg = st.navigation(pages=[about_page,app_1_page,app_2_page,app_3_page,app_4_page])
pg = st.navigation(
    {
        'Info':[about_page],
        'APP':[app_1_page,app_2_page,app_3_page,app_4_page]
    }
)

# --- shared on all pages ---
st.sidebar.text('Made by Joaquín Martínez')
st.sidebar.image('assets/rig2.png',use_column_width=True)
st.logo("assets/dp_logo1.png")

# --- run navigation ---
pg.run()






