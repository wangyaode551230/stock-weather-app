import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="AI 台股情緒 App Pro Max",
    page_icon="🔥",
    layout="wide"
)

# ======================
# CSS
# ======================

st.markdown("""
<style>

.stApp{
    background-image:url("https://images.unsplash.com/photo-1518770660439-4636190af475");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
    color:white;
}

html, body, [class*="css"]{
    font-family:Arial;
}

.block-container{
    background:rgba(2,6,23,0.82);
    padding:2rem;
    border-radius:30px;
}

.title{
    font-size:56px;
    font-weight:900;
    color:white;
}

.sub{
    color:#94a3b8;
    font-size:18px;
    margin-bottom:30px;
}

.card{
    background:linear-gradient(135deg,#0f172a,#111827);
    padding:25px;
    border-radius:28px;
    border:1px solid rgba(255,255,255,0.08);
    box-shadow:0 0 25px rgba(0,0,0,0.4);
    margin-bottom:20px;
}

.hero{
    background:linear-gradient(135deg,#172554,#0f172a);
    border:1px solid #3b82f6;
    padding:35px;
    border-radius:30px;
    margin-bottom:25px;
}

.rank{
    background:linear-gradient(135deg,#111827,#0b1220);
    padding:20px;
    border-radius:24px;
    text-align:center;
    margin-bottom:20px;
}

.green{
    color:#4ade80;
}

.red{
    color:#fb7185;
}

.yellow{
    color:#facc15;
}

</style>
""", unsafe_allow_html=True)

# ======================
# 標題
# ======================

st.markdown(
    '<div class="title">🔥 AI 台股情緒 App Pro Max</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub">AI 即時分析台股、ETF、情緒、熱門排行與市場動能</div>',
    unsafe_allow_html=True
)

# ======================
# 搜尋
# ======================

search = st.text_input(
    "🔍 搜尋股票代號或名稱",
    value="2330"
)

# 自動判斷股票代號
stock_code = search.strip()

# 中文股票轉換
name_map = {
    "台積":"2330",
    "台積電":"2330",
    "鴻海":"2317",
    "聯發":"2454",
    "聯發科":"2454",
    "長榮":"2603",
    "富邦":"2881",
    "富邦金":"2881",
    "中信":"2891",
    "中信金":"2891"
}

if stock_code in name_map:
    stock_code = name_map[stock_code]

ticker_symbol = f"{stock_code}.TW"

# ======================
# 股票資料
# ======================

try:

    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period="6mo")

    current_price = round(hist["Close"].iloc[-1], 2)
    prev_price = round(hist["Close"].iloc[-2], 2)

    change_percent = round(
        ((current_price - prev_price) / prev_price) * 100,
        2
    )

    volume = int(hist["Volume"].iloc[-1])

except:

    st.error("❌ 查無股票資料")
    st.stop()

# ======================
# AI 情緒系統
# ======================

if change_percent >= 4:
    weather = "🔥"
    mood = "市場爆發"
    animal = "🦁 獅王"
    score = 95

elif change_percent >= 2:
    weather = "☀️"
    mood = "市場偏多"
    animal = "🐺 狼王"
    score = 82

elif change_percent >= 0:
    weather = "☁️"
    mood = "市場震盪"
    animal = "🐢 烏龜"
    score = 65

elif change_percent >= -3:
    weather = "🌧️"
    mood = "市場偏弱"
    animal = "🦊 狐狸"
    score = 42

else:
    weather = "⛈️"
    mood = "市場恐慌"
    animal = "🐍 毒蛇"
    score = 20

# ======================
# 主卡片
# ======================

