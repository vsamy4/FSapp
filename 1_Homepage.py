import streamlit as st

st.set_page_config(page_title='Financial Services App | VS', page_icon='💵', layout='centered')
st.image('sidebarlogo.png')
st.sidebar.success('Choose a service above.')
st.logo('sidebarlogo.png')

st.subheader('Select a Service from below or the sidebar.', divider='grey')

col1, col2 = st.columns(2)
col1.page_link('pages/2_Mortgage_Calculator.py', label='Mortgage Calculator', icon='1️⃣')
col2.page_link('pages/3_NPV_Calculator.py', label='NPV Calculator', icon='2️⃣')
col1.page_link('pages/4_IRR_Calculator.py', label='IRR Calculator', icon='3️⃣')
col2.page_link('pages/5_TVM_Solver.py', label='TVM Solver', icon='4️⃣')