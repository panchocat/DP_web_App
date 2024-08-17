import streamlit as st 


def hole_profile():
    
    # placeholder = st.empty()
    with st.form('well_profile', clear_on_submit=True):
        st.markdown('Ingrese las secciones que tiene el pozo desde superficie a fondo:')
        Name = st.text_input("Nombre de la sección (ej. OH(open hole) or CSG(Casing)): ",value=None,placeholder=None)
        long = st.number_input("Longitud de la sección (ft): ",value=None,placeholder="Type a number...")
        Diam = st.number_input("Diametro de la sección (in): ",value=None,placeholder="Type a number...")
        st.markdown("Si desea cargar mas información, escriba la información y oprima ¡Cargar información!. Si no desea cargar mas información prima ¡finalizar!.")
        cargar = st.form_submit_button('¡cargar infomación!')
        final = st.form_submit_button('¡Finalizar!')
        if cargar:
            # hole_profile = ['Name','hole diameter(in)','Long(ft)']#crea listas con los nombres de las columnas que van a tener los dataframes.
            # dfhp = pd.DataFrame(columns=hole_profile, index=range(5))
            st.session_state.dataframe1.loc[st.session_state.counter] = [Name,long,Diam]
            st.session_state.counter += 1
            st.session_state.dataframe1.dropna(inplace=True)
            st.dataframe(st.session_state.dataframe1, hide_index=True)
            # st.rerun()
            # st.dataframe(st.session_state.dataframe1, hide_index=True)
        if final:
            # # dfhp = st.session_state.dataframe1
            # # dfhp = dfhp.dropna()
            # st.session_state.dataframe1.dropna(inplace=True)
            st.rerun()
            # # placeholder.empty()
            # # st.session_state.counter = st.session_state
            
 