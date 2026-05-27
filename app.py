import streamlit as st
import yfinance as yf
import pandas as pd
import random
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

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
st_autorefresh(
    interval=60000,
    key="stock_refresh"
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
    margin-top: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.4);
}

.stock-row {
    background-color: #132238;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    font-size: 20px;
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
    '<div class="sub-title">人人看得懂的股票分析 APP</div>',
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
# 開始分析
# =========================
if st.button("開始分析"):

    try:

        # 下載資料
        df = yf.download(
            stock_id,
            period="3mo",
            progress=False
        )

        # 防呆
        if len(df) < 5:
            st.error("股票資料不足")
            st.stop()

        # 最新價格
        latest_price = round(df["Close"].iloc[-1].item(), 2)

        # 五日漲跌
        old_price = df["Close"].iloc[-5].item()
        diff = latest_price - old_price

        # 漲跌百分比
        percent = round((diff / old_price) * 100, 2)

        # 天氣判斷
        if percent > 5:
            weather = "☀️ 大晴天"
            advice = "股票非常強勢，可持續觀察"
        elif percent > 0:
            weather = "⛅ 多雲"
            advice = "股票偏強，可留意後續走勢"
        elif percent > -5:
            weather = "🌧️ 小雨"
            advice = "股票偏弱，建議保守"
        else:
            weather = "⛈️ 暴風雨"
            advice = "風險較高，需注意"

        # =========================
        # 顯示卡片
        # =========================
        st.markdown(f"""
        <div class="weather-card">

        <h1>{weather}</h1>

        <h2>目前股價：{latest_price}</h2>

        <h3>五日漲跌：{percent}%</h3>

        <p style="font-size:22px;">
        {advice}
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # =========================
        # K線圖
        # =========================
        st.subheader("📈 股價走勢")

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Close"],
                mode='lines',
                name='收盤價'
            )
        )

        fig.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

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
        #{rank}　{name}（{code}）
        <br>
        能量值：{score}
    </div>
    """, unsafe_allow_html=True)

    rank += 1