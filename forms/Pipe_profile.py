import streamlit as st 


def pipe_profile():
    with st.form('pipe_profile', clear_on_submit=True):
        st.markdown('Ingrese los componentes de la sarta de perforación desde superficie a fondo:')
        Name = st.text_input("Nombre del componente (ej. DP(Drill pipe) or BHA(Bottom hole asembly)): ",placeholder=None)
        Long = st.number_input("Longitud del componente (ft): ",value=None,placeholder="Type a number...")
        O_D = st.number_input("Diametro Externo del componente (in): ",value=None,placeholder="Type a number...")
        I_D = st.number_input("Diametro Interno del componente (in): ",value=None,placeholder="Type a number...")
        tfa = st.number_input("TFA de la broca (:warning: Ingrese esta información cuando agregue el último componente de la sarta): ",value=None,placeholder="Type a number...")
        cargar1 = st.form_submit_button('¡cargar infomación!')
        final1 = st.form_submit_button('¡Finalizar!')
    if cargar1:
        lista = [Name,Long,O_D,I_D,]
        if None in lista:
            st.warning(f"Debe ingresar toda la información del formulario antes de oprimir el botón ¡cargar infomación!: ")
            st.stop()
        st.session_state.dataframe2.loc[st.session_state.counter1] = [Name,Long,0,O_D,I_D]
        st.session_state.counter1 += 1
        st.session_state.tfa=tfa
        st.session_state.dataframe2.dropna(inplace=True)
        st.dataframe(st.session_state.dataframe2, hide_index=True)
        st.write(f'TFA = {st.session_state.tfa}')
    if final1:
        st.rerun()