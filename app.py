import streamlit as st
import yfinance as yf
import pandas as pd
import random

st.set_page_config(
    page_title="股市天氣",
    page_icon="🌤️",
    layout="wide"
)

# =========================
# CSS 美化
# =========================
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #07111f;
    color: white;
    font-family: sans-serif;
}

.main-title {
    font-size: 48px;
    font-weight: bold;
    color: white;
}

.sub-title {
    color: #A0AEC0;
    font-size: 20px;
}

.weather-card {
    background: linear-gradient(135deg,#1e3c72,#2a5298);
    padding: 30px;
    border-radius: 25px;
    color: white;
    margin-bottom: 20px;
}

.personality-card {
    background: linear-gradient(135deg,#134E5E,#71B280);
    padding: 25px;
    border-radius: 25px;
    color: white;
    margin-bottom: 20px;
}

.energy-card {
    background: #111827;
    padding: 25px;
    border-radius: 25px;
    text-align: center;
}

.big-number {
    font-size: 50px;
    font-weight: bold;
    color: #4ADE80;
}

.stock-row {
    background-color: #111827;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================

st.markdown('<div class="main-title">🌤️ 股市天氣</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">用天氣與人格，看懂股票情緒</div>', unsafe_allow_html=True)

st.write("")

# =========================
# 股票輸入
# =========================

stock_id = st.text_input(
    "輸入股票代碼",
    value="2330.TW"
)

# =========================
# 天氣系統
# =========================

weather_types = [
    ("☀️ 晴天", "市場偏樂觀，資金持續流入"),
    ("⛅ 多雲", "市場觀望中，方向尚未明朗"),
    ("🌧️ 下雨", "市場偏弱，短線壓力較大"),
    ("⛈️ 暴風雨", "波動劇烈，需注意風險")
]

# =========================
# 人格系統
# =========================

personalities = [
    ("🦁 王者型", "強勢領漲，市場焦點"),
    ("🐺 狼型", "波動大但攻擊性強"),
    ("🐢 穩健型", "適合長期持有"),
    ("🦊 狡猾型", "容易突然爆發"),
    ("🐳 巨鯨型", "主力資金明顯")
]

# =========================
# 分析按鈕
# =========================

if st.button("開始分析"):

    try:

        stock = yf.Ticker(stock_id)
        df = stock.history(period="3mo")

        # 防呆
        if df.empty:
            st.error("查無股票資料")
            st.stop()

        current_price = round(float(df['Close'].iloc[-1]), 2)
        prev_price = round(float(df['Close'].iloc[-2]), 2)

        change = current_price - prev_price
        change_percent = round(change / prev_price * 100, 2)

        # 隨機生成
        weather = random.choice(weather_types)
        personality = random.choice(personalities)
        energy = random.randint(40, 98)

        # =========================
        # 今日天氣卡
        # =========================

        st.markdown(f"""
        <div class="weather-card">
            <h2>{weather[0]}</h2>
            <h4>{weather[1]}</h4>
            <br>
            <h1>{stock_id}</h1>
            <h2>目前價格：{current_price}</h2>
            <h3>漲跌：{change_percent}%</h3>
        </div>
        """, unsafe_allow_html=True)

        # =========================
        # 三欄
        # =========================

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(f"""
            <div class="personality-card">
                <h2>{personality[0]}</h2>
                <h4>{personality[1]}</h4>
            </div>
            """, unsafe_allow_html=True)

        with col2:

            st.markdown(f"""
            <div class="energy-card">
                <div>能量值</div>
                <div class="big-number">{energy}</div>
            </div>
            """, unsafe_allow_html=True)

        # =========================
        # AI 分析
        # =========================

        if change_percent > 3:
            mood = "市場非常樂觀，短線偏強。"
        elif change_percent > 0:
            mood = "市場情緒偏多，仍有上漲動能。"
        elif change_percent > -3:
            mood = "市場觀望氣氛濃厚。"
        else:
            mood = "市場偏空，需留意風險。"

        st.subheader("🤖 AI 情緒解讀")

        st.info(f"""
        {stock_id} 今日收盤 {current_price} 元。

        漲跌幅 {change_percent}% 。

        {mood}
        """)

        # =========================
        # K線圖
        # =========================

        st.subheader("📈 近期走勢")

        st.line_chart(df['Close'])

    except Exception as e:
        st.error("發生錯誤")
        st.code(str(e))

# =========================
# 熱門排行榜
# =========================

st.write("")
st.subheader("🔥 熱門股票排行榜")

hot_stocks = [
    ("2330.TW", "台積電"),
    ("2317.TW", "鴻海"),
    ("2603.TW", "長榮"),
    ("2454.TW", "聯發科"),
    ("2881.TW", "富邦金")
]

rank = 1

for code, name in hot_stocks:

    score = random.randint(50, 99)

    st.markdown(f"""
    <div class="stock-row">
        #{rank}　{name}　({code})
        <br>
        能量值：{score}
    </div>
    """, unsafe_allow_html=True)

    rank += 1