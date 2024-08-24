import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import math
from forms.mud_data import mud_data
from forms.pump_rate import pump_rate
from forms.Depth import depth

if 'mw1' not in st.session_state:
    st.session_state.mw1=0
if 'pv1' not in st.session_state:
    st.session_state.pv1=0
if 'yp1' not in st.session_state:
    st.session_state.yp1=0
if 't31' not in st.session_state:
    st.session_state.t31=0
if 'q1' not in st.session_state:
    st.session_state.q1=0
if 'q2' not in st.session_state:
    st.session_state.q2=0
if 'q3' not in st.session_state:
    st.session_state.q3=0
if 'd1' not in st.session_state:
    st.session_state.d1=0
if 'd2' not in st.session_state:
    st.session_state.d2=0
if 'step' not in st.session_state:
    st.session_state.step=0
if 'lista_depth' not in st.session_state:
    st.session_state.lista_depth=[] 
if 'lista_q' not in st.session_state:
    st.session_state.lista_q = []
if 'df2' not in st.session_state:
    st.session_state.df2= pd.DataFrame(columns=['Depth(ft)','SPPT(psi)','ECD(ppg)','Down stk','Up stk'], index=range(12))
if 'df3' not in st.session_state:
    st.session_state.df3= pd.DataFrame(columns=['Depth(ft)','SPPT(psi)','ECD(ppg)','Down stk','Up stk'], index=range(12))
if 'df4' not in st.session_state:
    st.session_state.df4= pd.DataFrame(columns=['Depth(ft)','SPPT(psi)','ECD(ppg)','Down stk','Up stk'], index=range(12))
if 'dfem' not in st.session_state:
    st.session_state.dfem= pd.DataFrame(columns=['Vol Sarta(bbl)','Vol Anu(bbl)','Vel Anu(ft/min)','Vel Tub(ft/seg)','Viscosidad eff(tubing)','Viscosidad eff(anular)','Reynolds (anular)','Reynolds (tubing)','friction factor(tubing)','friction factor(anular)','loss press grad(tubing)','loss press grad(anular)','Vel Crit(ft/min)','Caud Crit(gpm)','Reg Flujo(anular)'], index=range(12))

# def check (ncol, list):
#     if ncol in list:
#         return True
#     else:
#         return False
keys1 = ['mw1','pv1','yp1','t31']
keys2 = ['q1','q2','q3']
keys3 = ['d1','d2','step']
def limpiar_cache_1():
    for key in keys1:
        del st.session_state[key]

def limpiar_cache_2():
    for key in keys2:
        del st.session_state[key]

def limpiar_cache_3():
    for key in keys3:
        del st.session_state[key]




@st.dialog('Ingrese la información del fluido de perforación:')
def show_mud_data_form():
    mud_data()

@st.dialog('Ingrese la información del caudal de trabajo:')
def show_pump_rate_form():
    pump_rate()

@st.dialog('Ingrese la profundidades en las que desea calcular las presiones simuladas:')
def show_depth_form():
    depth()


multi ='''##### :blue[Esta opción le permitira simular presiones de perforación para tener una idea de como puede ser el comportamiento de la presión de perforación durante la operación e identificar posibles anomalias en este parámetro.] 
Para usar esta opción debe seguir estos pasos:  
1- Completar la información solicitada en la opción (2) de esta aplicación.  
2- Ingresar los siguientes Datos y luego oprimir el botón ¡generar presiones simuladas!.'''
st.markdown(multi)

if st.button('Formulario datos de fluido de perforación'):
    show_mud_data_form()
with st.expander("Visualizar datos del fluido de perforación"):
    st.write(f'MW = {st.session_state.mw1}')
    st.write(f'PV = {st.session_state.pv1}')
    st.write(f'YP = {st.session_state.yp1}')
    st.write(f'T3 = {st.session_state.t31}')
    st.markdown('###### Verifique la información que cargó, si hay algún error en esa información oprima el boton REINICIAR para cargar los datos nuevamente!!!')
    st.button('¡¡Limpiar formulario!!...', on_click=limpiar_cache_1)

if st.button('Formulario datos de caudal'):
    show_pump_rate_form()
with st.expander("Visualizar datos de caudal"):
    st.markdown('Verifique la información que cargó, si hay algún error oprima el botón ¡Limpiar formulario! para cargar los datos nuevamente.')
    st.write(f'Caudal_1 = {st.session_state.q1}')
    st.write(f'Caudal_2  = {st.session_state.q2}')
    st.write(f'Caudal_3  = {st.session_state.q3}')
    st.markdown('###### Verifique la información que cargó, si hay algún error en esa información oprima el boton REINICIAR para cargar los datos nuevamente!!!')
    st.button('¡¡Limpiar formulario!!..', on_click=limpiar_cache_2)

if st.button('Formulario datos de pronfundidad'):
    show_depth_form()
