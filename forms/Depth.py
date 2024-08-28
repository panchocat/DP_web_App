import streamlit as st 

def depth():
    with st.form('profundidades', clear_on_submit=True):
        st.markdown('Puede simular la presión de perforación para una profundidad puntual o para un rango de profundidad:')
        d1 = st.number_input("Profundidad inicial (ft) :red[*]: ",value=None,placeholder="Type a number...")
        d2 = st.number_input("Profundidad final (ft): ",placeholder="Type a number...")
        step = st.number_input("Pasos (generar presión de perforación cada 1 ft, 10ft etc...) (ft): ",placeholder="Type a number...")
        cargar4 = st.form_submit_button('¡cargar infomación!')
        final4 = st.form_submit_button('¡Finalizar!')
        st.markdown(":red[*] Campo obligatorio.")
        if cargar4:
            if d1 == None:
                st.warning(f"Debe ingresar el dato de 'Profundidad inicial (ft)' antes de oprimir ¡cargar infomación!: ")
                st.stop()
            st.session_state.d1 = int(d1)
            st.session_state.d2 = int(d2)
            st.session_state.step = int(step)
            st.session_state.lista_depth = [st.session_state.d1,st.session_state.d2,st.session_state.step]

            st.write(f'Profundidad inicial = {st.session_state.d1}')
            st.write(f'Profundidad final = {st.session_state.d2}')
            st.write(f'step = {st.session_state.step}')
        if final4:
            st.rerun()