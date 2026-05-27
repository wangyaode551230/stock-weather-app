import streamlit as st
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

# =====================
# 自動刷新
# =====================
st_autorefresh(interval=60000, key="refresh")

# =====================
# 頁面設定
# =====================
st.set_page_config(
    page_title="股市天氣",
    page_icon="☀️",
    layout="wide"
)

# =====================
# CSS
# =====================
st.markdown("""
<style>

.stApp {
    background-color: #f3f4f6;
}

/* 標題 */
.title {
    font-size: 50px;
    font-weight: bold;
    color: #111827;
}

.sub {
    font-size: 20px;
    color: #6b7280;
    margin-bottom: 30px;
}

/* 天氣卡 */
.weather-card {
    background: linear-gradient(135deg,#60a5fa,#2563eb);
    padding: 35px;
    border-radius: 30px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
}

.big-text {
    font-size: 65px;
    font-weight: bold;
}

/* 動物人格卡 */

.lion {
    background: linear-gradient(135deg,#f59e0b,#facc15);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    color: white;
}

.wolf {
    background: linear-gradient(135deg,#374151,#111827);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    color: white;
}

.turtle {
    background: linear-gradient(135deg,#10b981,#34d399);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    color: white;
}

.fox {
    background: linear-gradient(135deg,#f97316,#fb923c);
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    color: white;
}

.energy {
    font-size: 34px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================
# 標題
# =====================
st.markdown(
    '<div class="title">股市天氣 ☀️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub">用動物人格與天氣，看懂市場情緒</div>',
    unsafe_allow_html=True
)

# =====================
# 股票搜尋
# =====================
# 全台股清單
stocks = {
    "2330 台積電": "2330.TW",
    "2317 鴻海": "2317.TW",
    "2603 長榮": "2603.TW",
    "2454 聯發科": "2454.TW",
    "2881 富邦金": "2881.TW",
    "2303 聯電": "2303.TW",
    "2412 中華電": "2412.TW",
    "1301 台塑": "1301.TW",
    "1303 南亞": "1303.TW",
    "2002 中鋼": "2002.TW",
    "2891 中信金": "2891.TW",
    "2882 國泰金": "2882.TW",
    "2886 兆豐金": "2886.TW",
    "1216 統一": "1216.TW",
    "1101 台泥": "1101.TW",
    "3045 台灣大": "3045.TW",
    "6505 台塑化": "6505.TW",
    "5880 合庫金": "5880.TW",
    "2884 玉山金": "2884.TW",
    "2885 元大金": "2885.TW"
}

# 搜尋框
selected_stock = st.selectbox(
    "搜尋股票",
    list(stocks.keys())
)

# 股票代碼
stock_id = stocks[selected_stock]

selected_stock = st.selectbox(
    "搜尋股票",
    list(stock_options.keys())
)

stock_id = stock_options[selected_stock]

# =====================
# 抓股票資料
# =====================
df = yf.download(
    stock_id,
    period="3mo",
    progress=False
)

# 最新價格
latest_price = round(df["Close"].iloc[-1].item(), 2)

# 五日前價格
old_price = round(df["Close"].iloc[-5].item(), 2)

# 漲跌
diff = latest_price - old_price

# 漲跌百分比
percent = round((diff / old_price) * 100, 2)

diff = latest_price - old_price

percent = round((diff / old_price) * 100, 2)

# =====================
# 天氣判斷
# =====================
if percent > 5:

    weather = "☀️ 晴天"
    mood = "市場偏樂觀"
    advice = "資金流入，人氣上升中！"

elif percent > 0:

    weather = "⛅ 多雲"
    mood = "市場偏穩"
    advice = "震盪整理中。"

elif percent > -5:

    weather = "🌧️ 下雨"
    mood = "市場偏弱"
    advice = "市場較保守。"

else:

    weather = "⛈️ 暴風雨"
    mood = "市場恐慌"
    advice = "注意風險！"

# =====================
# 主天氣卡
# =====================
st.markdown(f"""
<div class="weather-card">

<div style="font-size:24px;">
今日市場天氣
</div>

<div class="big-text">
{weather}
</div>

<div style="font-size:30px;">
{mood}
</div>

<br>

<div style="font-size:24px;">
{advice}
</div>

</div>
""", unsafe_allow_html=True)

# =====================
# 熱門人格榜
# =====================
st.markdown("## 🔥 熱門股票人格榜")

stocks = [
    ("2330 台積電", "🦁 獅王型", "☀️ 晴天", 82),
    ("2603 長榮", "🐺 狼型", "⛈️ 暴風雨", 76),
    ("2317 鴻海", "🐢 烏龜型", "⛅ 多雲", 65),
    ("2454 聯發科", "🦊 狐狸型", "🌧️ 下雨", 45),
]

for stock, animal, weather, score in stocks:

    card_class = (
        "lion" if "獅" in animal else
        "wolf" if "狼" in animal else
        "turtle" if "龜" in animal else
        "fox"
    )

    st.markdown(f"""
    <div class="{card_class}">

    <h1>{animal}</h1>

    <h2>{stock}</h2>

    <h3>{weather}</h3>

    <div class="energy">
    能量值：{score}
    </div>

    </div>
    """, unsafe_allow_html=True)