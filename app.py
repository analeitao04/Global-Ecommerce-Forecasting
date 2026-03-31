import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="E-commerce Sales Forecast", page_icon="📈", layout="centered")

@st.cache_resource 
def load_model():
    return joblib.load('modelo_rf.pkl')

model = load_model()

st.title("📈 Demand Forecasting Simulator")
st.markdown("""
This tool uses **Machine Learning** (Random Forest) to predict the quantity of products
that will be sold based on price, temporality, and economic variables.
""")

st.divider()

st.subheader("Simulation Parameters")

col1, col2 = st.columns(2)

with col1:
    price = st.number_input("Product Price (£)", min_value=0.1, max_value=500.0, value=5.95)
    month = st.slider("Sales Month", min_value=1, max_value=12, value=6)
    day_of_week = st.selectbox("Day of the Week", options=[0, 1, 2, 3, 4, 5, 6],
                               format_func=lambda x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x])

with col2:
    market = st.radio("Market", ["United Kingdom (UK)", "International"])
    is_uk = 1 if market == "United Kingdom (UK)" else 0
    gdp = st.number_input("GDP Growth (%)", value=2.0)
    inflation = st.number_input("Inflation (%)", value=1.5)

st.divider()

if st.button("Calculate Sales Forecast", use_container_width=True):

    simulation_data = pd.DataFrame([[price, month, day_of_week, is_uk, gdp, inflation]],
                                   columns=['unit_price_gbp', 'month', 'day_of_week', 'is_uk', 'gdp_growth_pct', 'inflation_consumer_pct'])

    prediction = model.predict(simulation_data)[0]

    st.success(f"### Forecast: Approximately **{int(prediction)} units** of this product will be sold.")
    st.caption("Expected margin of error (MAE): ~8 units.")
