import streamlit as st
import numpy as np
import math

st.set_page_config(
    page_title="ActuaryPro - Financial Mathematics",
    layout="wide"
)

st.title("📈 ActuaryPro")
st.subheader("Financial Mathematics Module")

menu = st.sidebar.selectbox(
    "Pilih Fitur",
    [
        "Present Value",
        "Future Value",
        "Simple Interest",
        "Compound Interest",
        "Continuous Compounding",
        "Effective Interest Rate",
        "Force of Interest",
        "Annuity Immediate",
        "Annuity Due",
        "Future Value of Annuity",
        "Loan Payment",
        "NPV",
        "Retirement Planning"
    ]
)

# ==========================
# PRESENT VALUE
# ==========================
if menu == "Present Value":

    st.header("Present Value")

    FV = st.number_input("Future Value", value=1000000.0)
    i = st.number_input("Interest Rate (%)", value=5.0)
    n = st.number_input("Years", value=5)

    pv = FV / ((1 + i/100)**n)

    st.success(f"Present Value = Rp {pv:,.2f}")

# ==========================
# FUTURE VALUE
# ==========================
elif menu == "Future Value":

    st.header("Future Value")

    PV = st.number_input("Present Value", value=1000000.0)
    i = st.number_input("Interest Rate (%)", value=5.0)
    n = st.number_input("Years", value=5)

    fv = PV * ((1 + i/100)**n)

    st.success(f"Future Value = Rp {fv:,.2f}")

# ==========================
# SIMPLE INTEREST
# ==========================
elif menu == "Simple Interest":

    st.header("Simple Interest")

    P = st.number_input("Principal", value=1000000.0)
    r = st.number_input("Rate (%)", value=5.0)
    t = st.number_input("Time", value=3)

    A = P * (1 + r/100*t)

    st.success(f"Final Amount = Rp {A:,.2f}")

# ==========================
# COMPOUND INTEREST
# ==========================
elif menu == "Compound Interest":

    st.header("Compound Interest")

    P = st.number_input("Principal", value=1000000.0)
    r = st.number_input("Rate (%)", value=5.0)
    m = st.number_input("Compounds per Year", value=12)
    t = st.number_input("Years", value=5)

    A = P*(1+r/100/m)**(m*t)

    st.success(f"Final Amount = Rp {A:,.2f}")

# ==========================
# CONTINUOUS COMPOUNDING
# ==========================
elif menu == "Continuous Compounding":

    st.header("Continuous Compounding")

    P = st.number_input("Principal", value=1000000.0)
    r = st.number_input("Rate (%)", value=5.0)
    t = st.number_input("Years", value=5)

    A = P*np.exp((r/100)*t)

    st.success(f"Final Amount = Rp {A:,.2f}")

# ==========================
# EFFECTIVE RATE
# ==========================
elif menu == "Effective Interest Rate":

    st.header("Effective Interest Rate")

    j = st.number_input("Nominal Rate (%)", value=12.0)
    m = st.number_input("Compounds per Year", value=12)

    eff = (1+j/100/m)**m - 1

    st.success(f"Effective Rate = {eff*100:.4f}%")

# ==========================
# FORCE OF INTEREST
# ==========================
elif menu == "Force of Interest":

    st.header("Force of Interest")

    i = st.number_input("Effective Rate (%)", value=5.0)

    delta = np.log(1+i/100)

    st.success(f"δ = {delta:.6f}")

# ==========================
# ANNUITY IMMEDIATE
# ==========================
elif menu == "Annuity Immediate":

    st.header("Annuity Immediate")

    i = st.number_input("Interest Rate (%)", value=5.0)
    n = st.number_input("Periods", value=10)

    v = 1/(1+i/100)

    a = (1-v**n)/(i/100)

    st.success(f"a-angle-n = {a:.6f}")

# ==========================
# ANNUITY DUE
# ==========================
elif menu == "Annuity Due":

    st.header("Annuity Due")

    i = st.number_input("Interest Rate (%)", value=5.0)
    n = st.number_input("Periods", value=10)

    v = 1/(1+i/100)

    a = (1-v**n)/(i/100)

    adue = (1+i/100)*a

    st.success(f"ä-angle-n = {adue:.6f}")

# ==========================
# FUTURE VALUE OF ANNUITY
# ==========================
elif menu == "Future Value of Annuity":

    st.header("Future Value of Annuity")

    i = st.number_input("Interest Rate (%)", value=5.0)
    n = st.number_input("Periods", value=10)

    s = ((1+i/100)**n -1)/(i/100)

    st.success(f"s-angle-n = {s:.6f}")

# ==========================
# LOAN PAYMENT
# ==========================
elif menu == "Loan Payment":

    st.header("Loan Payment")

    P = st.number_input("Loan Amount", value=100000000.0)
    i = st.number_input("Interest Rate (%)", value=10.0)
    n = st.number_input("Number of Payments", value=60)

    r = i/100/12

    PMT = P*r/(1-(1+r)**(-n))

    st.success(f"Monthly Payment = Rp {PMT:,.2f}")

# ==========================
# NPV
# ==========================
elif menu == "NPV":

    st.header("Net Present Value")

    rate = st.number_input("Discount Rate (%)", value=10.0)

    cashflows = st.text_input(
        "Cash Flows separated by comma",
        "-1000000,300000,400000,500000,600000"
    )

    cf = [float(x) for x in cashflows.split(",")]

    npv = 0

    for t, c in enumerate(cf):
        npv += c/(1+rate/100)**t

    st.success(f"NPV = Rp {npv:,.2f}")

# ==========================
# RETIREMENT PLANNING
# ==========================
elif menu == "Retirement Planning":

    st.header("Retirement Planning")

    current_age = st.number_input("Current Age", value=25)
    retirement_age = st.number_input("Retirement Age", value=60)

    monthly_expense = st.number_input(
        "Current Monthly Expense",
        value=5000000.0
    )

    inflation = st.number_input(
        "Inflation (%)",
        value=4.0
    )

    years = retirement_age-current_age

    future_expense = monthly_expense * \
                     ((1+inflation/100)**years)

    needed_fund = future_expense*12*20

    st.success(
        f"Estimated Retirement Fund = Rp {needed_fund:,.2f}"
    )
