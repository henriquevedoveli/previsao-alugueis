# for run write in terminal : streamlit run main.py

import streamlit as st
import app1
import app2

emoji = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/house-with-garden_1f3e1.png'

st.set_page_config(page_title='Previsão Aluguéis', page_icon=emoji)

pages = {
    "Home":app1,
    "Sobre":app2
}

st.sidebar.title('Navegação')
selection = st.sidebar.radio(' ', list(pages.keys()))
page = pages[selection]
page.app()



