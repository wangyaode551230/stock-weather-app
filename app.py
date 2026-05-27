import streamlit as st
import yfinance as yf
import random
import twstock

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

st.markdown(f"""
<style>

.stApp{
    background:#f3f4f6;
}

h1,h2,h3,p{
    font-family:-apple-system;
}

.stock-card{
    padding:30px;
    border-radius:30px;
    color:white;
    margin-top:20px;
    margin-bottom:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.1);
}

.info-card{
    background:white;
    padding:18px;
    border-radius:18px;
    margin-bottom:12px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================

st.markdown(f"""
<h1 style="
font-size:58px;
font-weight:900;
color:#0f172a;
margin-bottom:0;
">
股市天氣 ☀️
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<p style="
font-size:24px;
color:#6b7280;
margin-top:0;
margin-bottom:40px;
">
用動物人格與天氣，看懂市場情緒
</p>
""", unsafe_allow_html=True)

# =========================
# 自動抓台股
# =========================



stocks = {}

for code, info in twstock.codes.items():

    if (
        info.market in ["上市", "上櫃"]
        and "購" not in info.name
        and "售" not in info.name
        and len(code) == 4
    ):

        stock_name = f"{code} {info.name}"

        # 上市股票
        if info.market == "上市":
            stocks[stock_name] = f"{code}.TW"

        # 上櫃股票
        else:
            stocks[stock_name] = f"{code}.TWO"

# =========================
# 搜尋股票
# =========================

selected_stock = st.selectbox(
    "搜尋股票",
    options=list(stocks.keys()),
    index=0
)

stock_id = stocks[selected_stock]

# =========================
# 下載股票資料
# =========================

df = yf.download(
    stock_id,
    period="3mo",
    progress=False
)

# 防呆
if len(df) < 5:

    st.error("股票資料不足")

    st.stop()

# =========================
# 股價資訊
# =========================

latest_price = float(df["Close"].iloc[-1].item())

old_price = float(df["Close"].iloc[-5].item())

diff = latest_price - old_price

percent = round((diff / old_price) * 100, 2)

# =========================
# 天氣系統
# =========================

if percent >= 5:

    weather = "☀️ 晴天"
    advice = "市場偏樂觀，資金持續流入。"
    weather_color = "linear-gradient(135deg,#FFD93D,#FFB800)"

elif percent >= 1:

    weather = "⛅ 多雲"
    advice = "市場偏穩，震盪整理中。"
    weather_color = "linear-gradient(135deg,#60a5fa,#2563eb)"

elif percent >= -3:

    weather = "🌧️ 小雨"
    advice = "市場轉弱，建議觀察。"
    weather_color = "linear-gradient(135deg,#94a3b8,#64748b)"

else:

    weather = "⛈️ 暴風雨"
    advice = "市場恐慌增加，注意風險。"
    weather_color = "linear-gradient(135deg,#374151,#111827)"

# =========================
# AI 動物人格
# =========================

if percent >= 6:

    animal = "獅王型"
    animal_icon = "🦁"

elif percent >= 3:

    animal = "獵豹型"
    animal_icon = "🐆"

elif percent >= 1:

    animal = "狐狸型"
    animal_icon = "🦊"

elif percent >= -1:

    animal = "海豚型"
    animal_icon = "🐬"

elif percent >= -3:

    animal = "烏龜型"
    animal_icon = "🐢"

elif percent >= -6:

    animal = "狼型"
    animal_icon = "🐺"

else:

    animal = "黑熊型"
    animal_icon = "🐻"

# =========================
# 能量值
# =========================

energy = random.randint(45, 98)

# =========================
# 主卡片
# =========================

st.markdown(f"""
<div class="stock-card" style="
background: linear-gradient(135deg,#1e293b,#0f172a);
padding:30px;
border-radius:25px;
color:white;
box-shadow:0 10px 30px rgba(0,0,0,0.4);
margin-top:20px;
">

<h3>今日市場天氣</h3>

<h1 style="
font-size:72px;
margin-bottom:10px;
">
{weather}
</h1>

<h2 style="
font-size:48px;
margin-top:20px;
">
{animal_icon} {animal}
</h2>

<h2 style="
font-size:56px;
color:#4ade80;
margin-top:30px;
">
市場能量值：{energy}
</h2>

<h3>
{selected_stock}
</h3>

<p style="
font-size:22px;
">
最新價格：{round(latest_price,2)}
</p>
<p style="
font-size:20px;
">
能量值越高代表股票越強，
80以上偏強勢，
50附近普通，
30以下偏弱勢。
</p>

<p style="
font-size:22px;
">
五日漲跌：{percent}%
</p>

<p style="
font-size:24px;
margin-top:20px;
">
{advice}
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# 熱門排行榜
# =========================

st.markdown(f"""
<h1 style="
margin-top:40px;
font-size:42px;
">
🔥 熱門股票人格榜
</h1>
""", unsafe_allow_html=True)

ranking = [
    ("2330 台積電","🦁","獅王型",82),
    ("2603 長榮","🐺","狼型",76),
    ("2317 鴻海","🐬","海豚型",65),
    ("2454 聯發科","🦊","狐狸型",58),
]

for name, icon, role, score in ranking:

    st.markdown(f"""
    <div class="info-card" style="
background: linear-gradient(135deg,#111827,#1f2937);
padding:20px;
border-radius:20px;
margin-bottom:15px;
color:white;
box-shadow:0 5px 20px rgba(0,0,0,0.3);
">

    <h2>{icon} {name}</h2>

    <h3>{role}</h3>

    <h1 style="
    color:#22c55e;
    ">
    能量值：{score}
    </h1>

    </div>
    """, unsafe_allow_html=True)

# =========================
# 動物人格說明
# =========================

st.markdown(f"""
<h1 style="
margin-top:50px;
font-size:42px;
">
🐾 動物人格說明
</h1>
""", unsafe_allow_html=True)

animal_info = [

    ("🦁 獅王型", "市場超強勢，主力資金集中。"),

    ("🐆 獵豹型", "爆發力強，快速拉升。"),

    ("🦊 狐狸型", "靈活偏多，慢慢走強。"),

    ("🐬 海豚型", "市場穩定，中性整理。"),

    ("🐢 烏龜型", "保守整理，適合觀察。"),

    ("🐺 狼型", "空方變強，波動增加。"),

    ("🐻 黑熊型", "市場恐慌，風險較高。")

]

for title, desc in animal_info:

    st.markdown(f"""
    <div class="info-card">

    <h2>{title}</h2>

    <p style="
    color:#6b7280;
    font-size:18px;
    ">
    {desc}
    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================
# 圖標解釋
# =========================

st.markdown("""
<h1 style="
margin-top:50px;
font-size:42px;
">
📖 圖標解釋
</h1>
""", unsafe_allow_html=True)

icon_info = [

    ("☀️ 晴天", "市場非常強勢，資金大量流入。"),

    ("⛅ 多雲", "市場穩定，偏多整理中。"),

    ("🌧️ 小雨", "市場轉弱，短線震盪增加。"),

    ("⛈️ 暴風雨", "市場恐慌，波動與風險升高。"),

    ("🦁 獅王型", "領漲股，主力資金集中。"),

    ("🐆 獵豹型", "短線爆發力強，上漲速度快。"),

    ("🦊 狐狸型", "靈活偏多，成長型股票。"),

    ("🐬 海豚型", "市場穩定，中性震盪。"),

    ("🐢 烏龜型", "保守整理，適合長期觀察。"),

    ("🐺 狼型", "空方壓力增加，波動較大。"),

    ("🐻 黑熊型", "市場恐慌，風險最高。")

]

for title, desc in icon_info:

    st.markdown(f"""
    <div class="info-card">

    <h2>{title}</h2>

    <p style="
    color:#6b7280;
    font-size:18px;
    ">
    {desc}
    </p>

    </div>
    """, unsafe_allow_html=True)