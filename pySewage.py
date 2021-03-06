import streamlit as st
import pandas as pd
import numpy as np
from texts import Texts
import math
import random
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="pySewage")

IMAGE_SUPP = Image.open('logos.png')

latext = r''' 
$$ 
NIP = \frac{VGC\cdot FR}{\alpha\cdot\beta\cdot\gamma}
$$ 
'''

#st.sidebar.markdown('# Navigation:')
#nav = st.sidebar.radio('Go to:', ['HOME', 'Simulation', 'Citation', 'Contact'])
        
with st.sidebar:
    nav = option_menu('Navegation:', ['HOME', 'Simulation', 'Citation', 'Contact'], 
    icons=['house', 'water', 'journal-check',  'chat-left-text-fill'], menu_icon="cast", default_index=0)
        
gettext = Texts()
text1_1 = gettext.text1_1()
text4 = gettext.text4()
st.sidebar.markdown('# Contribute')
st.sidebar.info('{}'.format(text4))

filecsv = pd.read_csv("template.csv")

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

def local_css(file_name):
    with open(file_name) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if nav == 'HOME':
    gettext = Texts()
    
    text1 = gettext.text1()
    st.markdown('# pySewage')
    st.markdown('{}'.format(text1), unsafe_allow_html=True)
    
    st.write(latext)
    
    text2 = gettext.text2()
    st.markdown('{}'.format(text2), unsafe_allow_html=True)
    
    csv = convert_df(filecsv)
    st.download_button(label="Download template csv",
                                   data=csv,
                                   file_name='template.csv',
                                   mime='text/csv')
    
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


        if k_auto_manual == 'Manual':

            VCG = df['Genomic Copies/L'].values.tolist()

            col1, col2 = st.columns(2)

            with col1:
                min_alpha = st.text_input('Add the minimum alpha parameter value', )

            with col2:
                max_alpha = st.text_input('Add the maximum value of the alpha parameter', )

            col3, col4 = st.columns(2)

            with col3:
                media_beta = st.text_input('Add the average of the beta parameter', )

            with col4:
                dp_beta = st.text_input('Add the standard deviation of the beta parameter', )

            col5, col6 = st.columns(2)

            with col5:
                min_gamma = st.text_input('Add the minimum value of the gamma parameter', )

            with col6:
                max_gamma = st.text_input('Add the maximum value of the gamma parameter', )

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

if nav == 'Citation':
    st.markdown('{}'.format(text1_1), unsafe_allow_html=True)


if nav == 'Contact':
    #st.header(":mailbox: Entre em contato comigo!!")
    st.header("Contact me!!")
    contact_form = """
    <form action="https://formsubmit.co/adrianoarvs@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" optional>
     <input type="email" name="email" placeholder="Your e-mail" optional>
     <textarea name="message" placeholder="Type your message here"></textarea>
     <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    local_css("style/style.css")



