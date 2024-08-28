import streamlit as st 


def hole_profile():
    
    # placeholder = st.empty()
    with st.form('well_profile', clear_on_submit=True):
        st.markdown('Ingrese las secciones que tiene el pozo desde superficie a fondo')
        Name = st.text_input("Nombre de la sección (ej. OH(open hole) or CSG(Casing)) :red[*]: ",value=None,placeholder=None)
        long = st.number_input("Longitud de la sección (ft) :red[*]: ",value=None,placeholder="Type a number...")
        Diam = st.number_input("Diametro de la sección (in) :red[*]: ",value=None,placeholder="Type a number...")
        st.markdown("Si desea cargar mas información, escriba la información y oprima ¡Cargar información!. Si no desea cargar mas información prima ¡finalizar!.")
        cargar = st.form_submit_button('¡cargar infomación!')
        final = st.form_submit_button('¡Finalizar!')
        st.markdown(":red[*] Información obligatorio.")

        if cargar:
            lista = [Name,long,Diam]
            if None in lista:
                st.warning(f"Debe ingresar toda la información del formulario antes de oprimir el botón ¡cargar infomación!: ")
                st.stop()
            st.session_state.dataframe1.loc[st.session_state.counter] = [Name,long,Diam]
            st.session_state.counter += 1
            st.session_state.dataframe1.dropna(inplace=True)
            st.dataframe(st.session_state.dataframe1, hide_index=True)

        if final:
            st.rerun()

            
 