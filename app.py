import streamlit as st
import yfinance as yf
import random

# =====================
# 頁面設定
# =====================

st.set_page_config(
    page_title="股市天氣",
    page_icon="☀️",
    layout="centered"
)

# =====================
# CSS
# =====================

st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp{
    background:#04164a;
    color:white;
}

.title{
    font-size:82px;
    font-weight:900;
    color:white;
    margin-bottom:0;
    line-height:1.1;
}

.subtitle{
    font-size:34px;
    color:#dbe4ff;
    margin-top:10px;
    margin-bottom:50px;
    font-weight:600;
}

.stock-card{
    padding:40px;
    border-radius:30px;
    color:white;
    margin-top:30px;
    box-shadow:0 10px 30px rgba(0,0,0,0.35);
}

.info-card{
    background:#10236e;
    padding:30px;
    border-radius:25px;
    margin-top:20px;
}

.stButton button{
    width:100%;
    border-radius:18px;
    height:65px;
    background:#1f3275;
    color:white;
    border:none;
    font-size:24px;
    font-weight:800;
}

.stTextInput input{
    font-size:26px !important;
    font-weight:700 !important;
    color:#111 !important;
    border-radius:18px !important;
    padding:18px !important;
}

h1{
    font-weight:900 !important;
}

h2{
    font-size:38px !important;
    font-weight:800 !important;
}

h3{
    font-size:28px !important;
    font-weight:700 !important;
}

p{
    font-size:24px !important;
    line-height:1.7;
}

</style>
""", unsafe_allow_html=True)

# =====================
# 標題
# =====================

st.markdown("""
<h1 class='title'>
股市天氣 ☀️
</h1>

<p class='subtitle'>
用天氣與人格，看懂股市情緒
</p>
""", unsafe_allow_html=True)

# =====================
# 搜尋
# =====================

st.markdown("## 🔎 搜尋股票")

stock_code = st.text_input(
    "",
    placeholder="輸入台股代號，例如 2330"
).strip()

# =====================
# 熱門股票
# =====================

popular = {
    "2330":"台積電",
    "2317":"鴻海",
    "2454":"聯發科",
    "2603":"長榮",
    "2881":"富邦金"
}

st.markdown("### 🔥 熱門股票")

cols = st.columns(5)

for i, (code, name) in enumerate(popular.items()):
    with cols[i]:
        if st.button(code):
            stock_code = code

# =====================
# 股票分析
# =====================

if stock_code != "":

    try:

        ticker = yf.Ticker(f"{stock_code}.TW")
        info = ticker.info

        if "regularMarketPrice" not in info:
            st.error("股票代號錯誤")
            st.stop()

        name = info.get("shortName", "台股")
        price = info.get("regularMarketPrice", 0)
        change = info.get("regularMarketChangePercent", 0)

        # =====================
        # 天氣判斷
        # =====================

        if change >= 3:
            weather = "晴天"
            weather_icon = "☀️"
            color = "linear-gradient(135deg,#ffb347,#ffcc33)"
            animal = "獅子型"
            animal_icon = "🦁"

        elif change >= 0:
            weather = "多雲"
            weather_icon = "⛅"
            color = "linear-gradient(135deg,#4facfe,#00f2fe)"
            animal = "狐狸型"
            animal_icon = "🦊"

        elif change >= -3:
            weather = "雨天"
            weather_icon = "🌧️"
            color = "linear-gradient(135deg,#667db6,#0082c8)"
            animal = "貓咪型"
            animal_icon = "🐱"

        else:
            weather = "暴風雨"
            weather_icon = "⛈️"
            color = "linear-gradient(135deg,#232526,#414345)"
            animal = "狼王型"
            animal_icon = "🐺"

        energy = random.randint(60, 99)

        # =====================
        # 主卡片
        # =====================

        st.markdown(f"""
        <div class="stock-card"
        style="background:{color};">

            <h1 style="font-size:52px;">
            {weather_icon} {weather}
            </h1>

            <h2>
            {name}
            </h2>

            <h3>
            股票代號：{stock_code}
            </h3>

            <h1 style="font-size:72px;">
            {price}
            </h1>

            <h2>
            漲跌幅：{round(change,2)}%
            </h2>

        </div>
        """, unsafe_allow_html=True)

        # =====================
        # 人格卡
        # =====================

        st.markdown(f"""
        <div class="info-card">

            <h1>
            {animal_icon} {animal}
            </h1>

            <h2>
            能量值：{energy}/100
            </h2>

            <p style="font-size:22px;">
            AI 判定市場情緒偏向
            <b>{animal}</b>，
            資金動能活躍。
            </p>

        </div>
        """, unsafe_allow_html=True)

        # =====================
        # AI 解讀
        # =====================

        st.markdown("### 🤖 AI 情緒解讀")

        if change > 0:
            st.success("市場偏多，資金流入增加。")

        else:
            st.warning("市場偏保守，短線波動提高。")

    except:
        st.error("股票代號錯誤")