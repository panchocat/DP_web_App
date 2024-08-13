import streamlit as st

if 'mw1' not in st.session_state:
    st.session_state['mw1']=0
if 'pv1' not in st.session_state:
    st.session_state['pv1']=0
if 'yp1' not in st.session_state:
    st.session_state['yp1']=0
if 't31' not in st.session_state:
    st.session_state['t31']=0
if 'q1' not in st.session_state:
    st.session_state['q1']=0
if 'q2' not in st.session_state:
    st.session_state['q2']=0
if 'q3' not in st.session_state:
    st.session_state['q3']=0



multi ='''##### :blue[Esta opción de la aplicación le permitira simular presiones de perforación para tener una idea de como puede ser el comportamiento de la presión durante la perforación. Esta información le permitirá detectar posibles anomalias en este parámetro durante la operación.]  
Para usar esta opción debe seguir estas indicaciones:  
1- Completar la información solicitada en la opción (2) de esta aplicación.  
2- Ahora complete la información solicitada en esta opción y luego oprimir el botón generar información.'''
st.markdown(multi)

with st.expander("Datos de entrada para simular presiones"):
    with st.form('presiones_simuladas', clear_on_submit=True):
        st.markdown('Datos fluido de perforación y caudal:')
        mw1 = st.text_area("Peso de lodo MW (ppg): ",value=None,placeholder="Type a number...",height=0,max_chars=4)
        pv1 = st.text_area("Viscosidad plastica PV (cp): ",value=None,placeholder="Type a number...")
        yp1 = st.text_area("Yield point YP (lbf/100ft**2): ",value=None,placeholder="Type a number...")
        t31 = st.text_area("Reologia TETA 3: ",value=None,placeholder="Type a number...")
        q1 = st.text_area("Caudal 1 (gpm): ",value=None,placeholder="Type a number...")
        q2 = st.text_area("Caudal 2 (gpm): ",value=None,placeholder="Type a number...")
        q3 = st.text_area("Caudal 3 (gpm): ",value=None,placeholder="Type a number...")
        boton3 = st.form_submit_button('¡cargar infomación!')

    if boton3:
        st.markdown('Verifique la información que cargó, si hay algún error en esa información oprima el boton REINICIAR para cargar los datos nuevamente ')
        st.session_state['mw1'] = float(mw1)
        st.session_state['pv1'] = float(pv1) 
        st.session_state['yp1'] = float(yp1) 
        st.session_state['t31'] = float(t31)
        st.session_state['q1'] = float(q1)
        st.session_state['q2'] = float(q2)
        st.session_state['q3'] = float(q3)

        st.write(f'MW = {st.session_state['mw1']}')
        st.write(f'PV = {st.session_state['pv1']}')
        st.write(f'YP = {st.session_state['yp1']}')
        st.write(f'T3 = {st.session_state['t31']}')
        st.write(f'Q1 = {st.session_state['q1']}')
        st.write(f'Q2= {st.session_state['q2']}')
        st.write(f'Q3 = {st.session_state['q3']}')
        boton4 = st.button('¡Reiniciar!')