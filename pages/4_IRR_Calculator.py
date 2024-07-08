import streamlit as st
import numpy_financial as npf

st.set_page_config(page_title='IRR Calculator', page_icon='💵')
st.title('Internal Rate of Return (IRR) Calculator')
st.sidebar.success('Choose a service above.')
st.logo('sidebarlogo.png')

st.divider()

st.subheader('Enter Your Data')
col1, col2 = st.columns(2)
initial_investment = col1.number_input('Initial Investment (in USD)', min_value=0, value=0)
total_cashflows = col2.number_input('Number of Cash Flows', min_value=0, value=0)

st.subheader('Enter Your Cash Flows')
st.write('Cashflow input boxes will appear once the total number of cashflows is specified.')
cashflows = []
for x in range(0, total_cashflows):
    cashflow = st.number_input(f'Enter the Cash Flow for Year {x+1} (in USD)', value=0, key=f'cashflow_{x}')
    if cashflow != 0:
        cashflows.append(cashflow)

st.subheader('Internal Rate of Return')
irr = 0.0
if st.button('Click to Calculate IRR'):   
    cashflows.insert(0, -initial_investment)
    irr = npf.irr(cashflows)
    irr *= 100
    st.metric('IRR is', value='{:.3f}'.format(irr) + '%')


st.divider()

st.write('Navigate to a different page below or through the sidebar.')
col1, col2 = st.columns(2)
col1.page_link('pages/2_Mortgage_Calculator.py', label='Mortgage Calculator', icon='1️⃣')
col2.page_link('pages/3_NPV_Calculator.py', label='NPV Calculator', icon='2️⃣')
col1.page_link('pages/4_IRR_Calculator.py', label='IRR Calculator', icon='3️⃣')
col2.page_link('pages/5_TVM_Solver.py', label='TVM Solver', icon='4️⃣')
col1.page_link('1_Homepage.py',label='Home Page', icon='🏠')