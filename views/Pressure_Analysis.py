import streamlit as st
import pandas as pd
import math
import copy
import plotly.graph_objects as go #Libreria que permite hacer gráfico mas complejo o elaborado. Permite personalizar los gráficos.

# dfex = st.session_state.df
if 'dfem' not in st.session_state:
    st.session_state.dfem= pd.DataFrame(columns=['Vol Sarta(bbl)','Vol Anu(bbl)','Vel Anu(ft/min)','Vel Tub(ft/min)','Viscosidad eff(tubing)','Viscosidad eff(anular)','Reynolds (anular)','Reynolds (tubing)','friction factor(tubing)','friction factor(anular)','loss press grad(tubing)','loss press grad(anular)','Vel Crit(ft/min)','Caud Crit(gpm)','Reg Flujo(anular)'], index=range(12))
# if 'df1' not in st.session_state:
#     st.session_state.df1=pd.DataFrame()
# st.session_state.df


# df1.set_index("MD", inplace=True)
# '<div style="text-align: justify;">Hello World!</div>', unsafe_allow_html=True
st.markdown('#### :blue[<div style="text-align: justify;">Esta opción generará un gráfico que compara la presión de perforación real vs la presión teórica de perforación para identificar posibles presiones anómalas que hubo durante la perforación. Para generar el gráfico de análisis de presión de perforación primero debe completar los pasos 1 y 2 de la aplicación.]', unsafe_allow_html=True)
with st.form('show'):
    error = st.number_input(' Ingrese el porcentaje de error o ventana de error respecto a la presión teórica que desea visualizar en el grafico',value=None,placeholder="Type a number...")
    graficar = st.form_submit_button('¡Generar Gráfico!')
    if graficar:
        if error == None:
            st.warning(f"Debe ingresar el dato de 'porcentaje de error' antes de oprimir ¡Generar Gráfico!: ")
            st.stop()
        df1 = st.session_state.df.copy(deep=True)
        dfl = len(st.session_state.df["MD"])# Calculamos y almacenamos el valor de la longitud de la serie HOLE DEPTH del df en la variable dfl.
        dmax = st.session_state.df["MD"].max()# almacenamos en una variable el valor minimo de la columna DEPTH.
        dmin = st.session_state.df["MD"].min()# almacenamos en una variable el valor maximo de la columna DEPTH.
        df1.set_index("MD", inplace=True)
        # dfex = st.session_state.df # se crea la variable df leyendo la información de un archivo .xlsx

        #mwl = st.session_state.df["MW"].head().isnull()# muestra si los primeros 5 valores de la columna MW esta vacios.
        print(st.session_state.df)
        print(dfl)
        print(dmax)
        print(dmin)
        # print(dmin)
        # print(dmax)
        #print(mwl)
        #print(mwl1)
        #print(mwl2)

    

