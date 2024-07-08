import streamlit as st

st.set_page_config(page_title='NPV Calculator', page_icon='💵')
st.title('Net Present Value (NPV) Calculator')
st.sidebar.success('Choose a service above.')
st.logo('sidebarlogo.png')

st.divider()

st.subheader('Enter Your Data')
col1, col2, col3 = st.columns(3)
discount_rate = col1.number_input('Discount Rate (in %)', min_value=0.0, value=0.0)
initial_investment = col2.number_input('Initial Investment (in USD)', min_value=0, value=0)
total_cashflows = col3.number_input('Number of Cash Flows', min_value=0, value=0)

st.subheader('Enter Your Cash Flows')
st.write('Cashflow input boxes will appear once the total number of cashflows is specified.')
cashflows = []
for x in range(0, total_cashflows):
    cashflow = st.number_input(f'Enter the Cash Flow for Year {x+1} (in USD)', min_value=0, value=0, key=f'cashflow_{x}')
    if cashflow != 0:
        cashflows.append(cashflow)

st.subheader('Net Present Value')
npv = 0.0
if st.button('Click to Calculate NPV'):
    cashflows.insert(0, -initial_investment)
    for i, cflow in enumerate(cashflows):
        npv += cflow / (1 + (discount_rate / 100))**i
    st.metric('NPV is', value="${:,.2f}".format(npv))

st.divider()

st.write('Navigate to a different page below or through the sidebar.')
col1, col2 = st.columns(2)
col1.page_link('pages/2_Mortgage_Calculator.py', label='Mortgage Calculator', icon='1️⃣')
col2.page_link('pages/3_NPV_Calculator.py', label='NPV Calculator', icon='2️⃣')
col1.page_link('pages/4_IRR_Calculator.py', label='IRR Calculator', icon='3️⃣')
col2.page_link('pages/5_TVM_Solver.py', label='TVM Solver', icon='4️⃣')
col1.page_link('1_Homepage.py',label='Home Page', icon='🏠')
            







