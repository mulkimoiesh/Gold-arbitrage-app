
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Gold Arbitrage Signal", layout="centered")

st.title("Gold Arbitrage Signal")
st.markdown("Live comparison of COMEX gold vs Indian GOLDBEES ETF")

# Fetch live prices
try:
    comex = yf.Ticker("GC=F").info['regularMarketPrice']
    usd_inr = yf.Ticker("USDINR=X").info['regularMarketPrice']
    gldbees = yf.Ticker("GOLDBEES.BO").info['regularMarketPrice']

    comex_inr_gram = (comex * usd_inr) / 31.1035
    etf_fair = comex_inr_gram * 0.01
    discount = (etf_fair - gldbees) / etf_fair * 100

    if discount > 2:
        signal = "BUY"
    elif discount < -2:
        signal = "SELL"
    else:
        signal = "HOLD"

    st.metric("COMEX Gold (USD/oz)", f"${comex:.2f}")
    st.metric("USD to INR", f"₹{usd_inr:.2f}")
    st.metric("COMEX (INR/gram)", f"₹{comex_inr_gram:.2f}")
    st.metric("Fair ETF Value", f"₹{etf_fair:.2f}")
    st.metric("GOLDBEES Price", f"₹{gldbees:.2f}")
    st.metric("Discount / Premium (%)", f"{discount:.2f}%")
    st.header(f"Signal: {signal}")

except Exception as e:
    st.error("Error fetching data. Please try again later.")