with st.expander("Visualizar datos pronfundidas"):
    st.markdown('Verifique la información que cargó, si hay algún error oprima el botón ¡Limpiar formulario! para cargar los datos nuevamente.')
    st.write(f'Profundidad inicial = {st.session_state.d1}')
    st.write(f'profundidad final  = {st.session_state.d2}')
    st.write(f'Pasos  = {st.session_state.step}')
    st.markdown('###### Verifique la información que cargó, si hay algún error en esa información oprima el boton REINICIAR para cargar los datos nuevamente!!!')
    st.button('¡¡Limpiar formulario!!.', on_click=limpiar_cache_3)






# with st.expander('Input data fluido de perforación:'):
# #     with st.form('mud', clear_on_submit=True):
# #         # st.markdown('Ingrese la información en el formulario y luego oprima el boton cargar información:')
# #         mw1 = st.number_input("Peso de lodo MW (ppg): ",value=None,placeholder="Type a number...")
# #         pv1 = st.number_input("Viscosidad plastica PV (cp): ",value=None,placeholder="Type a number...")
# #         yp1 = st.number_input("Yield point YP (lbf/100ft**2): ",value=None,placeholder="Type a number...")
# #         t31 = st.number_input("Reologia TETA 3: ",value=None,placeholder="Type a number...")
# #         # q1 = st.number_input("Caudal 1 (gpm): ",value=None,placeholder="Type a number...")
# #         # q2 = st.number_input("Caudal 2 (gpm): ",value=None,placeholder="Type a number...")
# #         # q3 = st.number_input("Caudal 3 (gpm): ",value=None,placeholder="Type a number...")
# #         boton3 = st.form_submit_button('¡cargar infomación!')
# #     if boton3:
# #         lista = [mw1,pv1,yp1,t31]
# #         if None in lista:
# #             st.warning(f"Debe ingresar toda la información del formulario antes de oprimir el botón ¡cargar infomación!: ")
# #             st.stop()

# #         st.session_state.mw1 = mw1
# #         st.session_state.pv1 = pv1
# #         st.session_state.yp1 = yp1
# #         st.session_state.t31 = t31
# #         # st.session_state.q1 = q1
# #         # st.session_state.q2 = q2
# #         # st.session_state.q3 = q3

# #     st.markdown('Verifique la información que cargó, si hay algún error oprima el botón REINICIAR para cargar los datos nuevamente.')
# #     st.write(f'MW = {st.session_state.mw1}')
# #     st.write(f'PV = {st.session_state.pv1}')
# #     st.write(f'YP = {st.session_state.yp1}')
# #     st.write(f'T3 = {st.session_state.t31}')
# #     # st.write(f'Q1 = {st.session_state.q1}')
# #     # st.write(f'Q2= {st.session_state.q2}')
# #     # st.write(f'Q3 = {st.session_state.q3}')
# #     boton4 = st.button('¡Reiniciar!')

# # with st.expander('Pump rate:'):
# #         with st.form('caudales', clear_on_submit=True):
# #             st.markdown('Puede simular la presión de perforación para diferentes caudales de perforación:')
# #             q1 = st.number_input("Caudal 1 (gpm): ",value=None,placeholder="Type a number...")
# #             q2 = st.number_input("Caudal 2 (gpm): ",value=None,placeholder="Type a number...")
# #             q3 = st.number_input("Caudal 3 (gpm): ",value=None,placeholder="Type a number...")
# #             boton5 = st.form_submit_button('¡cargar infomación!')
# #             if boton3:
# #                 st.session_state.q1 = q1
# #                 st.session_state.q2 = q2
# #                 st.session_state.q3 = q3


# #         st.markdown('Verifique la información que cargó, si hay algún error oprima el botón REINICIAR para cargar los datos nuevamente.')
# #         st.write(f'Caudal 1 = {st.session_state.q1}')
# #         st.write(f'Caudal 2 = {st.session_state.q2}')
# #         st.write(f'Caudal 3 = {st.session_state.q3}')
           

# # with st.expander('Pronfundidad:'):
# #         with st.form('depth', clear_on_submit=True):
# #             st.markdown('Puede simular la presión de perforación para una profundidad puntual o para un rango de profundidad:')
# #             d1 = st.number_input("Profundidad inicial (ft): ",value=None,placeholder="Type a number...")
# #             d2 = st.number_input("Profundidad final (ft): ",value=None,placeholder="Type a number...")
# #             step = st.number_input("Pasos (generar presión de perforación cada 1 ft, 10ft etc...) (ft): ",value=None,placeholder="Type a number...")
# #             boton6 = st.form_submit_button('¡cargar infomación!')
# #             if boton3:
# #                 st.session_state.d1 = d1
# #                 st.session_state.d2 = d2
# #                 st.session_state.step = step


