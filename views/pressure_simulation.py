import streamlit as st

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

# def check (ncol, list):
#     if ncol in list:
#         return True
#     else:
#         return False

multi ='''##### :blue[Esta opción le permitira simular presiones de perforación para tener una idea de como debe ser el comportamiento de la presión durante la perforación y poder detectar posibles anomalias en este parámetro durante la operación.] 
Para usar esta opción debe seguir estos pasos:  
1- Completar la información solicitada en la opción (2) de esta aplicación.  
2- Ingresar los siguientes Datos y luego oprimir el botón ¡generar presiones simuladas!.'''
st.markdown(multi)

with st.expander('Datos fluido de perforación:'):
    with st.form('mud', clear_on_submit=True):
        # st.markdown('Ingrese la información en el formulario y luego oprima el boton cargar información:')
        mw1 = st.number_input("Peso de lodo MW (ppg): ",value=None,placeholder="Type a number...")
        pv1 = st.number_input("Viscosidad plastica PV (cp): ",value=None,placeholder="Type a number...")
        yp1 = st.number_input("Yield point YP (lbf/100ft**2): ",value=None,placeholder="Type a number...")
        t31 = st.number_input("Reologia TETA 3: ",value=None,placeholder="Type a number...")
        # q1 = st.number_input("Caudal 1 (gpm): ",value=None,placeholder="Type a number...")
        # q2 = st.number_input("Caudal 2 (gpm): ",value=None,placeholder="Type a number...")
        # q3 = st.number_input("Caudal 3 (gpm): ",value=None,placeholder="Type a number...")
        boton3 = st.form_submit_button('¡cargar infomación!')
    if boton3:
        lista = [mw1,pv1,yp1,t31]
        if None in lista:
            st.warning(f"Debe ingresar toda la información del formulario antes de oprimir el botón ¡cargar infomación!: ")
            st.stop()

        st.session_state.mw1 = mw1
        st.session_state.pv1 = pv1
        st.session_state.yp1 = yp1
        st.session_state.t31 = t31
        # st.session_state.q1 = q1
        # st.session_state.q2 = q2
        # st.session_state.q3 = q3

    st.markdown('Verifique la información que cargó, si hay algún error oprima el botón REINICIAR para cargar los datos nuevamente.')
    st.write(f'MW = {st.session_state.mw1}')
    st.write(f'PV = {st.session_state.pv1}')
    st.write(f'YP = {st.session_state.yp1}')
    st.write(f'T3 = {st.session_state.t31}')
    # st.write(f'Q1 = {st.session_state.q1}')
    # st.write(f'Q2= {st.session_state.q2}')
    # st.write(f'Q3 = {st.session_state.q3}')
    boton4 = st.button('¡Reiniciar!')

with st.expander('Pump rate:'):
        with st.form('caudales', clear_on_submit=True):
            st.markdown('Puede simular la presión de perforación para diferentes caudales de perforación:')
            q1 = st.number_input("Caudal 1 (gpm): ",value=None,placeholder="Type a number...")
            q2 = st.number_input("Caudal 2 (gpm): ",value=None,placeholder="Type a number...")
            q3 = st.number_input("Caudal 3 (gpm): ",value=None,placeholder="Type a number...")
            boton5 = st.form_submit_button('¡cargar infomación!')
            if boton3:
                st.session_state.q1 = q1
                st.session_state.q2 = q2
                st.session_state.q3 = q3


        st.markdown('Verifique la información que cargó, si hay algún error oprima el botón REINICIAR para cargar los datos nuevamente.')
        st.write(f'Caudal 1 = {st.session_state.q1}')
        st.write(f'Caudal 2 = {st.session_state.q2}')
        st.write(f'Caudal 3 = {st.session_state.q3}')
           

with st.expander('Pronfundidad:'):
        with st.form('depth', clear_on_submit=True):
            st.markdown('Puede simular la presión de perforación para una profundidad puntual o para un rango de profundidad:')
            d1 = st.number_input("Profundidad inicial (ft): ",value=None,placeholder="Type a number...")
            d2 = st.number_input("Profundidad final (ft): ",value=None,placeholder="Type a number...")
            step = st.number_input("Pasos (generar presión de perforación cada 1 ft, 10ft etc...) (ft): ",value=None,placeholder="Type a number...")
            boton6 = st.form_submit_button('¡cargar infomación!')
            if boton3:
                st.session_state.d1 = d1
                st.session_state.d2 = d2
                st.session_state.step = step


        st.markdown('Verifique la información que cargó, si hay algún error oprima el botón REINICIAR para cargar los datos nuevamente.')
        st.write(f'Caudal 1 = {st.session_state.d1}')
        st.write(f'Caudal 2 = {st.session_state.d2}')
        st.write(f'Caudal 3 = {st.session_state.step}')



# st.markdown('###### Verifique la información que cargó en cada formulario, si hay algún error en esa información oprima el boton REINICIAR para cargar los datos nuevamente!!!')

st.button('¡Generar presiones simuladas!')