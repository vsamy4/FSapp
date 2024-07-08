import streamlit as st
import numpy as np
import numpy_financial as npf


st.set_page_config(page_title='TVM Solver', page_icon='💵')
st.title('TVM (Time, Value, Money) Solver')
st.sidebar.success('Choose a service above.')
st.logo('sidebarlogo.png')

st.divider()

st.subheader('Enter Your Data')
num_of_periods = st.number_input('N (# of periods)', min_value=0, value=0)
interest_rate = st.number_input('I% (interest rate in %)', min_value=0.0, value=0.0)
present_value = st.number_input('PV (present value)', value=0)
payment = st.number_input('PMT (period payment value)', value=0)
future_value = st.number_input('FV (future value)', value=0)
p_y = st.number_input('P/Y (payments per year)', min_value=0, value=1)
c_y = st.number_input('C/Y (amount interest is compounded per year)', min_value=0, value=1)

def calculate_n(pv, pmt, fv, i_rate):
    i_rate /= 100
    n = npf.nper(pv= pv, pmt= pmt, fv= fv, rate= i_rate)
    return n

def calculate_i_rate(pv, pmt, fv, n):
    i_rate = npf.rate(nper=n, pmt= pmt, pv= -pv, fv= fv)
    return i_rate

def calculate_pv(n, i_rate, pmt, fv):
    i_rate /= 100
    pv = npf.pv(nper=n, rate= i_rate, pmt= -pmt, fv= fv)
    return pv

def calculate_pmt(n, i_rate, pv, fv):
    i_rate /= 100
    pmt = npf.pmt(nper=n, pv= pv, rate= i_rate, fv= fv)
    return pmt

def calculate_fv(n, i_rate, pv, pmt):
    i_rate /= 100
    fv = npf.fv(nper= n, pmt= pmt, pv= pv, rate= i_rate)
    return fv

col1, col2, col3, col4, col5 = st.columns(5)
if col1.button('Solve for N'):
    num_of_periods = calculate_n(present_value, payment, future_value, interest_rate)
    st.metric('N is', value='{:.2f}'.format(num_of_periods))
if col2.button('Solve for I%'):
    interest_rate = calculate_i_rate(present_value, payment, future_value, num_of_periods)
    st.metric('I% is', value='{:.4f}'.format(interest_rate * 100) + '%')
if col3.button('Solve for PV'):
    present_value = calculate_pv(num_of_periods, interest_rate, payment, future_value)
    st.metric('PV is', value='${:,.2f}'.format(present_value))
if col4.button('Solve for PMT'):
    payment = calculate_pmt(num_of_periods, interest_rate, present_value, future_value)
    st.metric('PMT is', value='${:.2f}'.format(payment))
if col5.button('Solve for FV'):
    future_value = calculate_fv(num_of_periods, interest_rate, present_value, payment)
    st.metric('FV is', value='${:.2f}'.format(future_value))

st.divider()

st.write('Navigate to a different page below or through the sidebar.')
col1, col2 = st.columns(2)
col1.page_link('pages/2_Mortgage_Calculator.py', label='Mortgage Calculator', icon='1️⃣')
col2.page_link('pages/3_NPV_Calculator.py', label='NPV Calculator', icon='2️⃣')
col1.page_link('pages/4_IRR_Calculator.py', label='IRR Calculator', icon='3️⃣')
col2.page_link('pages/5_TVM_Solver.py', label='TVM Solver', icon='4️⃣')
col1.page_link('1_Homepage.py',label='Home Page', icon='🏠')