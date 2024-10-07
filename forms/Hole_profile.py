import streamlit as st 



def hole_profile():
    
    with st.form('well_profile', clear_on_submit=True):
        st.markdown('#### Ingrese las secciones que tiene el pozo desde superficie a fondo. (Campos obligatorios :red[*] ).')
        name = st.text_input("Nombre de la sección (ej. OH(open hole) or CSG(Casing)) :red[*]: ",value=None,placeholder=None)
        long = st.number_input("Longitud de la sección (ft) :red[*]: ",value=None,placeholder="Type a number...")
        diam = st.number_input("Diametro de la sección (in) :red[*]: ",value=None,placeholder="Type a number...")
        cargar = st.form_submit_button('¡cargar infomación!')
        st.markdown("Si no desea cargar mas información prima ¡finalizar!.")
        final = st.form_submit_button('¡Finalizar!')
        # st.markdown(":red[*] Información obligatorio.")

        if cargar:
            lista = [name,long,diam]
            if None in lista:
                st.warning(f"Debe ingresar toda la información del formulario antes de oprimir el botón ¡cargar infomación!: ")
                st.stop()
            st.session_state.dataframe1.loc[st.session_state.counter] = [name,long,diam]
            st.session_state.counter += 1
            st.session_state.dataframe1.dropna(inplace=True)
            st.dataframe(st.session_state.dataframe1, hide_index=True)
            st.success('Data saved!, Si desea cargar mas información, llene los campos y oprima ¡Cargar información!.')

        if final:
            st.rerun()

            
 