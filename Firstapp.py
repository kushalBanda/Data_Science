from matplotlib import ticker
import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.write("""
# Simple Stock Price App

Shown are the stock **Opening Price** , **Closing Price** , **Volume** and **Dividends** !
""")

# Define the ticker symbol
tickerSymbol = st.text_input("Enter the Stock Code", )
# get the historical prices for this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for the ticker
tickerDf = tickerData.history(period='1d', start='2000-5-25', end='2021-5-25')
# Open high   Low Close  Volume  Dividends   Stock Splits


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
# Dividends
""")
st.bar_chart(tickerDf.Dividends)
