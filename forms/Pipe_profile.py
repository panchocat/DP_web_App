import streamlit as st 


def pipe_profile():
    with st.form('pipe_profile', clear_on_submit=True):
        st.markdown('Ingrese los componentes de la sarta de perforación desde superficie a fondo:')
        Name = st.text_input("Nombre del componente (ej. DP(Drill pipe) or BHA(Bottom hole asembly)): ",placeholder=None)
        Long = st.number_input("Longitud del componente (ft): ",value=None,placeholder="Type a number...")
        O_D = st.number_input("Diametro Externo del componente (in): ",value=None,placeholder="Type a number...")
        I_D = st.number_input("Diametro Interno del componente (in): ",value=None,placeholder="Type a number...")
        tfa = st.number_input("TFA de la broca: ",value=None,placeholder="Type a number...")
        submit = st.form_submit_button('¡cargar infomación!')
        final = st.form_submit_button('¡Finalizar!')
    if submit:
        # hole_profile = ['Name','hole diameter(in)','Long(ft)']#crea listas con los nombres de las columnas que van a tener los dataframes.
        # dfhp = pd.DataFrame(columns=hole_profile, index=range(5))
        st.session_state.dataframe2.loc[st.session_state.counter1] = [Name,Long,0,O_D,I_D]
        st.session_state.counter1 += 1
        st.session_state.dataframe2.dropna(inplace=True)
        st.dataframe(st.session_state.dataframe2, hide_index=True)
        # st.dataframe(st.session_state.dataframe2, hide_index=True)
    if final:
        st.rerun()