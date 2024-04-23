import streamlit as st
import pandas as pd
import numpy as np
import math
import random
from PIL import Image
from streamlit_option_menu import option_menu
from texts import Texts

def convert_df(df):
    return df.to_csv(index=False, index_label=None).encode('utf-8')

def parameter_inputs(selected_virus=None):
    col1, col2, col3 = st.columns(3)
    
    if selected_virus == 'DENV':
        with col1:
            min_alpha = st.text_input('Minimum alpha', value='2.1')
        with col2:
            max_alpha = st.text_input('Maximum alpha', value='3.8')
        with col3:
            alpha_description = st.empty()  # Placeholder for alpha description
        
        col4, col5, col6 = st.columns(3)
    
        with col4:
            media_beta = st.text_input('Average beta', value='3.1')
        with col5:
            dp_beta = st.text_input('Standard deviation of beta', value='0.15')
        with col6:
            beta_description = st.empty()  # Placeholder for beta description
        
        col7, col8, col9 = st.columns(3)
        
        with col7:
            min_gamma = st.text_input('Minimum gamma', value='0.25')
        with col8:
            max_gamma = st.text_input('Maximum gamma', value='0.80')
        with col9:
            gamma_description = st.empty()  # Placeholder for gamma description

    elif selected_virus == 'ZIKV':
        with col1:
            min_alpha = st.text_input('Minimum alpha', value='5.85')
        with col2:
            max_alpha = st.text_input('Maximum alpha', value='8.34')
        with col3:
            alpha_description = st.empty()  # Placeholder for alpha description

        col4, col5, col6 = st.columns(3)
    
        with col4:
            media_beta = st.text_input('Average beta', value='3.1')
        with col5:
            dp_beta = st.text_input('Standard deviation of beta', value='0.15')
        with col6:
            beta_description = st.empty()  # Placeholder for beta description
        
        col7, col8, col9 = st.columns(3)
        
        with col7:
            min_gamma = st.text_input('Minimum gamma', value='0.25')
        with col8:
            max_gamma = st.text_input('Maximum gamma', value='0.80')
        with col9:
            gamma_description = st.empty()  # Placeholder for gamma description

    elif selected_virus == 'CHIKV':
        with col1:
            min_alpha = st.text_input('Minimum alpha', value='2.84')
        with col2:
            max_alpha = st.text_input('Maximum alpha', value='5.83')
        with col3:
            alpha_description = st.empty()  # Placeholder for alpha description

        col4, col5, col6 = st.columns(3)
    
        with col4:
            media_beta = st.text_input('Average beta', value='3.1')
        with col5:
            dp_beta = st.text_input('Standard deviation of beta', value='0.15')
        with col6:
            beta_description = st.empty()  # Placeholder for beta description
        
        col7, col8, col9 = st.columns(3)
        
        with col7:
            min_gamma = st.text_input('Minimum gamma', value='0.25')
        with col8:
            max_gamma = st.text_input('Maximum gamma', value='0.80')
        with col9:
            gamma_description = st.empty()  # Placeholder for gamma description

    else:
        with col1:
            min_alpha = st.text_input('Minimum alpha', value='6.3E5')
        with col2:
            max_alpha = st.text_input('Maximum alpha', value='1.3E8')
        with col3:
            alpha_description = st.empty()  # Placeholder for alpha description
        
        col4, col5, col6 = st.columns(3)
    
        with col4:
            media_beta = st.text_input('Average beta', value='149')
        with col5:
            dp_beta = st.text_input('Standard deviation of beta', value='95')
        with col6:
            beta_description = st.empty()  # Placeholder for beta description
        
        col7, col8, col9 = st.columns(3)
        
        with col7:
            min_gamma = st.text_input('Minimum gamma', value='0.25')
        with col8:
            max_gamma = st.text_input('Maximum gamma', value='0.80')
        with col9:
            gamma_description = st.empty()  # Placeholder for gamma description
    
    return min_alpha, max_alpha, media_beta, dp_beta, min_gamma, max_gamma

def generate_parameters_auto(selected_virus=None):
    if selected_virus == 'DENV':
        mc_rf_abc = [random.uniform(2.1, 3.8) for _ in range(50000)]
        mc_f = [random.normalvariate(3.1, 0.15) for _ in range(50000)]
        mc_e = [random.betavariate(0.25, 0.80) for _ in range(50000)]
    elif selected_virus == 'ZIKV':
        mc_rf_abc = [random.uniform(5.85, 8.34) for _ in range(50000)]
        mc_f = [random.normalvariate(3.1, 0.15) for _ in range(50000)]
        mc_e = [random.betavariate(0.25, 0.80) for _ in range(50000)]
    elif selected_virus == 'CHIKV':
        mc_rf_abc = [random.uniform(2.84, 5.83) for _ in range(50000)]
        mc_f = [random.normalvariate(3.1, 0.15) for _ in range(50000)]
        mc_e = [random.betavariate(0.25, 0.80) for _ in range(50000)]
    else:
        mc_rf_abc = [random.uniform(np.log10(6.3E5), np.log10(1.3E8)) for _ in range(50000)]
        mc_f = [random.normalvariate(149, 95) for _ in range(50000)]
        mc_e = [random.uniform(0.30, 0.90) for _ in range(50000)]

    RF = np.mean(mc_rf_abc)
    F = np.mean(mc_f)
    E = np.mean(mc_e)

    return RF, F, E

