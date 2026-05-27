import streamlit as st
import yfinance as yf
import pandas as pd
import random
import time

# =========================
# APP 設定
# =========================
st.set_page_config(
    page_title="股市天氣",
    page_icon="🌤️",
    layout="wide"
)

# =========================
# 自動刷新（60秒）
# =========================
st.autorefresh(
    interval=60000,
    key="stock_refresh"
)

# =========================
# CSS 美化
# =========================
st.markdown("""
<style>

html, body, [class*="css"]  {
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
    border-radius: 20px;
    color: white;
}

.energy-card {
    background: #111827;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
}

.stock-row {
    background: #111827;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
}

.big-number {
    font-size: 42px;
    font-weight: bold;
}

.small-gray {
    color: #A0AEC0;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================
st.markdown(
    '<div class="main-title">🌤️ 股市天氣</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">用天氣與人格，看懂股市情緒</div>',
    unsafe_allow_html=True
)

st.write("")

# =========================
# 股票輸入
# =========================
stock_id = st.text_input(
    "輸入股票代碼",
    "2330.TW"
)

# =========================
# 天氣判斷
# =========================
def get_weather(change):

    if change >= 3:
        return "☀️ 晴天", "市場非常樂觀"

    elif change >= 1:
        return "🌤️ 多雲", "市場偏多"

    elif change >= -1:
        return "☁️ 陰天", "市場觀望"

    elif change >= -3:
        return "🌧️ 下雨", "市場偏空"

    else:
        return "⛈️ 暴風雨", "市場恐慌"

# =========================
# 人格分析
# =========================
def get_personality(volatility):

    if volatility > 4:
        return "🦁 王者型", "波動大、人氣強"

    elif volatility > 2:
        return "🐺 狼型", "具攻擊性"

    else:
        return "🐢 穩健型", "穩定成長"

# =========================
# 股票分析
# =========================
try:

    # 下載股票資料
    df = yf.download(
        stock_id,
        period="3mo",
        progress=False
    )

    # 防呆
    if len(df) < 5:
        st.error("股票資料不足")
        st.stop()

    # 收盤價
    close_series = df["Close"].dropna()

    # 目前價格
    current_price = float(close_series.iloc[-1])

    # 前一天價格
    previous_price = float(close_series.iloc[-2])

    # 漲跌幅
    change_percent = (
        (current_price - previous_price)
        / previous_price
    ) * 100

    # 波動
    volatility = (
        close_series.pct_change().std()
    ) * 100

    # 天氣
    weather, weather_desc = get_weather(change_percent)

    # 人格
    personality, personality_desc = get_personality(volatility)

    # 能量值
    energy = random.randint(60, 98)

    # =========================
    # 今日天氣卡
    # =========================
    st.markdown(f"""
    <div class="weather-card">
        <h1>{weather}</h1>
        <h3>{weather_desc}</h3>
        <p>股票：{stock_id}</p>
        <p>目前股價：{current_price:.2f}</p>
        <p>漲跌幅：{change_percent:.2f}%</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # 左右欄位
    # =========================
    col1, col2 = st.columns(2)

    # 人格
    with col1:

        st.markdown(f"""
        <div class="personality-card">
            <h2>{personality}</h2>
            <p>{personality_desc}</p>
        </div>
        """, unsafe_allow_html=True)

    # 能量值
    with col2:

        st.markdown(f"""
        <div class="energy-card">
            <div class="big-number">{energy}</div>
            <div class="small-gray">市場能量值</div>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # AI 分析
    # =========================
    st.write("")
    st.subheader("🤖 AI 情緒分析")

    if change_percent > 2:
        st.success("市場氣氛偏多，資金流入明顯。")

    elif change_percent > 0:
        st.info("市場穩定偏強。")

    else:
        st.warning("市場偏弱，建議保守觀察。")

    # =========================
    # 走勢圖
    # =========================
    st.write("")
    st.subheader("📈 近期走勢")

    st.line_chart(close_series)

except Exception as e:

    st.error("發生錯誤")
    st.code(str(e))

# =========================
# 熱門股票排行
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
        #{rank}　{name}（{code}）
        <br>
        能量值：{score}
    </div>
    """, unsafe_allow_html=True)

    rank += 1