# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:38:10 2022

@author: 91971
"""

import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:white";text-align:center>Crop Prediction</h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    model = joblib.load("model_joblib_cp")
    
    f1 = st.text_input("Enter the Tempurature")
    
    f2 = st.text_input("Enter Humidity")

    f3 = st.text_input("Enter ph")
    f4 = st.text_input("Enter Rainfall")
    
    if st.button("Predict"):
        pred="none"
        pred = model.predict([[float(f1),float(f2),float(f3),float(f4)]])
        
        crops=['Black gram', 'Chickpea','Coconut', 'Coffee', 'Cotton', 'Ground Nut', 'Jute', 'Kidney Beans',
       'Lentil', 'Moth Beans', 'Mung Bean', 'Peas', 'Pigeon Peas', 'Rubber',
       'Sugarcane', 'Tea', 'Tobacco', 'apple', 'banana', 'grapes', 'maize',
       'mango', 'millet', 'muskmelon', 'orange', 'papaya', 'pomegranate',
       'rice', 'watermelon', 'wheat']
        
        c="none"
        for i in range(0,30):
            if(pred[0][i]==1):
                c=crops[i]
                st.success(c)
                break;      



if __name__ == '__main__':
    main()