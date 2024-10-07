#---Este modulo de la aplicación permite importar o leer la información de un dataset en formato excel y almacenarla en una variable para manipular los datos, también examina el dataset y si falta información para realizar el análisis lo informa.----


# -- Bibliotecas---
import streamlit as st
import pandas as pd
import plotly.graph_objects as go



if "load" not in st.session_state:
     st.session_state.load = False
if "df" not in st.session_state:
     st.session_state.df = pd.DataFrame()
# if "datos" not in st.session_state:
#      st.session_state.datos = 0

# -- Lista que contiene la información que debe tener el Dataset para poder analizarlo y generar el grafico.--
colnec = ['MD','SPP','CAUDAL','MW','PV','YP','T3']


# --- importa, carga o lee dataset en formato excel y se almacena en una variable para poder manipular los datos------------
st.markdown('## :blue[DRILLING PRESSURE]')
st.markdown('#### :blue[Carga tu Dataset de datos de perforación en formato .xlsx aquí] :point_down:')
datos = st.file_uploader(f'Los parámetros de perforación necesarios que debe tener el archivo de datos para genarar el análisis y gráfico son: :red[{colnec}].')

# datos = col2.file_uploader('Carga tu archivo . xlsx de datos de perforación aquí :point_down:')
# print('hola')


# --- Si hay un dataset cargado, se ejecuta el codigo del condicional, este condicional se pone con el fin de evitar error en el programa cuando el codigo pide información del dataset y este no se ha cargado ---
if datos is not None:
    st.session_state.df = pd.read_excel(datos)
    # st.dataframe(df,hide_index=True)
    dfl = len(st.session_state.df['MD'])# Calculamos y almacenamos el valor de la longitud de la serie MD del df en la variable dfl.
    mdmin = st.session_state.df['MD'].min()
    mdmax = st.session_state.df['MD'].max()


# --- Bloque de codigo que lee el nombre de las columnas de un df y los almacena en una lista. ---
    coldf = []
    for i in st.session_state.df:
        coldf.append(i)
    print(coldf)


# --- funcion que indica que valores de una lista predeterminada estan en otra. ---
    def check_values (lista,lista_preestablecida):
        not_values = [] 
        for j in lista_preestablecida:
            print (j)
            if j in lista:
                continue
            else:
                not_values.append(j)
        return not_values
    
    
    len_lista = len(check_values(coldf,colnec))



    if len_lista > 1:
        st.write(f'El Dataset no contiene el o los parametros: :red[{check_values(coldf,colnec)}], Revise el Dataset y cárguelo nuevamente:')
    else:
        st.write('El Dataset contiene los parámetros necesarios :thumbsup:.')


with st.expander("Visualizar dataset de parametros de perforación"):
    st.dataframe(st.session_state.df, hide_index=True)