# #         st.markdown('Verifique la información que cargó, si hay algún error oprima el botón REINICIAR para cargar los datos nuevamente.')
# #         st.write(f'Caudal 1 = {st.session_state.d1}')
# #         st.write(f'Caudal 2 = {st.session_state.d2}')
# #         st.write(f'Caudal 3 = {st.session_state.step}')



# st.markdown('###### Verifique la información que cargó en cada formulario, si hay algún error en esa información oprima el boton REINICIAR para cargar los datos nuevamente!!!')

# -- Función que elimina vañores None de una lista --
def clear_list (a):
    while True:
        if None in a:
            for i in a:
                # print(i)
                if i == None:
                    a.remove(None)#metodo que permite eliminar el valor en una lista.
                    break
        else:
            break


if st.button('¡Generar presiones simuladas!'):
    clear_list(st.session_state.lista_q)
    clear_list(st.session_state.lista_depth)
    contador3 = 0
    lista_df = [st.session_state.df2,st.session_state.df3,st.session_state.df4]
    for m in (st.session_state.lista_q):
        df_lista = lista_df[contador3]

        if len(st.session_state.lista_depth)<=1:
                dfpp1 = st.session_state.dataframe2.copy(deep=True)
                mw=st.session_state.mw1
                pv =st.session_state.pv1
                yp=st.session_state.yp1
                t3=st.session_state.t31
                tfa= st.session_state.tfa
                Q=m
                # mw1=dfex.at[k,'MW']
                # Q = dfex.at[k,'CAUDAL']
                # hole_depth = dfex.at[k,'MD']
                hole_depth = st.session_state.d1
                # dfpp1 = pd.DataFrame(columns=pipe_profile,index=range(12))
                ldfhp = st.session_state.dataframe2['Name'].count()
                ldfpp1 = dfpp1['Name'].count()


                # print(dfpp.at[2,'Long(ft)'])
                com1 = hole_depth >= st.session_state.dataframe1.at[0,'Long(ft)']
                com2 = (hole_depth-st.session_state.dataframe1.at[0,'Long(ft)'])>dfpp1.at[ldfhp-1,'Long(ft)']
                com3 = hole_depth <= st.session_state.dataframe1.at[0,'Long(ft)']
                print(com1,com2,com3)
                print(dfpp1)


                #----indica que la tuberia está dentro del casing o es una sola sección.----
                if com3:
                        
                    cont = 0
                    sum = 0
                    D_H = st.session_state.dataframe1.at[0,'hole diameter(in)']
                    print(ldfpp1-1)
            #---ajusta La longitudes de la tuberia en el dfpp1 con la  profundidad actual---            
                    for i in range (ldfpp1-1,-1,-1):
                        print(i)
                        sum = dfpp1.at[i,'Long(ft)']+sum
                        print(sum)
                        dfpp1.at[i,'Hole Diame(in)']=D_H
                        if hole_depth <= sum:
                            print(i)
                            diff = sum - hole_depth
                            dfpp1.at[i,'Long(ft)']=dfpp1.at[i,'Long(ft)']-diff
                            z = i-1
                            if z >= 0:
                                for q in range (z,-1,-1):
                                    dfpp1.drop([q], axis=0, inplace=True)
                                    dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                            print(dfpp1)
                            break
                                # dfpp1 = dfpp1.drop(index=[1])
                        cont += 1
            #---indica que el hueco tiene tiene dos secciones.---                   
                if com3==False:
                    cont = 0
                    sum = 0
                    D_H1 = st.session_state.dataframe1.at[0,'hole diameter(in)']
                    D_H2 = st.session_state.dataframe1.at[1,'hole diameter(in)']
                    print(ldfpp1-1)

            #---ajusta La longitudes de la tuberia en el dfpp1 con la profundidad actual---           
                    for i in range (ldfpp1-1,-1,-1):
                        print(i)
                        sum = dfpp1.at[i,'Long(ft)']+sum
                        print(sum)
                        dfpp1.at[i,'Hole Diame(in)']=D_H1
                        if hole_depth < sum:
                            print(i)
                            diff = sum - hole_depth
                            print(diff)
                            dfpp1.at[i,'Long(ft)']=dfpp1.at[i,'Long(ft)']-diff
                            if i-1 >= 0:
                                dfpp1.drop([i-1], axis=0, inplace=True)
                                print('hola')
                                print(dfpp1)
                                break
                            
                            cont += 1
                    sum=0
        #---bloque de codigo que calcula cual componente de la tuberia esta en la transición csg y hueco abierto, despues recalcula como deben quedar las longitudes del dfpp1----
                    ldfpp1 = dfpp1['Name'].count()
                    for j in range (ldfpp1-1,-1,-1):
                        diff = hole_depth-st.session_state.dataframe1.at[0,'Long(ft)']
                        sum = dfpp1.at[j,'Long(ft)']+sum
                        print(j)
                        if diff < sum:
                            if j == ldfpp1-1:
                                diff1 = dfpp1.at[j,'Long(ft)']-diff
                                diff2 = dfpp1.at[j,'Long(ft)']-diff1
                                dfpp1.at[j,'Long(ft)']=diff1
                                dfpp1.loc[j+0.5] = dfpp1.at[j,'Name'],diff,D_H2,dfpp1.at[j,'O.D Tub(in)'],dfpp1.at[j,'I.D Tub(in)']
                                dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                                print(dfpp1)
                                break
                            elif j == 0:
                                diff1 = dfpp1.at[j,'Long(ft)']-st.session_state.dataframe1.at[0,'Long(ft)']
                                diff2 = dfpp1.at[j,'Long(ft)']-diff1
                                dfpp1.at[j,'Long(ft)']=diff2
                                dfpp1.loc[j+0.5] = dfpp1.at[j,'Name'],diff1,D_H2,dfpp1.at[j,'O.D Tub(in)'],dfpp1.at[j,'I.D Tub(in)']
                                dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                                # dfpp = dfpp1.sort_index().reset_index(drop=True)
                                print(dfpp1)
                                # print(dfpp)
                                print('hola')
                                break 
                            elif j > 0:
                                print(j)
                                sum1=0
                                for k in range(j+1):
                                    sum1 = dfpp1.at[k,'Long(ft)']+sum1
                                diff1 = sum1-st.session_state.dataframe1.at[0,'Long(ft)']
                                diff2 = dfpp1.at[j,'Long(ft)']-diff1
                                dfpp1.at[j,'Long(ft)']=diff2
                                dfpp1.loc[j+0.5] = dfpp1.at[j,'Name'],diff1,D_H2,dfpp1.at[j,'O.D Tub(in)'],dfpp1.at[j,'I.D Tub(in)']
                                dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                                print(dfpp1)
                                break 
                        dfpp1.at[j,'Hole Diame(in)']=D_H2
                dfem1 = pd.concat([dfpp1,st.session_state.dfem], axis=1)
                    # print(dfemf)

                def vol_tub (O_D,I_D,Length):
                    if O_D is None:
                        volumen = round((I_D*I_D)*0.0009714*Length,1)
                    if O_D is not None:
                        volumen = round((O_D*O_D - I_D*I_D)*0.0009714*Length,1)
                    return volumen

                def vel_tub (I_D):
                    vt = round((Q*0.408)/I_D**2,0)
                    return vt
                def vel_anu (Q,OD_S,O_D):
                    va = round((Q*0.408)/(OD_S**2-O_D**2),0)
                    return va

                def vis_ef_tub (vt,I_D):
                    vet = round(100*Kt*(96*vt/I_D)**(Nt-1),0)
                    return vet
                def vis_ef_anu (va,OD_S,O_D):
                    vea = round(100*Ka*(144*(va)/(OD_S-O_D))**(Na-1),0)
                    return vea

                def reynolds_tub (vt,I_D,vet):
                    rt = round((928*vt*I_D*mw)/(vet*((3*Nt+1)/(4*Nt))**Nt),0)
                    return rt
                def reynolds_anu (va,OD_S,O_D,vea):
                    ra = round((928*va*(OD_S-O_D)*mw)/(vea*(((2*Na)+1)/(3*Na))**Na),1)
                    return ra

                def factor_fric_tub (rt):
                    if rt < (3470-1370*Nt):
                        fft = 16/rt
                    elif rt < (4270-1370*Nt):
                        fft = (((rt-(3470-1370*Nt))/800)*(((math.log10(Nt)+3.93)/50)/(4270-1370*Nt)**((1.75-math.log10(Nt))/7))-(16/(3470-1370*Nt))+16/(3470-1370*Nt))
                    else:
                        fft = ((math.log10(Nt)+3.93)/50)/(rt**((1.75-math.log10(Nt))/7))
                    return fft
                def factor_fric_anu (rfa,ra):
                    if ra < (3470-1370*Na):
                        ffa = round(24/ra,2)
                    elif ra < (4270-1370*Na):
                        round(((ra-(3470-1370*Na))/800)*((math.log10(Na)+3.93)/50/(4270-1370*Na)**((1.75-math.log10(Na))/7)-(24/(3470-1370*Na)))+(24/(3470-1370*Na)),2)
                        ffa = round(((ra-(3470-1370*Na))/800)*((math.log10(Na)+3.93)/50/(4270-1370*Na)**((1.75-math.log10(Na))/7)-(24/(3470-1370*Na)))+(24/(3470-1370*Na)),2)
                    else:
                        ffa = round(((math.log10(Na)+3.93)/50)/(ra**((1.75-math.log10(Na))/7)),2)
                    return ffa



                def Reg_Flujo_anular (ra):
                    com1 = (3470-1370*Na)
                    com2 = (4270-1370*Na)
                    if ra < com1:
                        rfa = 'LAM'
                    elif com1 < ra < com2:
                        rfa = 'TRANS' 
                    else:
                        rfa = 'TURB'
                    return rfa


                def loss_press_grad_tub (fft,vt,I_D,sl):
                    lpgt = round(((fft*vt**2*mw)/(25.81*I_D))*sl,0)
                    return lpgt
                def loss_press_grad_anu (ffa,va,OD_S,O_D,sl):
                    lpga = round((ffa*(va)**2*mw/(25.81*(OD_S-O_D)))*sl,0)
                    return lpga

                # --se Calcula el valor de la constante n y k para el anular y la tuberia--
                Na = round(0.5*math.log10((pv+yp)/t3),2)
                Ka = round((5.11*(pv+yp))/511**Na,2)
                Nt = round(3.32*math.log10((2*pv+yp)/(pv+yp)),2)
                Kt = round((5.11*(2*(pv+yp)-yp))/1022**Nt,2)


                    # Q = 206
                    #--Bloque de codigo que completa los datos indirectos del dfem que permite calcular la caida de presión del sistema--
                for i in range(10):
                    dfem1.at[i,'Vol Sarta(bbl)'] = vol_tub(None,dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                    dfem1.at[i,'Vol Anu(bbl)'] = vol_tub(dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                    dfem1.at[i,'Vel Anu(ft/min)'] = vel_anu(Q,dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'])
                    dfem1.at[i,'Vel Tub(ft/seg)'] = vel_tub(dfem1.at[i,'I.D Tub(in)'])
                    dfem1.at[i,'Viscosidad eff(tubing)']  = vis_ef_tub(dfem1.at[i,'Vel Tub(ft/seg)'],dfem1.at[i,'I.D Tub(in)'])
                    dfem1.at[i,'Viscosidad eff(anular)']  = vis_ef_anu(dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'])
                    dfem1.at[i,'Reynolds (tubing)'] = reynolds_tub(dfem1.at[i,'Vel Tub(ft/seg)'],dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Viscosidad eff(tubing)'])
                    dfem1.at[i,'Reynolds (anular)'] = reynolds_anu(dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Viscosidad eff(anular)'])
                    dfem1.at[i,'friction factor(tubing)'] = factor_fric_tub(dfem1.at[i,'Reynolds (tubing)'])
                    dfem1.at[i,'Reg Flujo(anular)'] = Reg_Flujo_anular(dfem1.at[i,'Reynolds (anular)'])
                    dfem1.at[i,'friction factor(anular)'] = factor_fric_anu(dfem1.at[i,'Reg Flujo(anular)'],dfem1.at[i,'Reynolds (anular)'])
                    dfem1.at[i,'loss press grad(tubing)'] = loss_press_grad_tub(dfem1.at[i,'friction factor(tubing)'],dfem1.at[i,'Vel Tub(ft/seg)'],dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                    dfem1.at[i,'loss press grad(anular)'] = loss_press_grad_anu(dfem1.at[i,'friction factor(anular)'],dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Long(ft)'])
        # ---calcula la caida de presión en la tuberia---

                loss_presure_tubing = round(dfem1['loss press grad(tubing)'].sum())
                loss_presure_anular = round(dfem1['loss press grad(anular)'].sum())
                # boquillas = tfa*1303.8
                # loss_presure_bit = 156*mw*Q**2/boquillas**2
                loss_presure_bit = (mw*Q**2)/(10858*(tfa**2))
                if loss_presure_tubing+loss_presure_anular == 0:
                    loss_presure_total = 0
                else:
                    loss_presure_total = loss_presure_tubing+loss_presure_anular+loss_presure_bit
                # print(dfem1[['Vol Anu(bbl)','Vel Anu(ft/min)']])
                print(loss_presure_total)
                df_lista.loc[0] = st.session_state.d1,round(loss_presure_total),0,0,0
                df_lista.dropna(inplace=True)
                # st.session_state.df2.reset_index(inplace=True)
                # df1.at[d,'SPPTE%+']  = df1.at[d,'SPPT']*error/100 + df1.at[d,'SPPT']
                # df1.at[d,'SPPTE%-']  = df1.at[d,'SPPT'] - df1.at[d,'SPPT']*error/100 
                
                # df1.reset_index(inplace=True)
                # print(df1)
                print(dfem1)        
                with st.expander("Visualizar dataset de parametros de perforación"):
                    st.dataframe(df_lista,hide_index=True)
                    st.dataframe(dfem1,hide_index = True)
                    st.write(f'Na = {Na}')
                    st.write(f'Ka = {Ka}')
                    st.write(f'Nt= {Nt}')
                    st.write(f'Kt = {Kt}')
  






        if len(st.session_state.lista_depth)>1:
            len_depth = st.session_state.d2 - st.session_state.d1
            contador4 = 0
            for v in range (st.session_state.d1,st.session_state.d2+1,st.session_state.step):

                dfpp1 = st.session_state.dataframe2.copy(deep=True)
                mw=st.session_state.mw1
                pv =st.session_state.pv1
                yp=st.session_state.yp1
                t3=st.session_state.t31
                tfa= st.session_state.tfa
                Q=m
                # mw1=dfex.at[k,'MW']
                # Q = dfex.at[k,'CAUDAL']
                # hole_depth = dfex.at[k,'MD']
                hole_depth = v
                # dfpp1 = pd.DataFrame(columns=pipe_profile,index=range(12))
                ldfhp = st.session_state.dataframe2['Name'].count()
                ldfpp1 = dfpp1['Name'].count()


            # print(dfpp.at[2,'Long(ft)'])
                com1 = hole_depth >= st.session_state.dataframe1.at[0,'Long(ft)']
                com2 = (hole_depth-st.session_state.dataframe1.at[0,'Long(ft)'])>dfpp1.at[ldfhp-1,'Long(ft)']
                com3 = hole_depth <= st.session_state.dataframe1.at[0,'Long(ft)']
                print(com1,com2,com3)
                print(dfpp1)


                    #----indica que la tuberia está dentro del casing o es una sola sección.----
                if com3:
                        
                    cont = 0
                    sum = 0
                    D_H = st.session_state.dataframe1.at[0,'hole diameter(in)']
                    print(ldfpp1-1)
            #---ajusta La longitudes de la tuberia en el dfpp1 con la  profundidad actual---            
                    for i in range (ldfpp1-1,-1,-1):
                        print(i)
                        sum = dfpp1.at[i,'Long(ft)']+sum
                        print(sum)
                        dfpp1.at[i,'Hole Diame(in)']=D_H
                        if hole_depth <= sum:
                            print(i)
                            diff = sum - hole_depth
                            dfpp1.at[i,'Long(ft)']=dfpp1.at[i,'Long(ft)']-diff
                            z = i-1
                            if z >= 0:
                                for q in range (z,-1,-1):
                                    dfpp1.drop([q], axis=0, inplace=True)
                                    dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                                print(dfpp1)
                                break
                                # dfpp1 = dfpp1.drop(index=[1])
                        cont += 1
            #---indica que el hueco tiene tiene dos secciones.---                   
                if com3==False:
                    cont = 0
                    sum = 0
                    D_H1 = st.session_state.dataframe1.at[0,'hole diameter(in)']
                    D_H2 = st.session_state.dataframe1.at[1,'hole diameter(in)']
                    print(ldfpp1-1)

            #---ajusta La longitudes de la tuberia en el dfpp1 con la profundidad actual---           
                    for i in range (ldfpp1-1,-1,-1):
                        print(i)
                        sum = dfpp1.at[i,'Long(ft)']+sum
                        print(sum)
                        dfpp1.at[i,'Hole Diame(in)']=D_H1
                        if hole_depth < sum:
                            print(i)
                            diff = sum - hole_depth
                            print(diff)
                            dfpp1.at[i,'Long(ft)']=dfpp1.at[i,'Long(ft)']-diff
                            if i-1 >= 0:
                                dfpp1.drop([i-1], axis=0, inplace=True)
                                print('hola')
                                print(dfpp1)
                                break
                            
                            cont += 1
                    sum=0
        #---bloque de codigo que calcula cual componente de la tuberia esta en la transición csg y hueco abierto, despues recalcula como deben quedar las longitudes del dfpp1----
                    ldfpp1 = dfpp1['Name'].count()
                    for j in range (ldfpp1-1,-1,-1):
                        diff = hole_depth-st.session_state.dataframe1.at[0,'Long(ft)']
                        sum = dfpp1.at[j,'Long(ft)']+sum
                        print(j)
                        if diff < sum:
                            if j == ldfpp1-1:
                                diff1 = dfpp1.at[j,'Long(ft)']-diff
                                diff2 = dfpp1.at[j,'Long(ft)']-diff1
                                dfpp1.at[j,'Long(ft)']=diff1
                                dfpp1.loc[j+0.5] = dfpp1.at[j,'Name'],diff,D_H2,dfpp1.at[j,'O.D Tub(in)'],dfpp1.at[j,'I.D Tub(in)']
                                dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                                print(dfpp1)
                                break
                            elif j == 0:
                                diff1 = dfpp1.at[j,'Long(ft)']-st.session_state.dataframe1.at[0,'Long(ft)']
                                diff2 = dfpp1.at[j,'Long(ft)']-diff1
                                dfpp1.at[j,'Long(ft)']=diff2
                                dfpp1.loc[j+0.5] = dfpp1.at[j,'Name'],diff1,D_H2,dfpp1.at[j,'O.D Tub(in)'],dfpp1.at[j,'I.D Tub(in)']
                                dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                                # dfpp = dfpp1.sort_index().reset_index(drop=True)
                                print(dfpp1)
                                # print(dfpp)
                                print('hola')
                                break 
                            elif j > 0:
                                print(j)
                                sum1=0
                                for k in range(j+1):
                                    sum1 = dfpp1.at[k,'Long(ft)']+sum1
                                diff1 = sum1-st.session_state.dataframe1.at[0,'Long(ft)']
                                diff2 = dfpp1.at[j,'Long(ft)']-diff1
                                dfpp1.at[j,'Long(ft)']=diff2
                                dfpp1.loc[j+0.5] = dfpp1.at[j,'Name'],diff1,D_H2,dfpp1.at[j,'O.D Tub(in)'],dfpp1.at[j,'I.D Tub(in)']
                                dfpp1 = dfpp1.sort_index().reset_index(drop=True)
                                print(dfpp1)
                                break 
                        dfpp1.at[j,'Hole Diame(in)']=D_H2
                dfem1 = pd.concat([dfpp1,st.session_state.dfem], axis=1)
                    # print(dfemf)
               
               
               
                def vol_tub (O_D,I_D,Length):
                    if O_D is None:
                        volumen = round((I_D*I_D)*0.0009714*Length,1)
                    if O_D is not None:
                        volumen = round((O_D*O_D - I_D*I_D)*0.0009714*Length,1)
                    return volumen

                def vel_tub (I_D):
                    vt = round((Q*0.408)/I_D**2,0)
                    return vt
                def vel_anu (Q,OD_S,O_D):
                    va = round((Q*0.408)/(OD_S**2-O_D**2),0)
                    return va

                def vis_ef_tub (vt,I_D):
                    vet = round(100*Kt*(96*vt/I_D)**(Nt-1),0)
                    return vet
                def vis_ef_anu (va,OD_S,O_D):
                    vea = round(100*Ka*(144*(va)/(OD_S-O_D))**(Na-1),0)
                    return vea

                def reynolds_tub (vt,I_D,vet):
                    rt = round((928*vt*I_D*mw)/(vet*((3*Nt+1)/(4*Nt))**Nt),0)
                    return rt
                def reynolds_anu (va,OD_S,O_D,vea):
                    ra = round((928*va*(OD_S-O_D)*mw)/(vea*(((2*Na)+1)/(3*Na))**Na),1)
                    return ra

                def factor_fric_tub (rt):
                    if rt < (3470-1370*Nt):
                        fft = 16/rt
                    elif rt < (4270-1370*Nt):
                        fft = (((rt-(3470-1370*Nt))/800)*(((math.log10(Nt)+3.93)/50)/(4270-1370*Nt)**((1.75-math.log10(Nt))/7))-(16/(3470-1370*Nt))+16/(3470-1370*Nt))
                    else:
                        fft = ((math.log10(Nt)+3.93)/50)/(rt**((1.75-math.log10(Nt))/7))
                    return fft
                def factor_fric_anu (rfa,ra):
                    if ra < (3470-1370*Na):
                        ffa = round(24/ra,2)
                    elif ra < (4270-1370*Na):
                        round(((ra-(3470-1370*Na))/800)*((math.log10(Na)+3.93)/50/(4270-1370*Na)**((1.75-math.log10(Na))/7)-(24/(3470-1370*Na)))+(24/(3470-1370*Na)),2)
                        ffa = round(((ra-(3470-1370*Na))/800)*((math.log10(Na)+3.93)/50/(4270-1370*Na)**((1.75-math.log10(Na))/7)-(24/(3470-1370*Na)))+(24/(3470-1370*Na)),2)
                    else:
                        ffa = round(((math.log10(Na)+3.93)/50)/(ra**((1.75-math.log10(Na))/7)),2)
                    return ffa



                def Reg_Flujo_anular (ra):
                    com1 = (3470-1370*Na)
                    com2 = (4270-1370*Na)
                    if ra < com1:
                        rfa = 'LAM'
                    elif com1 < ra < com2:
                        rfa = 'TRANS' 
                    else:
                        rfa = 'TURB'
                    return rfa


                def loss_press_grad_tub (fft,vt,I_D,sl):
                    lpgt = round(((fft*vt**2*mw)/(25.81*I_D))*sl,0)
                    return lpgt
                def loss_press_grad_anu (ffa,va,OD_S,O_D,sl):
                    lpga = round((ffa*(va)**2*mw/(25.81*(OD_S-O_D)))*sl,0)
                    return lpga

                # --se Calcula el valor de la constante n y k para el anular y la tuberia--
                Na = round(0.5*math.log10((pv+yp)/t3),2)
                Ka = round((5.11*(pv+yp))/511**Na,2)
                Nt = round(3.32*math.log10((2*pv+yp)/(pv+yp)),2)
                Kt = round((5.11*(2*(pv+yp)-yp))/1022**Nt,2)


                    # Q = 206
# --- Bloque de codigo que completa los datos indirectos del dfem1 que permite calcular las perdidas de presion del sistema ---
                for i in range(10):
                    dfem1.at[i,'Vol Sarta(bbl)'] = vol_tub(None,dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                    dfem1.at[i,'Vol Anu(bbl)'] = vol_tub(dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                    dfem1.at[i,'Vel Anu(ft/min)'] = vel_anu(Q,dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'])
                    dfem1.at[i,'Vel Tub(ft/seg)'] = vel_tub(dfem1.at[i,'I.D Tub(in)'])
                    dfem1.at[i,'Viscosidad eff(tubing)']  = vis_ef_tub(dfem1.at[i,'Vel Tub(ft/seg)'],dfem1.at[i,'I.D Tub(in)'])
                    dfem1.at[i,'Viscosidad eff(anular)']  = vis_ef_anu(dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'])
                    dfem1.at[i,'Reynolds (tubing)'] = reynolds_tub(dfem1.at[i,'Vel Tub(ft/seg)'],dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Viscosidad eff(tubing)'])
                    dfem1.at[i,'Reynolds (anular)'] = reynolds_anu(dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Viscosidad eff(anular)'])
                    dfem1.at[i,'friction factor(tubing)'] = factor_fric_tub(dfem1.at[i,'Reynolds (tubing)'])
                    dfem1.at[i,'Reg Flujo(anular)'] = Reg_Flujo_anular(dfem1.at[i,'Reynolds (anular)'])
                    dfem1.at[i,'friction factor(anular)'] = factor_fric_anu(dfem1.at[i,'Reg Flujo(anular)'],dfem1.at[i,'Reynolds (anular)'])
                    dfem1.at[i,'loss press grad(tubing)'] = loss_press_grad_tub(dfem1.at[i,'friction factor(tubing)'],dfem1.at[i,'Vel Tub(ft/seg)'],dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                    dfem1.at[i,'loss press grad(anular)'] = loss_press_grad_anu(dfem1.at[i,'friction factor(anular)'],dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Long(ft)'])
        # ---calcula la caida de presión en la tuberia---

                loss_presure_tubing = round(dfem1['loss press grad(tubing)'].sum())
                loss_presure_anular = round(dfem1['loss press grad(anular)'].sum())
                # boquillas = tfa*1303.8
                # loss_presure_bit = 156*mw*Q**2/boquillas**2
                loss_presure_bit = (mw*Q**2)/(10858*(tfa**2))
                if loss_presure_tubing+loss_presure_anular == 0:
                    loss_presure_total = 0
                else:
                    loss_presure_total = loss_presure_tubing+loss_presure_anular+loss_presure_bit
                # print(dfem1[['Vol Anu(bbl)','Vel Anu(ft/min)']])
                print(loss_presure_total)
                df_lista.loc[contador4] = v,round(loss_presure_total),0,0,0
                df_lista.dropna(inplace=True)
                # st.session_state.df2.reset_index(inplace=True)
                # df1.at[d,'SPPTE%+']  = df1.at[d,'SPPT']*error/100 + df1.at[d,'SPPT']
                # df1.at[d,'SPPTE%-']  = df1.at[d,'SPPT'] - df1.at[d,'SPPT']*error/100 
                
                # df1.reset_index(inplace=True)
                # print(df1)
                # print(dfem1)  
                contador4 +=1      
            with st.expander(f"Visualizar dataset de presiones simuladas para Caudal (gpm) {m}"):
                st.dataframe(df_lista,hide_index=True)
        contador3 += 1
            
#---Código que crea el gráfico analisis de presión de perforación---        
        fig = go.Figure() #Crea el objeto figura.
        fig.add_trace(go.Scatter(x=st.session_state.df2['Depth(ft)'], y=st.session_state.df2['SPPT(psi)'],name = f'Caudal: {st.session_state.lista_q[0]}',mode='lines', line_color='green'))# Se agrega una linea a la figura, donde se le da un nombre a la linea y se personaliza
        fig.add_trace(go.Scatter(x=st.session_state.df3['Depth(ft)'], y=st.session_state.df3['SPPT(psi)'],name = f'Caudal: {st.session_state.lista_q[1]}', mode='lines', line_color='white'))
        fig.add_trace(go.Scatter(x=st.session_state.df4['Depth(ft)'], y=st.session_state.df4['SPPT(psi)'],name = f'Caudal: {st.session_state.lista_q[2]}', mode='lines', line_color='yellow'))
        fig.update_layout(title='Presión de perforación simuladas', xaxis_title='Depth(ft)', yaxis_title='Presión(psi)',template='plotly_white')
    # fig.show() 

    st.plotly_chart(fig)