#--Bloque de codigo que corre hidraulica---
        for d in range(dmin,dmax+1):
            print(dmax)
            print(dmin)
            dfpp1 = st.session_state.dataframe2.copy(deep=True)
            mw=df1.at[d,'MW']
            pv =df1.at[d,'PV']
            yp=df1.at[d,'YP']
            t3=df1.at[d,'T3']
            tfa= st.session_state.tfa
            Q=df1.at[d,'CAUDAL']
            # mw1=dfex.at[k,'MW']
            # Q = dfex.at[k,'CAUDAL']
            # hole_depth = dfex.at[k,'MD']
            hole_depth = d
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
                        if i-1 >= 0:
                            dfpp1.drop([i-1], axis=0, inplace=True)
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

            def vel_anu (Q,OD_S,O_D):
                va = round(0.408*Q/(OD_S**2-O_D**2)*60,1)
                return va
            def vel_tub (I_D):
                vt = round((0.408*Q)/I_D**2,1)
                return vt

            def vis_ef_tub (vt,I_D):
                vet = 100*Kt*(96*vt/I_D)**(Nt-1)
                return vet
            def vis_ef_anu (va,OD_S,O_D):
                vea = 100*Ka*(144*(va/60)/(OD_S-O_D))**(Na-1)
                return vea

            def reynolds_tub (vt,I_D,vet):
                rt = round((928*vt*I_D*mw)/(vet*((3*Nt+1)/(4*Nt))**Nt),1)
                return rt
            def reynolds_anu (va,OD_S,O_D,vea):
                ra = round(928*va/60*(OD_S-O_D)*mw/(vea*(((2*Na)+1)/(3*Na))**Na),1)
                return ra

            def factor_fric_tub (rt):
                if rt < (3470-1370*Nt):
                    fft = 16/rt
                if rt <= (4207-1370*Nt):
                    fft = (((rt-(3470-1370*Nt))/800)*(((math.log10(Nt)+3.93)/50)/(4270-1370*Nt)**((1.75-math.log10(Nt))/7))-(16/(3470-1370*Nt))+16/(3470-1370*Nt))
                else:
                    fft = ((math.log10(Nt)+3.93)/50)/(rt**((1.75-math.log10(Nt))/7))
                return fft
            def factor_fric_anu (rfa,ra):
                if rfa == "LAM":
                    ffa = round(24/ra,3)
                elif rfa == "TRANS":
                    ffa = round(((ra-(3470-1370*Na))/800)*((math.log10(Na)+3.93)/50/(4270-1370*Na)**((1.75-math.log10(Na))/7)-(24/(3470-1370*Na)))+(24/(3470-1370*Na)),3)
                else:
                    ffa = round(((math.log10(Na)+3.93)/50)/(ra**((1.75-math.log10(Na))/7)),3)
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
                lpgt = (fft*vt**2*mw)/(25.81*I_D)*sl
                return lpgt
            def loss_press_grad_anu (ffa,va,OD_S,O_D,sl):
                lpga = (ffa*(va/60)**2*mw/(25.81*(OD_S-O_D)))*sl
                return lpga

            # --se Calcula el valor de la constante n y k para el anular y la tuberia--
            Na = round(0.5*math.log10((pv+yp)/t3),3)
            Ka = round(5.11*(pv+yp)/511**Na,3)
            Nt = round(3.32*math.log10((2*pv+yp)/(pv+yp)),3)
            Kt = round(5.11*(2*(pv+yp)-yp)/1022**Nt,3)


            # Q = 206
            #--Bloque de codigo que completa los datos indirectos del dfem que permite calcular la caida de presión del sistema--
            for i in range(10):
                dfem1.at[i,'Vol Sarta(bbl)'] = vol_tub(None,dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                dfem1.at[i,'Vol Anu(bbl)'] = vol_tub(dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                dfem1.at[i,'Vel Anu(ft/min)'] = vel_anu(Q,dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'])
                dfem1.at[i,'Vel Tub(ft/min)'] = vel_tub(dfem1.at[i,'I.D Tub(in)'])
                dfem1.at[i,'Viscosidad eff(tubing)']  = vis_ef_tub(dfem1.at[i,'Vel Tub(ft/min)'],dfem1.at[i,'I.D Tub(in)'])
                dfem1.at[i,'Viscosidad eff(anular)']  = vis_ef_anu(dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'])
                dfem1.at[i,'Reynolds (tubing)'] = reynolds_tub(dfem1.at[i,'Vel Tub(ft/min)'],dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Viscosidad eff(tubing)'])
                dfem1.at[i,'Reynolds (anular)'] = reynolds_anu(dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Viscosidad eff(anular)'])
                dfem1.at[i,'friction factor(tubing)'] = factor_fric_tub(dfem1.at[i,'Reynolds (tubing)'])
                dfem1.at[i,'Reg Flujo(anular)'] = Reg_Flujo_anular(dfem1.at[i,'Reynolds (anular)'])
                dfem1.at[i,'friction factor(anular)'] = factor_fric_anu(dfem1.at[i,'Reg Flujo(anular)'],dfem1.at[i,'Reynolds (anular)'])
                dfem1.at[i,'loss press grad(tubing)'] = loss_press_grad_tub(dfem1.at[i,'friction factor(tubing)'],dfem1.at[i,'Vel Tub(ft/min)'],dfem1.at[i,'I.D Tub(in)'],dfem1.at[i,'Long(ft)'])
                dfem1.at[i,'loss press grad(anular)'] = loss_press_grad_anu(dfem1.at[i,'friction factor(anular)'],dfem1.at[i,'Vel Anu(ft/min)'],dfem1.at[i,'Hole Diame(in)'],dfem1.at[i,'O.D Tub(in)'],dfem1.at[i,'Long(ft)'])

# ---calcula la caida de presión en la tuberia---
            loss_presure_tubing = round(dfem1['loss press grad(tubing)'].sum())
            loss_presure_anular = round(dfem1['loss press grad(anular)'].sum())
            boquillas = tfa*1303.8
            loss_presure_bit = 156*mw*Q**2/boquillas**2
            loss_presure_total = loss_presure_tubing+loss_presure_anular+loss_presure_bit
            # print(dfem1[['Vol Anu(bbl)','Vel Anu(ft/min)']])
            print(loss_presure_total)
            df1.at[d,'SPPT'] = round(loss_presure_total)
            df1.at[d,'SPPTE%+']  = df1.at[d,'SPPT']*error/100 + df1.at[d,'SPPT']
            df1.at[d,'SPPTE%-']  = df1.at[d,'SPPT'] - df1.at[d,'SPPT']*error/100 
        
        df1.reset_index(inplace=True)
        print(df1)
        # print(dfem1)        
        with st.expander("Visualizar dataset de parametros de perforación"):
            st.dataframe(df1)
        
#---Código que crea el gráfico analisis de presión de perforación---        
        fig = go.Figure() #Crea el objeto figura.
        fig.add_trace(go.Scatter(x=df1.MD, y=df1['SPPT'],name = 'SPPT',mode='lines', line_color='indigo'))# Se agrega una linea a la figura, donde se le da un nombre a la linea y se personaliza
        fig.add_trace(go.Scatter(x=df1.MD, y=df1['SPPTE%+'],name = 'SPPT5%+', line=dict(color='royalblue', width=4,dash='dash'),fill='tonexty'))
        fig.add_trace(go.Scatter(x=df1.MD, y=df1['SPPT'],name = 'SPPT',mode='lines', line_color='indigo',showlegend=False))
        fig.add_trace(go.Scatter(x=df1.MD, y=df1['SPPTE%-'],name = 'SPPT5%-', line=dict(color='royalblue', width=4,dash='dash'),fill='tonexty'))
        fig.add_trace(go.Scatter(x=df1.MD, y=df1.SPP,name = 'SPP',mode='lines', line_color='green'))
        fig.update_layout(title='Análisis de presión de perforación', xaxis_title='Depth(ft)', yaxis_title='Presión(psi)',template='plotly_white')
        # fig.show() 
        
        st.plotly_chart(fig)
# with st.expander("Visualizar dataset de parametros de perforación"):
#     st.dataframe(df1, hide_index=True)