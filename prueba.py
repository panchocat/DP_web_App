# ---- Modules ------- 
import streamlit as st
import pandas as pd
import plotly.express as px

if "load" not in st.session_state:
     st.session_state.load = False

st.header("Fruits List")
# ---- Creating Dictionary ----
_dic = { 'Name': ['Mango', 'Apple', 'Banana'],
         'Quantity': [45, 38, 90]}
# load = st.button('Load Data')
# if load:

boton = st.button('load')
if boton or st.session_state.load:
   st.session_state.load = True
   _df = pd.DataFrame(_dic)
   st.write(_df)
   
   # ---- Plot types -------
   opt = st.radio('Plot type :',['Bar', 'Pie'])
   if opt == 'Bar':
      fig = px.bar(_df, x= 'Name',
                   y = 'Quantity',title ='Bar Chart')
      st.plotly_chart(fig)
   
   else:     
      fig = px.pie(_df,names = 'Name',
                   values = 'Quantity',title ='Pie Chart')
      st.plotly_chart(fig)
print(boton)
print(st.session_state.load)
print(boton or st.session_state.load)