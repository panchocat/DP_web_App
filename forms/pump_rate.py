import streamlit as st  

def pump_rate():
     with st.form('caudales', clear_on_submit=True):
        st.markdown('Puede simular la presión de perforación para diferentes caudales de perforación:')
        q1 = st.number_input("Caudal 1 (gpm): ",value=None,placeholder="Type a number...")
        q2 = st.number_input("Caudal 2 (gpm): ",value=None,placeholder="Type a number...")
        q3 = st.number_input("Caudal 3 (gpm): ",value=None,placeholder="Type a number...")
        cargar3 = st.form_submit_button('¡cargar infomación!')
        final3 = st.form_submit_button('¡Finalizar!')
        if cargar3:
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.q3 = q3
            st.session_state.lista_q = [st.session_state.q1,st.session_state.q2,st.session_state.q3]
            st.write(f'Caudal 1 = {st.session_state.q1}')
            st.write(f'Caudal 2 = {st.session_state.q2}')
            st.write(f'Caudal 3 = {st.session_state.q3}')
        if final3:
            st.rerun()


  