import streamlit as st

# import pandas as pd
# import xlwings as xw
# import plotly.graph_objects as go #Libreria que permite hacer grafica datos mas complejos o elaborados. Permite personalizar los gráficos.

about_page = st.Page(
    page = 'pages/Inicio.py',
    title='Inicio',
    icon=':material/home:',
    default=True
)
app_1_page = st.Page(
    page = 'pages/DataSet.py',
    title='1_._Cargar_DataSet_de_parámetros_de_perforación',
    icon=':material/upload:'
)
app_2_page = st.Page(
    page = 'pages/Input_Data.py',
    title='2_._Datos_de_entrada_para_hidraulica',
    icon=':material/input:'
)
app_3_page = st.Page(
    page = 'pages/Pressure_Analysis.py',
    title='3_._Análisis_de_presión_de_perforación',
    icon=':material/play_arrow:'
)
app_4_page = st.Page(
    page = 'pages/pressure_simulation.py',
    title='4_._Simulación_de_presiones_de_perforación',
    icon=':material/play_arrow:'
)
# --- navigation setup [without sections] ---
# pg = st.navigation(pages=[about_page,app_1_page,app_2_page,app_3_page,app_4_page])
pg = st.navigation(
    {
        'Info':[about_page],
        'APP':[app_1_page,app_2_page,app_3_page,app_4_page]
    }
)

# --- shared on all pages ---
st.sidebar.text('Made by Joaquín Martínez')
# --- run navigation ---
pg.run()






# print('hola')
# # if "load" not in st.session_state:
# #      st.session_state.load = False

# # col1, col2 = st.columns([2,1])
# st.markdown('# DRILLING PRESSURE')
# st.markdown('## :blue[Drilling Pressure es una aplicación web que permite analizar la presión de perforación de pozos de crudo o gas mediante un gráfico interactivo o simular presiones de perforación :chart_with_upwards_trend:.]')

# datos = col2.file_uploader('Carga tu archivo . xlsx de datos de perforación aquí :point_down:')
# print('hola')

# if datos is not None:
#     df = pd.read_excel(datos)
#     # st.dataframe(df,hide_index=True)
#     dfl = len(df['MD'])# Calculamos y almacenamos el valor de la longitud de la serie MD del df en la variable dfl.
#     mdmin = df['MD'].min()
#     mdmax = df['MD'].max()

#     # Bloque de codigo que lee el nombre de las columnas de un df y los almacena en una lista.
#     coldf = []
#     for i in df:
#         coldf.append(i)
#     #print(coldf)

#     # Función que verifica si un dato está en una lista.
#     def check (ncol, list):
#         if ncol in list:
#             return True
#         else:
#             return False

#     # Lista con la información que debe tener la data para poder analizarla y generar el grafico.
#     colnec = ['MD','SPP','CAUDAL','MW']
#     conta = 0 

#     def main():
       
#         placeholder = st.empty()
#         with placeholder.form('cargar'):
#             st.markdown('El archivo de datos no contiene el parametro "MW", ingrese esa información:')
#             mw = st.number_input("Ingrese el valor del peso del lodo (MW): ")
#             mdin = int(st.number_input(f"Ingrese el valor de profundidad donde empieza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : "))
#             mdfi = int(st.number_input(f"Ingrese el valor de profundidad donde finaliza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : "))
#             st.markdown("Si quiere cargar mas información de peso de lodo (MW), escriba la información y oprima ¡Cargar información!. Si no desea cargar mas información marque la casilla finalizar y prima el boton!!! ")
#             checkbox_val = st.checkbox("Finalizar!!!")
#             load = st.form_submit_button('¡cargar infomación!')
#             # st.dataframe(df,hide_index=True)
#         if load or st.session_state.load:
#         # if load:
#             st.session_state.load = True
#             com1 = mdin >= mdmin
#             com2 = mdin <= mdmax
#             com3 = mdfi <= mdmax
#             com4 = mdfi >= mdmin
#             if com1 & com2 == False:
#                 st.warning(f"Ingrese el valor de profundidad donde empieza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : ")
#                 print(load)
#                 st.stop()
#             if com3 & com4 == False:
#                 st.warning(f"Ingrese el valor de profundidad donde finaliza este peso de lodo (El valor debe estar en este rango: {mdmin} y {mdmax}) : ")
#                 print(load)
#                 st.stop()
#             df.set_index("MD", inplace=True)# cambiamos el indice del df que se generó por defecto en pandas por uno presonalizado que en este caso va a ser "DEPTH"
#             for i in range (mdin,mdfi+1):# iteración que permite guardar en el df los datos solicitados anteriormente.
#                 df.at[i,'MW'] = mw # Almacena en una celda especifica del df el dato mw.
#             if checkbox_val:
#                 placeholder.empty()
#                 # st.markdown('La información se registró correctamente, desea registrar más información (Y/N):')
            
#             # st.dataframe(df,hide_index=True)
        
#         return [mw,mdin,mdfi,load,checkbox_val]
    
