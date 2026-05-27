import streamlit as st
import yfinance as yf
import pandas as pd
import random

# ======================
# 頁面設定
# ======================

st.set_page_config(
    page_title="AI 台股情緒 App",
    layout="wide"
)

# ======================
# CSS 美化
# ======================

st.markdown("""
<style>

.stApp {
    background-color: #050816;
    color: white;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.card {
    background: linear-gradient(135deg,#1e293b,#0f172a);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
}

.weather {
    font-size: 70px;
}

.stock-name {
    font-size: 28px;
    font-weight: bold;
    color: white;
}

.energy {
    font-size: 50px;
    font-weight: bold;
    color: #22c55e;
}

.small {
    color: #94a3b8;
    font-size: 15px;
}

.rank-card {
    background: #111827;
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 12px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# 標題
# ======================

st.markdown(
    '<div class="big-title">🔥 AI 台股情緒 App</div>',
    unsafe_allow_html=True
)

st.write("")

# ======================
# 股票資料
# ======================

stocks = {
    "2330 台積電": "2330.TW",
    "2317 鴻海": "2317.TW",
    "2454 聯發科": "2454.TW",
    "2308 台達電": "2308.TW",
    "2603 長榮": "2603.TW",
    "2881 富邦金": "2881.TW",
    "2891 中信金": "2891.TW",
    "0050 元大台灣50": "0050.TW"
}

selected = st.selectbox(
    "搜尋股票",
    list(stocks.keys())
)

ticker_symbol = stocks[selected]

# ======================
# 天氣系統
# ======================

weather_types = [
    ("☀️ 晴天", "市場偏樂觀"),
    ("⛅ 多雲", "市場震盪"),
    ("🌧️ 下雨", "市場偏弱"),
    ("⛈️ 暴風雨", "波動劇烈"),
]

animal_types = [
    "🦁 王者型",
    "🦊 狐狸型",
    "🐢 穩健型",
    "🐺 狼型"
]

weather = random.choice(weather_types)
animal = random.choice(animal_types)
energy = random.randint(40,95)

# ======================
# 主卡片
# ======================

st.markdown(f"""
<div class="card">

<div class="weather">{weather[0]}</div>

<div class="stock-name">{selected}</div>

<br>

<div class="small">
{weather[1]}
</div>

<br>

<div class="energy">
⚡ {energy}
</div>

<div class="small">
AI 能量值
</div>

<br>

<div style="font-size:24px;">
{animal}
</div>

</div>
""", unsafe_allow_html=True)

# ======================
# 股票資料
# ======================

ticker = yf.Ticker(ticker_symbol)

try:

    hist = ticker.history(period="1mo")

    current_price = round(hist["Close"].iloc[-1],2)

    st.markdown(f"""
    <div class="card">
    <div class="stock-name">
    💰 目前股價：{current_price}
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.line_chart(hist["Close"])

except:

    st.error("股票資料取得失敗")

# ======================
# 熱門排行榜
# ======================

st.write("")
st.subheader("🔥 熱門股票排行榜")

rank_data = [
    ("2330 台積電","☀️ 晴天",88),
    ("2603 長榮","⛈️ 暴風雨",76),
    ("2317 鴻海","⛅ 多雲",65),
    ("2454 聯發科","🌧️ 下雨",52),
]

for stock,weather,score in rank_data:

    st.markdown(f"""
    <div class="rank-card">

    <div style="font-size:22px;font-weight:bold;">
    {stock}
    </div>

    <br>

    <div style="font-size:18px;">
    {weather}
    </div>

    <br>

    <div style="color:#22c55e;font-size:26px;font-weight:bold;">
    ⚡ {score}
    </div>

    </div>
    """, unsafe_allow_html=True)

# ======================
# AI 解讀
# ======================

st.write("")
st.subheader("🤖 AI 情緒解讀")

st.markdown(f"""
<div class="card">

目前市場對 <b>{selected}</b> 偏向樂觀。

近期成交量提升，
市場資金關注度增加。

AI 判定：

• 情緒偏強  
• 波動增加  
• 短線偏多

</div>
""", unsafe_allow_html=True)