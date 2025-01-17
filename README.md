# Personalized storytelling nudge with Phi-3
This is a Python streamlit app to demonstrate the fesability of leveraging LLM (well, technically phi-3 is a small language model) in behavioral science experiment design. 
This app uses socio-demographic data of experiment subject to create relevant story to nudge subject to seek more information on investment.  

## Technical details
I deployed phi-3-mini on Azure and called its API in my app. The reason to choose phi-3 is that Azure provides serverless API for phi-3, which means it doesn't involve GPU or CPU resources to deploy phi-3 and the billing is based on the consumed tokens. Although ChatGPT-4 seems to perform better than phi-3 in its more accurate recommendation of investment products, phi-3 is enough for a proof-of-concept purpose. 

## App demo
Please see the app_demo.gif 

## App interface

![app interface](https://github.com/claudiatang95/storynudge/blob/main/nudge_app.png)
