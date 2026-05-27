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
<div style="
background: linear-gradient(135deg,#1e3a8a,#0f172a);
padding:35px;
border-radius:30px;
margin-bottom:25px;
box-shadow:0 0 30px rgba(0,0,0,0.5);
">

<div style="font-size:85px;">
{weather[0]}
</div>

<div style="
font-size:42px;
font-weight:bold;
color:white;
margin-top:10px;
">
{selected}
</div>

<div style="
font-size:22px;
color:#cbd5e1;
margin-top:8px;
">
{weather[1]}
</div>

<br>

<div style="
background:#111827;
padding:20px;
border-radius:20px;
margin-top:10px;
">

<div style="
font-size:18px;
color:#94a3b8;
">
AI 能量值
</div>

<div style="
font-size:60px;
font-weight:bold;
color:#22c55e;
">
⚡ {energy}
</div>

<div style="
width:100%;
height:16px;
background:#1e293b;
border-radius:30px;
overflow:hidden;
margin-top:10px;
">

<div style="
width:{energy}%;
height:100%;
background:linear-gradient(90deg,#22c55e,#4ade80);
border-radius:30px;
">
</div>

</div>

</div>

<br>

<div style="
background:linear-gradient(135deg,#78350f,#451a03);
padding:22px;
border-radius:25px;
">

<div style="
font-size:32px;
font-weight:bold;
">
{animal}
</div>

<div style="
font-size:18px;
color:#fde68a;
margin-top:10px;
">

AI 判定此股票近期市場關注度提升，
資金動能偏強，
短線情緒偏多。

</div>

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

rank_data = []

top_stocks = [
    ("2330","台積電"),
    ("2603","長榮"),
    ("2317","鴻海"),
    ("2454","聯發科"),
    ("2881","富邦金")
]

for code,name in top_stocks:

    try:

        ticker = yf.Ticker(f"{code}.TW")

        hist = ticker.history(period="5d")

        if len(hist) >= 2:

            close_now = hist["Close"].iloc[-1]

            close_old = hist["Close"].iloc[-2]

            change = ((close_now - close_old) / close_old) * 100

            volume = hist["Volume"].iloc[-1]

            avg_volume = hist["Volume"].mean()

            # ======================
            # AI 情緒判斷
            # ======================

            if change >= 4:

                weather = "🔥 火山"

                score = 95

                animal = "🦁"

            elif change >= 2:

                weather = "☀️ 晴天"

                score = 82

                animal = "🐺"

            elif change >= 0:

                weather = "☁️ 多雲"

                score = 65

                animal = "🐢"

            elif change >= -3:

                weather = "🌧️ 下雨"

                score = 42

                animal = "🦊"

            else:

                weather = "⛈️ 暴風雨"

                score = 20

                animal = "🐍"

            # 成交量爆增加分

            if volume > avg_volume * 1.5:

                score += 5

            score = min(score,100)

            rank_data.append(
                (
                    f"{code} {name}",
                    weather,
                    score,
                    animal,
                    round(change,2)
                )
            )

    except:
        pass


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