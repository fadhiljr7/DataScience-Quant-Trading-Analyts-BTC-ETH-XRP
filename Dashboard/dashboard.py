import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("main_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.set_page_config(page_title="Quant Trading Analysis",
                   page_icon="bar_chart:",
                   layout="wide")

# ----- SIDEBAR -----
st.sidebar.image("https://github.com/fadhiljr7/DataScience-Quant-Trading-Analyts-BTC-ETH-XRP/blob/3a563c4f4ede20aea5c9b409fe139a737cb8d702/Dashboard/Images/logo.png")

st.sidebar.header("Filter:")

cr_filter = st.sidebar.selectbox(
    'CRYPTOCURENCY:',
    options=['BTC/USD', 'ETH/USD', 'XRP/USD'])

min_date = df["Date"].min()
max_date = df["Date"].max()
start_date, end_date = st.sidebar.date_input(
        label='Time Period:',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = df[(df["Date"] >= str(start_date)) & 
                (df["Date"] <= str(end_date))]

# ----- MAINPAGE -----
st.title("📈 Quant Trading Analysis 📋")
st.markdown("##")

if cr_filter == 'BTC/USD':
    lowest_pr = main_df["BTC-LOW"].min()
    highest_pr = main_df["BTC-HIGH"].max()
    roi = ((highest_pr - lowest_pr) / lowest_pr) * 100
    limage = "https://github.com/fadhiljr7/DataScience-Quant-Trading-Analyts-BTC-ETH-XRP/blob/3a563c4f4ede20aea5c9b409fe139a737cb8d702/Dashboard/Images/btc.png"
    fig = px.line(main_df, x='Date', y='BTC-CLOSE', title='Bitcoin(BTC) Price Over Time').update_layout(xaxis_title="Date", yaxis_title="BTC Price (USD)")
    fig2 = px.bar(main_df, x='Date', y=['BTC-HIGH', 'BTC-LOW', 'BTC-CLOSE'], title='Bitcoin (BTC) High, Low, and Close Prices Over Time').update_layout(xaxis_title="Date", yaxis_title="Price (USD)")
    fig3 = px.scatter(main_df, x='BTC-VOLUME', y='BTC-CLOSE', title='Relationship between Trading Volume and Price').update_layout(xaxis_title="BTC Trading Volume", yaxis_title="BTC Price (USD)")
    fig4 = px.histogram(main_df, x='BTC-CLOSE', title='BTC Price Distribution over a Specific Period').update_layout(xaxis_title="BTC Price (USD)", yaxis_title="Frequency")
elif cr_filter == 'ETH/USD':
    lowest_pr = main_df["ETH-LOW"].min()
    highest_pr = main_df["ETH-HIGH"].max()
    roi = ((highest_pr - lowest_pr) / lowest_pr) * 100
    limage = "https://github.com/fadhiljr7/DataScience-Quant-Trading-Analyts-BTC-ETH-XRP/blob/3a563c4f4ede20aea5c9b409fe139a737cb8d702/Dashboard/Images/eth.png"
    fig = px.line(main_df, x='Date', y='ETH-CLOSE', title='Ethereum(ETH) Price Over Time').update_layout(xaxis_title="Date", yaxis_title="ETH Price (USD)")
    fig2 = px.bar(main_df, x='Date', y=['ETH-HIGH', 'ETH-LOW', 'ETH-CLOSE'], title='Ethereum (ETH) High, Low, and Close Prices Over Time').update_layout(xaxis_title="Date", yaxis_title="Price (USD)")
    fig3 = px.scatter(main_df, x='ETH-VOLUME', y='ETH-CLOSE', title='Relationship between Trading Volume and Price').update_layout(xaxis_title="ETH Trading Volume", yaxis_title="ETH Price (USD)")
    fig4 = px.histogram(main_df, x='ETH-CLOSE', title='ETH Price Distribution over a Specific Period').update_layout(xaxis_title="ETH Price (USD)", yaxis_title="Frequency")
elif cr_filter == 'XRP/USD':
    lowest_pr = main_df["XRP-LOW"].min()
    highest_pr = main_df["XRP-HIGH"].max()
    roi = ((highest_pr - lowest_pr) / lowest_pr) * 100
    limage = "https://github.com/fadhiljr7/DataScience-Quant-Trading-Analyts-BTC-ETH-XRP/blob/3a563c4f4ede20aea5c9b409fe139a737cb8d702/Dashboard/Images/xrp.png"
    fig = px.line(main_df, x='Date', y='XRP-CLOSE', title='Ripple(XRP) Price Over Time').update_layout(xaxis_title="Date", yaxis_title="XRP Price (USD)")
    fig2 = px.bar(main_df, x='Date', y=['XRP-HIGH', 'XRP-LOW', 'XRP-CLOSE'], title='Ripple (XRP) High, Low, and Close Prices Over Time').update_layout(xaxis_title="Date", yaxis_title="Price (USD)")
    fig3 = px.scatter(main_df, x='XRP-VOLUME', y='XRP-CLOSE', title='Relationship between Trading Volume and Price').update_layout(xaxis_title="XRP Trading Volume", yaxis_title="XRP Price (USD)")
    fig4 = px.histogram(main_df, x='XRP-CLOSE', title='XRP Price Distribution over a Specific Period').update_layout(xaxis_title="XRP Price (USD)", yaxis_title="Frequency")

left_column, mid_column, right_column,  right_column2= st.columns(4)
with left_column:
    st.subheader("Lowest Price:")
    st.subheader(f"${lowest_pr:.2f}")

with mid_column:
    st.subheader("Highest Price:")
    st.subheader(f"${highest_pr:.2f}")

with right_column:
    st.subheader("ROI:")
    st.subheader(f"{roi:.0f}%")

with right_column2:
    st.image(limage, width=120)



# ----- CHART -----
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig3, use_container_width=True)
right_column.plotly_chart(fig4, use_container_width=True)

st.write(
    """
    <div style='text-align:center;'>
        <h5>DO YOUR OWN RESET #DYOR</h5>
    </div>
    """,
    unsafe_allow_html=True
)

# ----- HIDE STREAMLIT STYLE -----
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
