from matplotlib import ticker
import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

st.write("""
# Simple Stock Analysis App

Shown are the stock **Opening Price** , **Closing Price** , **Volume** , **High** and **Low** !
""")

# Define the ticker symbol
tickerSymbol = st.text_input("Enter the Stock Code", )
# get the historical prices for this ticker
tickerData = yf.Ticker(tickerSymbol)

me = st.slider('Select a range:', min_value=date(2000, 1, 1),
               max_value=date(2021, 10, 10), format="DD/MM/YY", value=[date(2000, 1, 1), date(2021, 10, 10)])
# me = st.slider('Select a range:', min_value=2000,
#                max_value=2021, value=[2000, 2021])

# get the historical prices for the ticker
tickerDf = tickerData.history(period='1d', start=me[0], end=me[1])
# Open  Close  Volume  High  Close


st.write("""
# Opening Price
""")
st.line_chart(tickerDf.Open)

st.write("""
# Closing Price
""")
st.line_chart(tickerDf.Close)

st.write(""""
# Volume
""")
st.line_chart(tickerDf.Volume)

st.write("""
# High
""")
st.line_chart(tickerDf.High)

st.write(""""
# Low
""")
st.line_chart(tickerDf.Low)

# get recommendation data for ticker
tickerData.recommendations
