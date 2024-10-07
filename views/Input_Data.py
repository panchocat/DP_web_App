#--Librerias-----
import streamlit as st
import pandas as pd

from forms.Hole_profile import hole_profile
from forms.Pipe_profile import pipe_profile





# -------------- Settings -----------------------------
if 'counter' not in st.session_state:
    st.session_state.counter=0
if 'counter1' not in st.session_state:
    st.session_state.counter1=0
if 'dataframe1' not in st.session_state:
    st.session_state.dataframe1= pd.DataFrame(columns=['Name','Long(ft)','hole diameter(in)'], index=range(5))
if 'dataframe2' not in st.session_state:
    st.session_state.dataframe2= pd.DataFrame(columns=['Name','Long(ft)','Hole Diame(in)','O.D Tub(in)','I.D Tub(in)'], index=range(10))
if 'tfa' not in st.session_state:
    st.session_state.tfa=0
# if 'mw' not in st.session_state:
#     st.session_state.mw=0
# if 'pv' not in st.session_state:
#     st.session_state.pv=0
# if 'yp' not in st.session_state:
#     st.session_state.yp=0
# if 't3' not in st.session_state:
#     st.session_state.t3=0
# if 'q' not in st.session_state:
#     st.session_state.q=0
keys = ['counter','counter1','dataframe1']
keys_0 = ['counter','counter1','dataframe2','tfa']
#--------------------------------------------------


def limpiar_cache():
    for key in keys:
        del st.session_state[key]
def limpiar_cache_0():
    for key in keys_0:
        del st.session_state[key]      



@st.dialog('Perfil del pozo:')
def show_hole_profile_form():
    hole_profile()

@st.dialog('Perfil de la tuberia')
def show_pipe_profile_form():
    pipe_profile()
    


st.markdown('#### :blue[<div style="text-align: justify;">Para realizar análisis de presiones de perforación o simular presiónes de preforación, debe ingresar el estado mecánico del pozo (Perfil del pozo y perfil de la tuberia) que se perforó o se va a perforar:]', unsafe_allow_html=True)
if st.button('Cargar perfil del pozo'):
    show_hole_profile_form()
with st.expander("Visualizar Perfil del pozo"):
    st.dataframe(st.session_state.dataframe1, hide_index=True)
    st.markdown('###### Verifique la información que cargó, si hay algún error en esa información haga click en el boton REINICIAR para cargar los datos nuevamente!!!')
    st.button('¡¡Limpiar formulario!!', on_click=limpiar_cache)

if st.button('Cargar perfil de la tuberia'):
    show_pipe_profile_form()
with st.expander("Visualizar Perfil de la tuberia"):
    st.dataframe(st.session_state.dataframe2, hide_index=True)
    st.write(f'TFA = {st.session_state.tfa}')
    st.markdown('###### Verifique la información que cargó, si hay algún error en esa información haga click en el boton REINICIAR para cargar los datos nuevamente!!!')
    st.button('¡Limpiar formulario!', on_click=limpiar_cache_0)


# def limpiar_cache():
#     for key in keys:
#         del st.session_state[key]

# 


#--Bloque de codigo que crea formularios-----

# with st.expander("Perfil del pozo"):
#     with st.form('well_profile', clear_on_submit=True):
#         st.markdown('Ingrese las secciones que tiene el pozo desde superficie a fondo:')
#         Name = st.text_input("Nombre de la sección (ej. OH(open hole) or CSG(Casing)): ",value=None,placeholder=None)
#         long = st.number_input("Longitud de la sección (ft): ",value=None,placeholder="Type a number...")
#         Diam = st.number_input("Diametro de la sección (in): ",value=None,placeholder="Type a number...")
#         submit = st.form_submit_button('¡cargar infomación!')
#         final = st.form_submit_button('¡Finalizar!')
#     if submit:
#         # hole_profile = ['Name','hole diameter(in)','Long(ft)']#crea listas con los nombres de las columnas que van a tener los dataframes.
#         # dfhp = pd.DataFrame(columns=hole_profile, index=range(5))
#         st.session_state.dataframe1.loc[st.session_state.counter] = [Name,long,Diam]
#         st.session_state.counter += 1
#         # st.dataframe(st.session_state.dataframe1, hide_index=True)
#     if final:
#         # dfhp = st.session_state.dataframe1
#         # dfhp = dfhp.dropna()
#         st.session_state.dataframe1.dropna(inplace=True)
#         # st.session_state.counter = st.session_state
#     st.dataframe(st.session_state.dataframe1, hide_index=True)
        

        # st.markdown("Si quiere cargar mas información de peso de lodo (MW), escriba la información y oprima ¡Cargar información!. Si no desea cargar mas información marque la casilla finalizar y prima el boton!!! ")
        # checkbox_val = st.checkbox("Finalizar!!!")
        

