import streamlit as st  


def mud_data():
    with st.form('mud', clear_on_submit=True):
        st.markdown('Ingrese la información en el formulario y luego oprima el boton cargar información:')
        mw1 = st.number_input("Peso de lodo MW (ppg) :red[*]: ",value=None,placeholder="Type a number...")
        pv1 = st.number_input("Viscosidad plastica PV (cp) :red[*]: ",value=None,placeholder="Type a number...")
        yp1 = st.number_input("Yield point YP (lbf/100ft**2) :red[*]: ",value=None,placeholder="Type a number...")
        t31 = st.number_input("Reologia TETA 3 :red[*]:",value=None,placeholder="Type a number...")
        cargar2 = st.form_submit_button('¡cargar infomación!')
        final2 = st.form_submit_button('¡Finalizar!')
        st.markdown(":red[*] Campo obligatorio.")
        if cargar2:
            lista = [mw1,pv1,yp1,t31]
            if None in lista:
                st.warning(f"Debe ingresar toda la información del formulario antes de oprimir el botón ¡cargar infomación!: ")
                st.stop()

            st.session_state.mw1 = mw1
            st.session_state.pv1 = pv1
            st.session_state.yp1 = yp1
            st.session_state.t31 = t31
            st.write(f'MW = {st.session_state.mw1}')
            st.write(f'PV = {st.session_state.pv1}')
            st.write(f'YP = {st.session_state.yp1}')
            st.write(f'T3 = {st.session_state.t31}')
        if final2:
            st.rerun()
