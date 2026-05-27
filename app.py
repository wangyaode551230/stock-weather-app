import streamlit as st
import yfinance as yf
import random

# ======================
# 頁面設定
# ======================

st.set_page_config(
    page_title="🔥 AI 台股情緒 App",
    page_icon="🔥",
    layout="wide"
)

# ======================
# CSS 美化
# ======================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Arial';
}

.stApp {
    background: linear-gradient(180deg,#020617,#071226);
    color: white;
}

/* 標題 */

.main-title {
    font-size: 52px;
    font-weight: 900;
    color: white;
    margin-bottom: 10px;
}

.sub-title {
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 30px;
}

/* 主卡片 */

.hero-card {
    background: linear-gradient(135deg,#1e3a8a,#0f172a);
    padding: 35px;
    border-radius: 35px;
    margin-bottom: 25px;
    box-shadow: 0 0 35px rgba(0,0,0,0.45);
}

/* 能量卡 */

.energy-card {
    background: rgba(15,23,42,0.9);
    padding: 22px;
    border-radius: 24px;
    margin-top: 18px;
}

/* 排行榜卡片 */

.rank-card {
    background: linear-gradient(135deg,#111827,#0f172a);
    padding: 24px;
    border-radius: 26px;
    margin-bottom: 18px;
    box-shadow: 0 0 20px rgba(0,0,0,0.35);
    transition: 0.3s;
}

.rank-card:hover {
    transform: scale(1.02);
}

/* AI 解讀 */

.ai-card {
    background: linear-gradient(135deg,#1e293b,#0f172a);
    padding: 28px;
    border-radius: 28px;
    margin-top: 20px;
    box-shadow: 0 0 25px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# ======================
# 標題
# ======================

st.markdown(
    '<div class="main-title">🔥 AI 台股情緒 App</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">即時分析台股情緒、能量與市場熱度</div>',
    unsafe_allow_html=True
)

# ======================
# 股票清單
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
    "🔍 搜尋股票",
    list(stocks.keys())
)

ticker_symbol = stocks[selected]

# ======================
# 抓股票資料
# ======================

ticker = yf.Ticker(ticker_symbol)

try:

    hist = ticker.history(period="1mo")

    current_price = round(hist["Close"].iloc[-1], 2)

    prev_price = round(hist["Close"].iloc[-2], 2)

    change = round(((current_price - prev_price) / prev_price) * 100, 2)

    volume = hist["Volume"].iloc[-1]

except:

    current_price = 0
    change = 0
    volume = 0

# ======================
# AI 情緒判斷
# ======================

if change >= 4:

    weather = "🔥 火山"
    mood = "市場極度樂觀"
    animal = "🦁 王者型"
    energy = 95

elif change >= 2:

    weather = "☀️ 晴天"
    mood = "市場偏強"
    animal = "🐺 狼型"
    energy = 82

elif change >= 0:

    weather = "⛅ 多雲"
    mood = "市場震盪"
    animal = "🐢 穩健型"
    energy = 65

elif change >= -3:

    weather = "🌧️ 下雨"
    mood = "市場偏弱"
    animal = "🦊 狐狸型"
    energy = 42

else:

    weather = "⛈️ 暴風雨"
    mood = "市場恐慌"
    animal = "🐍 毒蛇型"
    energy = 20

# ======================
# 主卡片
# ======================

st.markdown(f"""
<div class="hero-card">

<div style="font-size:95px;">
{weather}
</div>

<div style="
font-size:46px;
font-weight:bold;
margin-top:10px;
">
{selected}
</div>

<div style="
font-size:24px;
color:#cbd5e1;
margin-top:10px;
">
{mood}
</div>

<br>

<div class="energy-card">

<div style="
font-size:18px;
color:#94a3b8;
">
AI 能量值
</div>

<div style="
font-size:68px;
font-weight:bold;
color:#22c55e;
">
⚡ {energy}
</div>

<div style="
width:100%;
height:18px;
background:#1e293b;
border-radius:30px;
overflow:hidden;
margin-top:12px;
">

<div style="
width:{energy}%;
height:100%;
background:linear-gradient(90deg,#22c55e,#4ade80);
">
</div>

</div>

</div>

<br>

<div style="
background:linear-gradient(135deg,#78350f,#451a03);
padding:24px;
border-radius:24px;
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
AI 判定近期市場關注度提高，
資金動能正在升溫。
</div>

</div>

</div>
""", unsafe_allow_html=True)

# ======================
# 股價資訊
# ======================

change_color = "#22c55e" if change >= 0 else "#ef4444"
arrow = "📈" if change >= 0 else "📉"

st.markdown(f"""
<div class="rank-card">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
font-size:34px;
font-weight:bold;
">
💰 {current_price}
</div>

<div style="
font-size:18px;
color:{change_color};
margin-top:8px;
">
{arrow} {change}%
</div>

</div>

<div style="
text-align:right;
">

<div style="
font-size:16px;
color:#94a3b8;
">
成交量
</div>

<div style="
font-size:22px;
font-weight:bold;
">
{volume:,}
</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)

# ======================
# K線圖
# ======================

st.subheader("📈 股價走勢")

st.line_chart(hist["Close"])

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

        close_now = hist["Close"].iloc[-1]
        close_old = hist["Close"].iloc[-2]

        change_rank = round(
            ((close_now - close_old) / close_old) * 100,
            2
        )

        if change_rank >= 4:
            weather_rank = "🔥 火山"
            score = 95
            animal_rank = "🦁"

        elif change_rank >= 2:
            weather_rank = "☀️ 晴天"
            score = 82
            animal_rank = "🐺"

        elif change_rank >= 0:
            weather_rank = "⛅ 多雲"
            score = 65
            animal_rank = "🐢"

        elif change_rank >= -3:
            weather_rank = "🌧️ 下雨"
            score = 42
            animal_rank = "🦊"

        else:
            weather_rank = "⛈️ 暴風雨"
            score = 20
            animal_rank = "🐍"

        rank_data.append(
            (
                f"{code} {name}",
                weather_rank,
                score,
                animal_rank,
                change_rank
            )
        )

    except:
        pass

rank_data = sorted(
    rank_data,
    key=lambda x: x[2],
    reverse=True
)

# ======================
# 顯示排行榜
# ======================

for i, (stock, weather_rank, score, animal_rank, change_rank) in enumerate(rank_data, 1):

    rank_color = "#22c55e" if change_rank >= 0 else "#ef4444"

    rank_arrow = "📈" if change_rank >= 0 else "📉"

    medal = ""

    if i == 1:
        medal = "🥇"
    elif i == 2:
        medal = "🥈"
    elif i == 3:
        medal = "🥉"

    st.markdown(f"""
    <div class="rank-card">

    <div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    ">

        <div>

            <div style="
            color:#94a3b8;
            font-size:16px;
            ">
            {medal} #{i} 排名
            </div>

            <div style="
            font-size:30px;
            font-weight:bold;
            margin-top:8px;
            ">
            {stock}
            </div>

            <div style="
            font-size:20px;
            color:#cbd5e1;
            margin-top:10px;
            ">
            {weather_rank} {animal_rank}
            </div>

        </div>

        <div style="text-align:right;">

            <div style="
            color:{rank_color};
            font-size:22px;
            ">
            {rank_arrow} {change_rank}%
            </div>

            <div style="
            font-size:46px;
            font-weight:bold;
            color:#22c55e;
            margin-top:10px;
            ">
            {score}
            </div>

            <div style="
            color:#94a3b8;
            font-size:14px;
            ">
            能量值
            </div>

        </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

# ======================
# AI 解讀
# ======================

st.write("")
st.subheader("🤖 AI 情緒解讀")

st.markdown(f"""
<div class="ai-card">

<div style="
font-size:22px;
line-height:1.8;
">

目前市場對 <b>{selected}</b> 偏向樂觀。<br><br>

近期成交量提升，
市場資金關注度增加。<br><br>

AI 判定：<br><br>

✅ 情緒偏強<br>
✅ 波動增加<br>
✅ 短線偏多<br>
✅ 市場熱度提升

</div>

</div>
""", unsafe_allow_html=True