# with st.expander("Componentes de la sarta de perforación"):
#     with st.form('string_profile', clear_on_submit=True):
#         st.markdown('Ingrese los componentes de la sarta de perforación desde superficie a fondo:')
#         Name = st.text_input("Nombre del componente (ej. DP(Drill pipe) or BHA(Bottom hole asembly)): ",placeholder=None)
#         Long = st.number_input("Longitud del componente (ft): ",value=None,placeholder="Type a number...")
#         O_D = st.number_input("Diametro Externo del componente (in): ",value=None,placeholder="Type a number...")
#         I_D = st.number_input("Diametro Interno del componente (in): ",value=None,placeholder="Type a number...")
#         tfa = st.number_input("TFA de la broca: ",value=None,placeholder="Type a number...")
#         submit = st.form_submit_button('¡cargar infomación!')
#         final = st.form_submit_button('¡Finalizar!')
#     if submit:
#         # hole_profile = ['Name','hole diameter(in)','Long(ft)']#crea listas con los nombres de las columnas que van a tener los dataframes.
#         # dfhp = pd.DataFrame(columns=hole_profile, index=range(5))
#         st.session_state.dataframe2.loc[st.session_state.counter1] = [Name,Long,0,O_D,I_D]
#         st.session_state.counter1 += 1
#         st.session_state.tfa=tfa
#         # st.dataframe(st.session_state.dataframe2, hide_index=True)
#     if final:
#         # dfpp = st.session_state.dataframe2
#         # dfpp = dfpp.dropna()
#         st.session_state.dataframe2.dropna(inplace=True)
#         # st.session_state.counter1 = st.session_state
#     st.dataframe(st.session_state.dataframe2, hide_index=True)
#     st.write(f'TFA = {st.session_state.tfa}')


# st.markdown('##### Si desea simular la presión de perforación a partir de un dataset de parametros de perforación, omita este formulario porque el dataset debe tener esta información')

# with st.expander("Información del lodo y caudal"):
#     with st.form('mud_a_bit', clear_on_submit=True):
#         st.markdown('Ingrese los componentes de la sarta de perforación desde superficie a fondo:')
#         mw = st.text_input("Peso del lodo MW (ppg): ",placeholder=None)
#         pv = st.number_input("Viscosidad Plastica PV: ",value=None,placeholder="Type a number...")
#         yp = st.number_input("Yield Point YP: ",value=None,placeholder="Type a number...")
#         t3 = st.number_input("Reologia TETA 3: ",value=None,placeholder="Type a number...")
#         q = st.number_input("Caudal (gpm): ",value=None,placeholder="Type a number...")
#         submit = st.form_submit_button('¡cargar infomación!')
#         final = st.form_submit_button('¡Finalizar!')
#     if submit:
#         st.session_state.mw=mw
#         st.session_state.pv=pv
#         st.session_state.yp=yp
#         st.session_state.t3=t3
#         st.session_state.q=q
#     # if final:
#     #     # dfpp = st.session_state.dataframe2
#     #     # dfpp = dfpp.dropna()
#     #     st.session_state.dataframe2.dropna(inplace=True)
#     #     # st.session_state.counter1 = st.session_state
#     st.write(f'MW = {st.session_state.mw}')
#     st.write(f'PV = {st.session_state.pv}')
#     st.write(f'YP = {st.session_state.yp}')
#     st.write(f'T3 = {st.session_state.t3}')
#     st.write(f'TFA = {st.session_state.q}')


# st.markdown('###### Verifique la información que cargó, si hay algún error en esa información oprima el boton REINICIAR para cargar los datos nuevamente!!!')
# # # reset = st.button('¡REINICIAR!')

# #--funcion creada para limpiar las variables creadas con el metodo session_state al comienzo del modulo--- 
# def limpiar_cache():
#     for key in keys:
#         del st.session_state[key]

# st.button('¡REINICIAR!', on_click=limpiar_cache)
# if reset:
#     st.session_state.dataframe1 = pd.DataFrame(columns=['Name','Long(ft)','hole diameter(in)'], index=range(5))
#     st.session_state.dataframe2= pd.DataFrame(columns=['Name','Long(ft)','O.D Tub(in)','I.D Tub(in)'], index=range(10))
#     st.session_state.counter = 0
# print(reset)
    
        # st.dataframe(df,hide_index=True)
# if load or st.session_state.load:
#     # if load:
#     st.session_state.load = True
#     com1 = mdin >= mdmin
#     com2 = mdin <= mdmax
#     com3 = mdfi <= mdmax
#     com4 = mdfi >= mdmin
#     if com1 & com2 == False:
#         st.warning(f"Ingrese el valor de profundidad donde empieza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : ")
#         print(load)
#         st.stop()
#     if com3 & com4 == False:
#         st.warning(f"Ingrese el valor de profundidad donde finaliza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : ")
#         print(load)
#         st.stop()
#     df.set_index("MD", inplace=True)# cambiamos el indice del df que se generó por defecto en pandas por uno presonalizado que en este caso va a ser "DEPTH"
#     for i in range (mdin,mdfi+1):# iteración que permite guardar en el df los datos solicitados anteriormente.
#         df.at[i,'MW'] = mw # Almacena en una celda especifica del df el dato mw.
#     if checkbox_val:
#         placeholder.empty()