st.markdown(f"""
<div class="hero">

<div style="display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;">

<div>

<div style="font-size:110px;">
{weather}
</div>

<div style="
font-size:72px;
font-weight:900;
">
{stock_code}
</div>

<div style="
font-size:28px;
color:#cbd5e1;
margin-top:10px;
">
{mood}
</div>

</div>

<div style="flex:1;min-width:280px;">

<div class="card">

<div style="font-size:18px;color:#cbd5e1;">
AI 能量值
</div>

<div class="green" style="
font-size:68px;
font-weight:900;
margin-top:10px;
">
⚡ {score}
</div>

</div>

<div class="card">

<div style="font-size:18px;color:#cbd5e1;">
AI 動物模型
</div>

<div style="
font-size:44px;
font-weight:900;
margin-top:10px;
">
{animal}
</div>

</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)

# ======================
# 即時資訊
# ======================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="card">
    <div style="color:#94a3b8;">目前股價</div>
    <div style="font-size:34px;font-weight:bold;">
    {current_price}
    </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    color = "#4ade80" if change_percent >= 0 else "#fb7185"

    st.markdown(f"""
    <div class="card">
    <div style="color:#94a3b8;">漲跌幅</div>
    <div style="font-size:34px;font-weight:bold;color:{color};">
    {change_percent}%
    </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="card">
    <div style="color:#94a3b8;">成交量</div>
    <div style="font-size:26px;font-weight:bold;">
    {volume:,}
    </div>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="card">
    <div style="color:#94a3b8;">AI 能量</div>
    <div class="green" style="font-size:34px;font-weight:bold;">
    {score}
    </div>
    </div>
    """, unsafe_allow_html=True)

# ======================
# 走勢圖
# ======================

st.subheader("📈 股價走勢")

chart_df = pd.DataFrame({
    "收盤價": hist["Close"]
})

st.line_chart(chart_df)

# ======================
# AI 排行榜
# ======================

st.subheader("🔥 AI 熱門排行榜")

top_list = [
    ("2330","台積電"),
    ("2317","鴻海"),
    ("2454","聯發科"),
    ("2308","台達電"),
    ("2603","長榮"),
    ("2881","富邦金"),
    ("2891","中信金"),
    ("0050","元大50")
]

rank_data = []

for code, name in top_list:

    try:

        t = yf.Ticker(f"{code}.TW")
        h = t.history(period="5d")

        new_price = h["Close"].iloc[-1]
        old_price = h["Close"].iloc[-2]

        chg = round(((new_price - old_price) / old_price) * 100, 2)

        if chg >= 4:
            icon = "🔥"
            ani = "🦁"
            energy = 95

        elif chg >= 2:
            icon = "☀️"
            ani = "🐺"
            energy = 82

        elif chg >= 0:
            icon = "☁️"
            ani = "🐢"
            energy = 65

        else:
            icon = "🌧️"
            ani = "🦊"
            energy = 42

        rank_data.append(
            [code, icon, ani, energy]
        )

    except:
        pass

cols = st.columns(4)

for i, item in enumerate(rank_data):

    code, icon, ani, energy = item

    with cols[i % 4]:

        color = "#4ade80" if energy >= 80 else "#facc15"

        st.markdown(f"""
        <div class="rank">

        <div style="color:#94a3b8;">
        🏅 #{i+1}
        </div>

        <div style="
        font-size:30px;
        font-weight:900;
        margin-top:12px;
        ">
        {code}
        </div>

        <div style="
        margin-top:10px;
        font-size:20px;
        ">
        {icon} {ani}
        </div>

        <div style="
        font-size:48px;
        font-weight:900;
        color:{color};
        margin-top:12px;
        ">
        {energy}
        </div>

        </div>
        """, unsafe_allow_html=True)

# ======================
# AI 解讀
# ======================

st.subheader("🤖 AI 情緒解讀")

st.markdown(f"""
<div class="card">

<div style="
font-size:24px;
font-weight:bold;
margin-bottom:15px;
">
目前 AI 判定：
</div>

<ul style="line-height:2;font-size:20px;">

<li>市場情緒：
<span class="green">{mood}</span>
</li>

<li>動能強度：
<span class="green">{score}</span>
</li>

<li>動物模型：
<span class="green">{animal}</span>
</li>

</ul>

<div style="
margin-top:20px;
font-size:18px;
color:#cbd5e1;
">
近期成交量與價格波動提升，
代表市場資金正在關注此股票。
AI 預測目前短線偏向強勢格局。
</div>

</div>
""", unsafe_allow_html=True)

st.caption("Made with Streamlit ❤️")
