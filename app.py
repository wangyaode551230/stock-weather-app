import streamlit as st
import yfinance as yf
import random

# =========================
# 頁面設定
# =========================

st.set_page_config(
    page_title="股市天氣",
    page_icon="☀️",
    layout="centered"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #f4f6f8;
    font-family: sans-serif;
}

.block-container{
    padding-top: 1rem;
    padding-bottom: 3rem;
}

.stock-card{
    background:white;
    border-radius:30px;
    padding:30px;
    margin-top:25px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
}

.energy{
    color:#28d463;
    font-size:60px;
    font-weight:bold;
}

.personality{
    font-size:32px;
    font-weight:bold;
    margin-top:10px;
}

.stock-title{
    font-size:42px;
    font-weight:bold;
}

.big-title{
    font-size:56px;
    font-weight:bold;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================

st.markdown("""
<div class="big-title">
🔥 熱門股票人格榜
</div>
""", unsafe_allow_html=True)

# =========================
# 搜尋
# =========================

search = st.text_input(
    "🔎 搜尋股票",
    placeholder="輸入股票代號，例如 2330"
)

# =========================
# 股票列表
# =========================

stocks = {
    "2330":"台積電",
    "2317":"鴻海",
    "2454":"聯發科",
    "2603":"長榮",
    "2881":"富邦金"
}

# =========================
# 股票卡片
# =========================

for code,name in stocks.items():

    if search != "":
        if search not in code and search not in name:
            continue

    try:

        ticker = yf.Ticker(f"{code}.TW")
        info = ticker.info

        price = info.get("regularMarketPrice","--")
        change = info.get("regularMarketChangePercent",0)

        # AI 人格

        if change >= 3:
            icon = "🦁"
            personality = "獅王型"

        elif change >= 0:
            icon = "🐺"
            personality = "狼型"

        elif change >= -3:
            icon = "🐢"
            personality = "穩健型"

        else:
            icon = "🦊"
            personality = "狡猾型"

        energy = random.randint(40,95)

        st.markdown(f"""
        <div class="stock-card">

            <div class="stock-title">
            {icon} {code} {name}
            </div>

            <h2>
            即時股價：{price}
            </h2>

            <h2>
            漲跌幅：{round(change,2)}%
            </h2>

            <div class="personality">
            {personality}
            </div>

            <div class="energy">
            ⚡ {energy}
            </div>

        </div>
        """, unsafe_allow_html=True)

    except:
        st.error(f"{code} 資料讀取失敗")