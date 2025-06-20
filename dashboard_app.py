# Streamlit dashboard app
import streamlit as st
from xgboost_predictor import get_stock_predictions  # Make sure this function exists

st.set_page_config(page_title="Breakout Signal Dashboard", layout="wide")
st.title("📈 Breakout Signal Dashboard")

# Run prediction and display
try:
    predictions = get_stock_predictions()
    if predictions:
        for signal in predictions:
            st.success(f"Stock: {signal['stock']} | Direction: {signal['direction']} | Target: ₹{signal['target_price']}")
    else:
        st.warning("No breakout signals found today.")
except Exception as e:
    st.error(f"Error fetching signals: {e}")
