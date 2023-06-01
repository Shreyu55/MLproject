# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:57:31 2023

@author: shrey
"""

import streamlit as st
import joblib

def main():
    html_temp = """ 
    <div style = "backfround-color:Lightblue;padding:16px">
    <h2 style ="color:Green";text-align:center>Insurance Predicative Analysis
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    # load the model
    model = joblib.load('model_joblib_gr')
    
    p1 = st.slider("Enter Your Age",18,100)
    
    s1=st.selectbox("Sex",("Male","Female"))
    if s1=="Male":
        p2=1
    else:
        p2=0

    p3 =st.number_input("Enter Your BMI Value")
    p4 = st.selectbox("Enter Number of Children",(0,1,2,4)) 
    
    s2=st.selectbox("Smoker",("Yes","No"))
    if s2=="Yes":
        p5=1
    else:
        p5=0
        
    p6 = st.slider("Enter Your Region [1-4]",1,4)
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.success('Insurance Amount is {} '.format(round(prediction[0],2)))  
    
if __name__ == '__main__':
    main()