import streamlit as st

st.set_page_config(page_title='Mortgage Calculator', page_icon='💵')
st.title('Mortgage Payment Calculator')
st.sidebar.success('Choose a service above.')
st.logo('sidebarlogo.png')

st.divider()

st.subheader('Enter Your Data')
col1, col2, col3, col4 = st.columns(4)
principal = col1.number_input('Prinicipal Amount', min_value=0, value=500000)
deposit = col2.number_input('Initial Deposit Amount', min_value=0, value=100000)
interest_rate = col3.number_input('Interest Rate (in %)', min_value=0.0, value=5.0)
years = col4.number_input('Mortgage Term (in years)', min_value=1, value=30)

initial_value = principal - deposit
monthly_rate = (interest_rate / 12) / 100
months = years * 12
monthly_payment = initial_value * ((monthly_rate * ((1 + monthly_rate)** months)) / (((1 + monthly_rate) ** months) - 1))

total_payment = monthly_payment * months
total_interest = total_payment - initial_value

st.subheader('Payment Values')
col1, col2 = st.columns(2)
col1.metric('Monthly Payments', value="${:,.2f}".format(monthly_payment))
col1.metric('Total Payments', value="${:,.2f}".format(total_payment))
col2.metric('Total Interest Paid', value="${:,.2f}".format(total_interest))
col2.metric('Total Principal Paid (after initial deposit)', value="${:,.2f}".format(initial_value))

st.divider()

st.write('Navigate to a different page below or through the sidebar.')
col1, col2 = st.columns(2)
col1.page_link('pages/2_Mortgage_Calculator.py', label='Mortgage Calculator', icon='1️⃣')
col2.page_link('pages/3_NPV_Calculator.py', label='NPV Calculator', icon='2️⃣')
col1.page_link('pages/4_IRR_Calculator.py', label='IRR Calculator', icon='3️⃣')
col2.page_link('pages/5_TVM_Solver.py', label='TVM Solver', icon='4️⃣')
col1.page_link('1_Homepage.py',label='Home Page', icon='🏠')