#     for j in colnec:
#         conta +=1
#         eval1 = j != "MW"
#         eval2 = check(j,coldf) == False
#         # consulta = check(i,coldf)
#         # if consulta == False:
#         if eval2 & eval1: # estructura de control que indica si el df no contiene la información necesaria.
#             # print(f'El dataframe no contiene los datos de {j}, por favor revise los datos de origen y vuelva a correr el programa.')
#             # break
#             col1.markdown(f':warning: El archivo de datos no contiene el parametro {j}, por favor revise el archivo de datos y vuelva a cargarlo.')
#             col1.markdown(f'Los parámetros de perforación necesarios que debe tener el archivo de datos para poder genarar el análisis y gráfico son: :red[{colnec}].')
#             break
        
#         if check(j,coldf) == False: # Si el df no tiene la información del parámetro "MW", lo informa y solicita que ingrese esa información.
#                 # col1.markdown('El archivo de datos no contiene el parametro "MW", ingrese esa información:')
        
#                 # with st.form('cargar'):
#                 #     mw = st.number_input("Ingrese el valor del peso del lodo: ")
#                 #     mdin = st.number_input(f"Ingrese el valor de profundidad donde empieza este peso de lodo (este valor debe estar en este rango: {mdmin} y {mdmax}) : ")
#                 #     mdfi = st.number_input(f"Ingrese el valor de profundidad donde finaliza este peso de lodo (este valor debe estar en este rango: {mdmin} y {mdmax}) : ")
#                 #     cargar = st.form_submit_button('¡Registrar infomación!')

               
#                 mw1, mdin1, mdfi1, cargar, casilla = main()
#                 print(df)
#                 if casilla:
#                     st.markdown('Gracias por cargar la información, a continuación se analizará los datos y se generará el gráfico!!')
#                     df.reset_index(inplace=True)
                
#                     wb = xw.Book('D:\Cursos\Analisis de datos y graficos con python\TGT REPORTE DIARIO INGENIERIA 03 QUIFA 931H 24-04-2023.xlsx')
#                     ws = wb.sheets['REP ING 1']
#                     for i in range(0,dfl):
#                         ws['G6'].value = df.at[i,"MD"]
#                         ws['D22'].value = df.at[i,"CAUDAL"]
#                         ws['C224'].value = df.at[i,"MW"]
#                         df.at[i,'SPPT'] = ws['D215'].value
#                     for j in range(0,dfl):
#                         df.at[j,'SPPT5%+']  = df.at[j,'SPPT']*5/100 + df.at[j,'SPPT']
#                         df.at[j,'SPPT5%-']  = df.at[j,'SPPT'] - df.at[j,'SPPT']*5/100
                    
#                     fig = go.Figure() #Crea el objeto figura.
#                     fig.add_trace(go.Scatter(x=df.MD, y=df['SPPT'],name = 'SPPT',mode='lines', line_color='indigo'))# Se agrega una linea a la figura, donde se le da un nombre a la linea y se personaliza
#                     fig.add_trace(go.Scatter(x=df.MD, y=df['SPPT5%+'],name = 'SPPT5%+', line=dict(color='royalblue', width=4,dash='dash'),fill='tonexty'))
#                     fig.add_trace(go.Scatter(x=df.MD, y=df['SPPT'],name = 'SPPT',mode='lines', line_color='indigo',showlegend=False))
#                     fig.add_trace(go.Scatter(x=df.MD, y=df['SPPT5%-'],name = 'SPPT5%-', line=dict(color='royalblue', width=4,dash='dash'),fill='tonexty'))
#                     fig.add_trace(go.Scatter(x=df.MD, y=df.SPP,name = 'SPP',mode='lines', line_color='green'))
#                     fig.update_layout(title='Análisis de presión de operación', xaxis_title='Depth(ft)', yaxis_title='Presión(psi)',template='plotly_white')
#                     fig.show() 
                    
#                     even = st.plotly_chart(fig)

#                 print(mw1, mdin1, mdfi1, cargar)
#                 print(st.session_state.load)

                # if cargar1 == True:
                #   com1 = mdin1 >= mdmin
                #   com2 = mdin1 <= mdmax
                #   com3 = mdfi1 <= mdmax
                #   com4 = mdfi1 >= mdmin
                #   if com1 & com2 == False:
                #     st.warning(f"Ingrese el valor de profundidad donde empieza este peso de lodo (este valor debe estar en este rango: {mdmin} y {mdmax}) : ")
                #     st.stop()
                #   if com3 & com4 == False:
                #     st.warning(f"Ingrese el valor de profundidad donde finaliza este peso de lodo (este valor debe estar en este rango: {mdmin} y {mdmax}) : ")
                #     st.stop()

                
                # df.set_index("MD", inplace=True)# cambiamos el indice del df que se generó por defecto en pandas por uno presonalizado que en este caso va a ser "DEPTH"
                # for i in range (mdin1,mdfi1+1):# iteración que permite guardar en el df los datos solicitados anteriormente.
                #     df.at[i,'MW'] = mw1 # Almacena en una celda especifica del df el dato mw.
               

                    
                  

        # if conta == 4:
        #     col1.markdown('La información del dataframe está completa, a continuación se analizaran los datos y se generará la gráfica de correlación de presiones')

    # with st.expander("Visualizar Archivo de Datos"):
    #     st.dataframe(df, hide_index=True)
