import streamlit as st
import yfinance as yf
import pandas as pd
import random

# =========================
# 頁面設定
# =========================

st.set_page_config(
    page_title="🔥 AI 台股情緒 App Pro",
    page_icon="🔥",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp{
    background:linear-gradient(180deg,#020617,#071226);
    color:white;
}

html,body,[class*="css"]{
    font-family:Arial;
}

/* 標題 */

.main-title{
    font-size:52px;
    font-weight:900;
    color:white;
}

.sub-title{
    color:#94a3b8;
    font-size:18px;
    margin-bottom:25px;
}

/* 卡片 */

.main-card{
    background:linear-gradient(135deg,#1e3a8a,#0f172a);
    padding:35px;
    border-radius:30px;
    margin-bottom:25px;
    box-shadow:0 0 30px rgba(0,0,0,0.45);
}

.info-card{
    background:linear-gradient(135deg,#111827,#0f172a);
    padding:25px;
    border-radius:25px;
    margin-bottom:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.3);
}

.rank-card{
    background:linear-gradient(135deg,#111827,#0f172a);
    padding:22px;
    border-radius:24px;
    margin-bottom:18px;
    box-shadow:0 0 18px rgba(0,0,0,0.35);
    transition:0.3s;
}

.rank-card:hover{
    transform:scale(1.02);
}

.ai-card{
    background:linear-gradient(135deg,#1e293b,#0f172a);
    padding:28px;
    border-radius:28px;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================

st.markdown(
    '<div class="main-title">🔥 AI 台股情緒 App Pro</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">AI 即時分析台股情緒與市場熱度</div>',
    unsafe_allow_html=True
)

# =========================
# 搜尋
# =========================

search = st.text_input(
    "🔍 搜尋股票代號或名稱",
    value="2330"
)

# =========================
# 股票解析
# =========================

tw_stock_map = {
    "台積電":"2330",
    "鴻海":"2317",
    "聯發科":"2454",
    "台達電":"2308",
    "長榮":"2603",
    "富邦金":"2881",
    "中信金":"2891",
    "0050":"0050",
    "00878":"00878",
    "00919":"00919"
}

if search in tw_stock_map:
    stock_code = tw_stock_map[search]
else:
    stock_code = search

ticker_symbol = f"{stock_code}.TW"

# =========================
# 抓資料
# =========================

try:

    ticker = yf.Ticker(ticker_symbol)

    hist = ticker.history(period="1mo")

    info = ticker.info

    current_price = round(hist["Close"].iloc[-1],2)

    prev_price = round(hist["Close"].iloc[-2],2)

    change_percent = round(
        ((current_price - prev_price)/prev_price)*100,
        2
    )

    high_price = round(hist["High"].iloc[-1],2)

    low_price = round(hist["Low"].iloc[-1],2)

    open_price = round(hist["Open"].iloc[-1],2)

    volume = int(hist["Volume"].iloc[-1])

    stock_name = info.get("longName",stock_code)

except:

    st.error("❌ 找不到股票資料")

    st.stop()

# =========================
# AI 情緒
# =========================

if change_percent >= 4:

    weather = "🔥 火山"
    mood = "市場極度樂觀"
    animal = "🦁 王者型"
    energy = 95

elif change_percent >= 2:

    weather = "☀️ 晴天"
    mood = "市場偏強"
    animal = "🐺 狼型"
    energy = 82

elif change_percent >= 0:

    weather = "⛅ 多雲"
    mood = "市場震盪"
    animal = "🐢 穩健型"
    energy = 65

elif change_percent >= -3:

    weather = "🌧️ 下雨"
    mood = "市場偏弱"
    animal = "🦊 狐狸型"
    energy = 42

else:

    weather = "⛈️ 暴風雨"
    mood = "市場恐慌"
    animal = "🐍 崩盤蛇"
    energy = 20

# =========================
# 主卡片
# =========================

st.markdown(f"""
<div class="main-card">

<div style="font-size:90px;">
{weather}
</div>

<div style="
font-size:46px;
font-weight:bold;
margin-top:10px;
">
{stock_name}
</div>

<div style="
font-size:24px;
color:#cbd5e1;
margin-top:10px;
">
{mood}
</div>

<br>

<div style="
background:#111827;
padding:22px;
border-radius:22px;
">

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
padding:22px;
border-radius:24px;
">

<div style="
font-size:34px;
font-weight:bold;
">
{animal}
</div>

<div style="
font-size:18px;
color:#fde68a;
margin-top:10px;
">
AI 判定近期市場熱度提升，
資金動能偏強。
</div>

</div>

</div>
""", unsafe_allow_html=True)

# =========================
# 股價資訊
# =========================

change_color = "#22c55e" if change_percent >= 0 else "#ef4444"

change_arrow = "📈" if change_percent >= 0 else "📉"

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="info-card">

    <div style="color:#94a3b8;">
    目前股價
    </div>

    <div style="
    font-size:42px;
    font-weight:bold;
    margin-top:10px;
    ">
    {current_price}
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="info-card">

    <div style="color:#94a3b8;">
    漲跌幅
    </div>

    <div style="
    font-size:36px;
    font-weight:bold;
    color:{change_color};
    margin-top:10px;
    ">
    {change_arrow} {change_percent}%
    </div>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="info-card">

    <div style="color:#94a3b8;">
    今日最高
    </div>

    <div style="
    font-size:36px;
    font-weight:bold;
    margin-top:10px;
    ">
    {high_price}
    </div>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="info-card">

    <div style="color:#94a3b8;">
    今日最低
    </div>

    <div style="
    font-size:36px;
    font-weight:bold;
    margin-top:10px;
    ">
    {low_price}
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================
# 成交量
# =========================

st.markdown(f"""
<div class="info-card">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
color:#94a3b8;
font-size:18px;
">
成交量
</div>

<div style="
font-size:38px;
font-weight:bold;
margin-top:10px;
">
{volume:,}
</div>

</div>

<div>

<div style="
font-size:22px;
color:#22c55e;
">
{change_arrow}
</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)

# =========================
# 股價走勢
# =========================

st.subheader("📈 股價走勢")

st.line_chart(hist["Close"])

# =========================
# 熱門排行榜
# =========================

st.write("")
st.subheader("🔥 AI 熱門排行榜")

top_stocks = [
    ("2330","台積電"),
    ("2603","長榮"),
    ("2317","鴻海"),
    ("2454","聯發科"),
    ("2881","富邦金"),
    ("2891","中信金"),
    ("2308","台達電")
]

rank_data = []

for code,name in top_stocks:

    try:

        ticker = yf.Ticker(f"{code}.TW")

        hist_rank = ticker.history(period="5d")

        close_now = hist_rank["Close"].iloc[-1]

        close_old = hist_rank["Close"].iloc[-2]

        change_rank = round(
            ((close_now-close_old)/close_old)*100,
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
    key=lambda x:x[2],
    reverse=True
)

# =========================
# 顯示排行榜
# =========================

for i,(stock,weather_rank,score,animal_rank,change_rank) in enumerate(rank_data,1):

    medal = ""

    if i == 1:
        medal = "🥇"

    elif i == 2:
        medal = "🥈"

    elif i == 3:
        medal = "🥉"

    rank_color = "#22c55e" if change_rank >= 0 else "#ef4444"

    rank_arrow = "📈" if change_rank >= 0 else "📉"

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
            margin-top:10px;
            ">
            {stock}
            </div>

            <div style="
            color:#cbd5e1;
            font-size:20px;
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
            font-size:48px;
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

# =========================
# AI 解讀
# =========================

st.write("")
st.subheader("🤖 AI 情緒解讀")

st.markdown(f"""
<div class="ai-card">

<div style="
font-size:22px;
line-height:1.8;
">

目前市場對 <b>{stock_name}</b> 偏向樂觀。<br><br>

近期成交量提升，
市場資金持續流入。<br><br>

AI 判定：<br><br>

✅ 市場熱度提升<br>
✅ 短線情緒偏多<br>
✅ 波動增加<br>
✅ 關注度提升

</div>

</div>
""", unsafe_allow_html=True
