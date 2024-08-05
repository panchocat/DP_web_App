# import streamlit as st
# import pandas as pd
# import xlwings as xw

# st.markdown('# DRILLING PRESSURE')
# st.markdown('### Para realizar el grafico de analisis de presión de perforación necesita cargar el estado mecanico pozo :point_down:')

# placeholder = st.empty()
# with placeholder.form('cargar'):
#     st.markdown('El archivo de datos no contiene el parametro "MW", ingrese esa información:')
#     mw = st.number_input("Ingrese el valor del peso del lodo (MW): ")
#     mdin = int(st.number_input(f"Ingrese el valor de profundidad donde empieza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : "))
#     mdfi = int(st.number_input(f"Ingrese el valor de profundidad donde finaliza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : "))
#     st.markdown("Si quiere cargar mas información de peso de lodo (MW), escriba la información y oprima ¡Cargar información!. Si no desea cargar mas información marque la casilla finalizar y prima el boton!!! ")
#     checkbox_val = st.checkbox("Finalizar!!!")
#     load = st.form_submit_button('¡cargar infomación!')
#     # st.dataframe(df,hide_index=True)
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