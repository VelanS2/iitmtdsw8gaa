# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:19:08 2022

@author: SIGNATURE MOMENTS 3
"""
import streamlit as st

text1 = st.number_input("ENTER A NUMBER(N1):")
st.markdown("")
text2 = st.number_input("ENTER A NUMBER(N2):")
st.markdown("")
text3 = st.number_input("ENTER A NUMBER(N3):")
st.markdown("")
val =  max(text1,text2,text3)
button = st.button("FIND LARGEST NUMBER")
if button == True :
    st.markdown(f"THE LARGEST OF THE 3 NUMBERS IS {val}")

