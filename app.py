import streamlit as st

# 頁面設定
st.set_page_config(
    page_title="股市天氣",
    page_icon="☀️",
    layout="wide"
)

# 深色主題 CSS
st.markdown("""
<style>

.stApp {
    background-color: #06111f;
    color: white;
}

.title {
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.sub {
    color: #9aa4b2;
    font-size: 18px;
    margin-bottom: 30px;
}

.weather-card {
    background: linear-gradient(135deg, #ffb347, #ffcc33);
    padding: 30px;
    border-radius: 25px;
    color: white;
    margin-bottom: 25px;
}

.stock-card {
    background: #0f1c2e;
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 15px;
}

.big {
    font-size: 48px;
    font-weight: bold;
}

.small {
    font-size: 20px;
    opacity: 0.9;
}

.energy {
    font-size: 32px;
    color: #4ade80;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# 標題
st.markdown('<div class="title">股市天氣 ☀️</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">用天氣與人格，看懂股市情緒</div>', unsafe_allow_html=True)

# 今日天氣卡
st.markdown("""
<div class="weather-card">
    <div class="small">今日市場天氣</div>
    <div class="big">晴天 ☀️</div>
    <div class="small">
        市場偏樂觀<br>
        資金流入，人氣上升中！
    </div>
</div>
""", unsafe_allow_html=True)

# 排行榜
st.subheader("🔥 熱門股票人格榜")

stocks = [
    ("2330 台積電", "獅王型", "☀️ 晴天", 82),
    ("2603 長榮", "狼型", "⛈️ 暴風雨", 76),
    ("2317 鴻海", "穩健型", "☁️ 多雲", 65),
    ("2454 聯發科", "狐狸型", "🌧️ 下雨", 45),
]

for i, stock in enumerate(stocks, start=1):
    st.markdown(f"""
    <div class="stock-card">
        <h3>#{i} {stock[0]}</h3>
        <p>{stock[1]}</p>
        <p>{stock[2]}</p>
        <div class="energy">能量值：{stock[3]}</div>
    </div>
    """, unsafe_allow_html=True)