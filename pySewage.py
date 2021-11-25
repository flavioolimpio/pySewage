import streamlit as st
import pandas as pd
import numpy as np
from texts import Texts
import math
import random
import base64
from io import BytesIO
import os
from PIL import Image

st.set_page_config(page_title="pySewage",layout="wide",initial_sidebar_state="expanded")

IMAGE_SUPP = Image.open('logos.png')

st.sidebar.markdown('# Navegação:')
nav = st.sidebar.radio('Ir para:', ['Home', 'Simulation'])

#df = pd.read_excel('Data_MC.xlsx')

'''
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download csv file</a>' # decode b'abc' => abc
'''

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

if nav == 'Home':
    gettext = Texts()
    text1 = gettext.text1()
    st.markdown('# Python Sewage')
    st.markdown('{}'.format(text1), unsafe_allow_html=True)
    gettext = Texts()
    text3 = gettext.text3()
    st.markdown('{}'.format(text3), unsafe_allow_html=True)
    st.image(IMAGE_SUPP, use_column_width=True)


if nav == 'Simulation':
    st.header(r'Monte Carlo Simulation for infection prevalence estimation')

    file = st.file_uploader("Pick a file")

    if file:    
        df = pd.read_csv(file)

        FR = st.text_input('Type your waterwaste flow rate data (L/s)', )

        k_auto_manual = st.radio("Choose your parameters (alpha, beta and gamma)", ('Automatic', 'Manual'))

        if k_auto_manual == 'Automatic':

            generate = st.button("Generate")
            if generate:

                VCG = df['Genomic Copies/L']
                FR = 1866

                mc_rf_aut = []; mc_rf_uae = []; mc_rf_abc = []; mc_f = []; mc_e = []
                for i in range(1,50000+1):
                    #mc_rf_aut.append(random.normalvariate(2.11, 0.25))
                    mc_rf_abc.append(random.uniform(np.log10(6.3E5), np.log10(1.3E8)))
                    mc_f.append(random.normalvariate(149, 95))
                    mc_e.append(random.uniform(0.29, 0.55))

                RF = np.mean(mc_rf_abc); F = np.mean(mc_f); E = np.mean(mc_e);  
                df['NIP'] = (df['Genomic Copies/L'] * FR) / (RF * F * E)

                st.table(df.head())

                csv = convert_df(df)
                st.download_button(label="Download data as CSV",
                                   data=csv,
                                   file_name='table.csv',
                                   mime='text/csv')
                #st.markdown(get_table_download_link(df), unsafe_allow_html=True)


        if k_auto_manual == 'Manual':

            VCG = df['Genomic Copies/L'].values.tolist()

            col1, col2 = st.columns(2)

            with col1:
                min_alpha = st.text_input('Adicione o valor minimo do parâmetro alpha', )

            with col2:
                max_alpha = st.text_input('Adicione o valor máximo do parâmetro alpha', )

            col3, col4 = st.columns(2)

            with col3:
                media_beta = st.text_input('Adicione a média do parâmetro beta', )

            with col4:
                dp_beta = st.text_input('Adicione o desvio padrão do parâmetro beta', )

            col5, col6 = st.columns(2)

            with col5:
                min_gamma = st.text_input('Adicione o valor minimo do parâmetro gamma', )

            with col6:
                max_gamma = st.text_input('Adicione o valor máximo do parâmetro gamma', )

            generate = st.button("Generate")
            if generate:
            
                mc_rf_alpha = []; mc_f = []; mc_e = []
                for i in range(1,50000+1):
                    mc_rf_alpha.append(random.uniform(math.log10(float(min_alpha)), math.log10(float(max_alpha))))
                    #mc_rf_alpha.append(random.uniform(np.log10(6.3E5), np.log10(1.3E8)))
                    mc_f.append(random.normalvariate(float(media_beta), float(dp_beta)))
                    mc_e.append(random.uniform(float(min_gamma), float(max_gamma)))

                RF = np.mean(mc_rf_alpha, dtype='float'); F = np.mean(mc_f, dtype='float'); E = np.mean(mc_e, dtype='float');  
                
                
                NIP = [ ((x*float(FR)) / (RF * F  * E)) for x in VCG ]

                df['NIP'] = NIP

                st.table(df.head())

                csv = convert_df(df)
                st.download_button(label="Download data as CSV",
                                   data=csv,
                                   file_name='table.csv',
                                   mime='text/csv')
                
                #st.markdown(get_table_download_link(df), unsafe_allow_html=True)

    if nav == 'About':
        gettext = Texts()
        text3 = gettext.text3()
        st.markdown('{}'.format(text3), unsafe_allow_html=True)
        st.image(IMAGE_SUPP, use_column_width=True)
