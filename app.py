import streamlit as st
import yfinance as yf
import random

# ======================
# 頁面設定
# ======================

st.set_page_config(
    page_title="股市天氣",
    page_icon="🌤️",
    layout="centered"
)

# ======================
# CSS
# ======================

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #06153a;
    color: white;
    font-family: sans-serif;
}

.block-container{
    padding-top: 1rem;
    padding-bottom: 3rem;
}

h1,h2,h3,p{
    color:white;
}

.search-box input{
    background:#111c44 !important;
    color:white !important;
    border-radius:20px !important;
    border:none !important;
    height:60px !important;
    font-size:24px !important;
}

.stock-card{
    padding:25px;
    border-radius:28px;
    margin-top:20px;
    background: linear-gradient(135deg,#1f3c88,#39a0ff);
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.info-card{
    padding:22px;
    border-radius:24px;
    background:#101b46;
    margin-top:18px;
}

.small-card{
    padding:18px;
    border-radius:22px;
    background:#111c44;
    margin-top:14px;
}

.energy{
    font-size:68px;
    font-weight:bold;
    color:#62ff9c;
}

.hot-btn button{
    width:100%;
    background:#13255f;
    color:white;
    border:none;
    border-radius:18px;
    height:60px;
    font-size:20px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# 標題
# ======================

st.markdown("""
<h1 style='font-size:58px;'>
股市天氣 🌤️
</h1>

<p style='font-size:24px;color:#b8c7ff;'>
用天氣與人格，看懂股市情緒
</p>
""", unsafe_allow_html=True)

# ======================
# 搜尋
# ======================

st.markdown("## 🔎 搜尋股票")

stock_code = st.text_input(
    "",
    placeholder="輸入股票代號，例如 2330"
)

# ======================
# 熱門股票
# ======================

popular = {
    "2330":"台積電",
    "2317":"鴻海",
    "2454":"聯發科",
    "2603":"長榮",
    "2881":"富邦金"
}

st.markdown("## 🔥 熱門股票")

cols = st.columns(2)

i = 0
for code,name in popular.items():

    with cols[i % 2]:
        st.markdown("<div class='hot-btn'>", unsafe_allow_html=True)

        if st.button(f"{code} {name}"):

            stock_code = code

        st.markdown("</div>", unsafe_allow_html=True)

    i += 1

# ======================
# 股票分析
# ======================

if stock_code != "":

    try:

        ticker = yf.Ticker(f"{stock_code}.TW")
        info = ticker.info

        if "regularMarketPrice" not in info:
            st.error("股票代號錯誤")
            st.stop()

        name = info.get("shortName","台股")
        price = info.get("regularMarketPrice",0)
        change = info.get("regularMarketChangePercent",0)

        # ======================
        # 天氣
        # ======================

        if change >= 3:
            weather = "晴天"
            icon = "☀️"
            color = "linear-gradient(135deg,#f6b73c,#ff7e5f)"
            animal = "王者型 🦁"

        elif change >= 0:
            weather = "多雲"
            icon = "⛅"
            color = "linear-gradient(135deg,#4facfe,#00f2fe)"
            animal = "穩健型 🐢"

        elif change >= -3:
            weather = "下雨"
            icon = "🌧️"
            color = "linear-gradient(135deg,#667db6,#0082c8)"
            animal = "狡猾型 🦊"

        else:
            weather = "暴風雨"
            icon = "⛈️"
            color = "linear-gradient(135deg,#232526,#414345)"
            animal = "猴型 🐺"

        energy = random.randint(45,95)

        # ======================
        # 主卡片
        # ======================

        st.markdown(f"""
        <div class='stock-card'
        style='background:{color};'>

        <h1 style='font-size:52px;'>
        {icon} {weather}
        </h1>

        <h2 style='font-size:42px;'>
        {name}
        </h2>

        <h3 style='font-size:26px;'>
        股票代號：{stock_code}
        </h3>

        <h1 style='font-size:82px;'>
        {price}
        </h1>

        <h2>
        漲跌幅：{round(change,2)}%
        </h2>

        </div>
        """, unsafe_allow_html=True)

        # ======================
        # AI人格
        # ======================

        st.markdown(f"""
        <div class='info-card'>

        <h1>
        🤖 AI 人格分析
        </h1>

        <h2>
        {animal}
        </h2>

        <p style='font-size:22px;line-height:1.8;'>

        AI 判定目前市場情緒偏向
        <b>{animal}</b>，
        資金流動活躍，
        市場關注度提高。

        </p>

        </div>
        """, unsafe_allow_html=True)

        # ======================
        # 能量值
        # ======================

        st.markdown(f"""
        <div class='small-card'>

        <h2>
        ⚡ 市場能量值
        </h2>

        <div class='energy'>
        {energy}
        </div>

        <p style='font-size:22px;color:#cbd5ff;'>

        AI 綜合成交量、
        價格波動、
        市場情緒分析。

        </p>

        </div>
        """, unsafe_allow_html=True)

    except:
        st.error("股票代號錯誤")