def generate_parameters_manual(min_alpha, max_alpha, media_beta, dp_beta, min_gamma, max_gamma, selected_virus=None):
    if selected_virus == 'DENV':
        mc_rf_alpha = [random.uniform(float(min_alpha), float(max_alpha)) for _ in range(50000)]
        mc_f = [random.normalvariate(float(media_beta), float(dp_beta))  for _ in range(50000)]
        mc_e = [random.betavariate(float(min_gamma), float(max_gamma)) for _ in range(50000)]

    elif selected_virus == 'ZIKV':
        mc_rf_alpha = [random.uniform(float(min_alpha), float(max_alpha)) for _ in range(50000)]
        mc_f = [random.normalvariate(float(media_beta), float(dp_beta))  for _ in range(50000)]
        mc_e = [random.betavariate(float(min_gamma), float(max_gamma)) for _ in range(50000)]
    
    elif selected_virus == 'CHIKV':
        mc_rf_alpha = [random.uniform(float(min_alpha), float(max_alpha)) for _ in range(50000)]
        mc_f = [random.normalvariate(float(media_beta), float(dp_beta))  for _ in range(50000)]
        mc_e = [random.betavariate(float(min_gamma), float(max_gamma)) for _ in range(50000)]

    else: 
        mc_rf_alpha = [random.uniform(np.log10(float(min_alpha)), np.log10(float(max_alpha))) for _ in range(50000)]
        mc_f = [random.normalvariate(float(media_beta), float(dp_beta)) for _ in range(50000)]
        mc_e = [random.uniform(float(min_gamma), float(max_gamma)) for _ in range(50000)]

    RF = np.mean(mc_rf_alpha)
    F = np.mean(mc_f)
    E = np.mean(mc_e)

    return RF, F, E


def run_simulation(df, FR, RF, F, E):
    FR = float(FR)
    print(type(df.iloc[0:, 0][0]))
    NIP = (df.iloc[0:, 0].astype(float) * float(FR)) / (RF * F * E)
    df['NIP'] = NIP

    st.table(df.head())
    csv = convert_df(df)
    print(csv)
    st.download_button(label="Download data as CSV",
                       data=csv,
                       file_name='table.csv',
                       mime='text/csv')

st.set_page_config(page_title="pySewage")
latext = r''' 
$$ 
NIP = \frac{VGC\cdot FR}{\alpha\cdot\beta\cdot\gamma}
$$ 
'''

with st.sidebar:
    nav = option_menu('Navigation:', ['HOME', 'Simulation SARS-CoV-2', 'Simulation Arboviruses',  'Citation', 'Contact'], 
                      icons=['house', 'water', 'bug', 'journal-check',  'chat-left-text-fill'], menu_icon="cast", default_index=0)

gettext = Texts()
text1_1 = gettext.text1_1()
text4 = gettext.text4()
st.sidebar.markdown('# Contribute')
st.sidebar.info('{}'.format(text4))

filecsv = pd.read_csv("template.csv")

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
    IMAGE_SUPP = Image.open('logos.png')
    st.image(IMAGE_SUPP, use_column_width=True)

if nav == 'Simulation SARS-CoV-2':
    st.header(r'Monte Carlo Simulation for SARS-CoV-2 infection prevalence estimation.')
    session_id = "session_1"
    file1 = st.file_uploader("Pick a file", key=session_id)
    if file1:    
        df = pd.read_csv(file1)  # Não há necessidade de pular a primeira linha
        FR = st.text_input('Type your waterwaste flow rate data (L/day)', )
        k_auto_manual = st.radio("Choose your parameters (alpha, beta and gamma)", ('Automatic', 'Manual'))
        if k_auto_manual == 'Automatic':
            generate = st.button("Generate")
            if generate:
                #VCG = df.iloc[1:, 0].tolist()
                RF, F, E = generate_parameters_auto()
                run_simulation(df, FR, RF, F, E)
        elif k_auto_manual == 'Manual':
            #VCG_column = df.iloc[1:, 0].tolist()
            min_alpha, max_alpha, media_beta, dp_beta, min_gamma, max_gamma = parameter_inputs()
            generate = st.button("Generate")
            if generate:
                RF, F, E = generate_parameters_manual(min_alpha, max_alpha, media_beta, dp_beta, min_gamma, max_gamma)
                run_simulation(df, FR, RF, F, E)

elif nav == 'Simulation Arboviruses':
    st.header(r'Monte Carlo Simulation for arboviruses infection prevalence estimation.')
    session_id = "session_2"
    file2 = st.file_uploader("Pick a file", key=session_id)
    if file2:    
        df = pd.read_csv(file2)
        FR = st.text_input('Type your waterwaste flow rate data (L/person/day)', )
        arbovirus = st.selectbox("Choose the arbovirus:", ['DENV', 'ZIKV', 'CHIKV'])
        k_auto_manual = st.radio("Choose your parameters (alpha, beta and gamma)", ('Automatic', 'Manual'))
        if k_auto_manual == 'Automatic':
            generate = st.button("Generate")
            if generate:
                #VCG = df.iloc[1:, 0].tolist()
                RF, F, E = generate_parameters_auto(arbovirus)
                run_simulation(df, FR, RF, F, E)
        elif k_auto_manual == 'Manual':
            #VCG = df.iloc[1:, 0].tolist()
            min_alpha, max_alpha, media_beta, dp_beta, min_gamma, max_gamma = parameter_inputs(arbovirus)
            generate = st.button("Generate")
            if generate:
                RF, F, E = generate_parameters_manual(min_alpha, max_alpha, media_beta, dp_beta, min_gamma, max_gamma, arbovirus)
                run_simulation(df, FR, RF, F, E)

if nav == 'Citation':
    st.markdown('{}'.format(text1_1), unsafe_allow_html=True)

if nav == 'Contact':
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
