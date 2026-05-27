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

.stApp{
    background:#061133;
    color:white;
}

html, body, [class*="css"]{
    color:white;
    font-family:-apple-system;
}

.block-container{
    padding-top:20px;
}

.stock-card{
    border-radius:28px;
    padding:28px;
    margin-top:20px;
    margin-bottom:20px;
    color:white;
    box-shadow:0 10px 30px rgba(0,0,0,0.3);
}

.info-card{
    background:#0d1b4d;
    border-radius:20px;
    padding:18px;
    margin-top:12px;
}

.search-box input{
    background:#111c44;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================

st.markdown("""
<h1 style='font-size:56px;font-weight:900;'>
股市天氣 ☀️
</h1>

<p style='font-size:28px;color:#cfd8ff;'>
用天氣與人格，看懂股市情緒
</p>
""", unsafe_allow_html=True)

# =========================
# 搜尋
# =========================

st.markdown("## 🔍 搜尋股票")

stock_code = st.text_input(
    "",
    placeholder="輸入台股代號，例如 2330"
).strip()

# =========================
# 熱門股票
# =========================

popular = {
    "2330": "台積電",
    "2317": "鴻海",
    "2454": "聯發科",
    "2603": "長榮",
    "2881": "富邦金"
}

st.markdown("### 🔥 熱門股票")

for code, name in popular.items():
    if st.button(f"{code} {name}"):
        stock_code = code

            st.markdown(f"""
            <div class="card">
                <h2>{name} ({code})</h2>
                <h3>☀️ 晴天</h3>
                <p>人格：王者型</p>
                <h1 style="color:#4ade80;">82</h1>
            </div>
            """, unsafe_allow_html=True)

# =========================
# 股票分析
# =========================

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

        # =========================
        # 天氣判斷
        # =========================

        if change >= 3:
            weather = "晴天"
            weather_icon = "☀️"
            color = "linear-gradient(135deg,#ffb347,#ffcc33)"

        elif change >= 0:
            weather = "多雲"
            weather_icon = "⛅"
            color = "linear-gradient(135deg,#4facfe,#00f2fe)"

        elif change >= -3:
            weather = "下雨"
            weather_icon = "🌧️"
            color = "linear-gradient(135deg,#5f72bd,#9b23ea)"

        else:
            weather = "暴風雨"
            weather_icon = "⛈️"
            color = "linear-gradient(135deg,#232526,#414345)"

        # =========================
        # 人格判斷
        # =========================

        energy = random.randint(45, 98)

        if energy >= 80:
            animal = "獅王型"
            animal_icon = "🦁"

        elif energy >= 65:
            animal = "獵豹型"
            animal_icon = "🐆"

        elif energy >= 55:
            animal = "狐狸型"
            animal_icon = "🦊"

        elif energy >= 45:
            animal = "海豚型"
            animal_icon = "🐬"

        else:
            animal = "烏龜型"
            animal_icon = "🐢"

        # =========================
        # 主卡片
        # =========================

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

        # =========================
        # 人格卡
        # =========================

        st.markdown(f"""
        <div class="info-card">

        <h1>
        {animal_icon} {animal}
        </h1>

        <h3>
        能量值：{energy}/100
        </h3>

        <p style="font-size:22px;">
        AI 判定市場情緒偏向
        <b>{animal}</b>
        ，資金動能活躍。
        </p>

        </div>
        """, unsafe_allow_html=True)

        # =========================
        # AI解讀
        # =========================

        st.markdown("""
        ### 🤖 AI 情緒解讀
        """)

        if change > 0:
            st.success("市場偏多，資金流入增加。")
        else:
            st.warning("市場偏保守，短線波動提高。")

    except:
    if stock_code != "":
        st.error("股票代號錯誤")
      