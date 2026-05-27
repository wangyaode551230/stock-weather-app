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

st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
}

h1,h2,h3,p{
    font-family:-apple-system;
    color:white;
}

.stock-card{
    padding:30px;
    border-radius:30px;
    color:white;
    margin-top:20px;
    margin-bottom:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.25);
}

.info-card{
    background:#111827;
    padding:20px;
    border-radius:22px;
    margin-bottom:16px;
    box-shadow:0 4px 15px rgba(0,0,0,0.2);
}

.small-card{
    background:#111827;
    padding:20px;
    border-radius:22px;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================

st.markdown("""
<h1 style="
font-size:58px;
font-weight:900;
margin-bottom:0;
">
股市天氣 ☀️
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
font-size:24px;
color:#94a3b8;
margin-top:0;
margin-bottom:30px;
">
用天氣與人格，看懂股市情緒
</p>
""", unsafe_allow_html=True)

# =========================
# 搜尋功能
# =========================

st.markdown("""
<h1 style="
margin-top:20px;
font-size:40px;
">
🔍 搜尋股票
</h1>
""", unsafe_allow_html=True)

search = st.text_input(
    "",
    placeholder="輸入股票代號，例如 2330"
)

if search:

    try:

        stock = yf.Ticker(f"{search}.TW")

        hist = stock.history(period="5d")

        if len(hist) > 0:

            close = round(hist["Close"][-1], 2)

            prev = round(hist["Close"][-2], 2)

            change = round(
                ((close - prev) / prev) * 100,
                2
            )

            volume = int(hist["Volume"][-1])

            info = twstock.realtime.get(search)

            stock_name = info["info"]["name"]

            score = random.randint(45, 95)

            # =========================
            # 人格分類
            # =========================

            if change >= 4:
                icon = "🦁"
                role = "王者型"
                weather = "☀️ 晴天"

            elif change >= 2:
                icon = "🐺"
                role = "狼型"
                weather = "⛅ 多雲"

            elif change >= -1:
                icon = "🐢"
                role = "穩健型"
                weather = "🌥️ 陰天"

            else:
                icon = "🦊"
                role = "投機型"
                weather = "⛈️ 暴風雨"

            # =========================
            # 搜尋結果卡片
            # =========================

            st.markdown(f"""
            <div class="stock-card"
            style="
            background:linear-gradient(
            135deg,
            #1e3c72,
            #2a5298
            );
            ">

            <h1>{stock_name} {search}</h1>

            <h2>{weather}</h2>

            <h2>{icon} {role}</h2>

            <h1 style="
            font-size:70px;
            ">
            {score}
            </h1>

            <p style="font-size:26px;">
            股價：{close}
            </p>

            <p style="font-size:26px;">
            漲跌：{change}%
            </p>

            <p style="font-size:26px;">
            成交量：{volume:,}
            </p>

            </div>
            """, unsafe_allow_html=True)

            # =========================
            # AI 解讀
            # =========================

            st.markdown(f"""
            <div class="info-card">

            <h2>🤖 AI 情緒解讀</h2>

            <p style="font-size:22px;">

            {stock_name} 今日市場情緒偏向
            {role}，
            目前股價變動 {change}% 。

            </p>

            <p style="font-size:20px;color:#cbd5e1;">

            成交量 {volume:,}，
            顯示市場關注度提高。

            </p>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.error("查無股票資料")

    except:

        st.error("股票代號錯誤")

# =========================
# 熱門排行榜
# =========================

st.markdown("""
<h1 style="
margin-top:40px;
font-size:40px;
">
🔥 熱門股票人格榜
</h1>
""", unsafe_allow_html=True)

ranking = [

    ("2330","台積電","🦁","王者型",82,"☀️ 晴天"),
    ("2603","長榮","🐺","狼型",76,"⛈️ 暴風雨"),
    ("2317","鴻海","🐢","穩健型",65,"⛅ 多雲"),
    ("2454","聯發科","🦊","投機型",58,"🌧️ 下雨"),
    ("2881","富邦金","🐢","穩健型",61,"🌥️ 陰天")

]

for code, name, icon, role, score, weather in ranking:

    st.markdown(f"""
    <div class="info-card">

    <h2>
    {icon} {code} {name}
    </h2>

    <p style="font-size:22px;">
    {weather}
    </p>

    <p style="font-size:22px;">
    人格：{role}
    </p>

    <h1 style="
    color:#4ade80;
    ">
    {score}
    </h1>

    </div>
    """, unsafe_allow_html=True)

# =========================
# 人格解釋
# =========================

st.markdown("""
<h1 style="
margin-top:40px;
font-size:40px;
">
🧠 人格說明
</h1>
""", unsafe_allow_html=True)

animal_info = [

("🦁 王者型","市場超強勢，主力資金集中。"),
("🐺 狼型","波動較大，爆發力強。"),
("🐢 穩健型","適合長期持有。"),
("🦊 投機型","短線波動較大。")

]

for title, desc in animal_info:

    st.markdown(f"""
    <div class="info-card">

    <h2>{title}</h2>

    <p style="font-size:22px;">
    {desc}
    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================
# 能量值說明
# =========================

st.markdown("""
<h1 style="
margin-top:40px;
font-size:40px;
">
⚡ 能量值說明
</h1>
""", unsafe_allow_html=True)

energy_info = [

("80 - 100","🔥 非常強勢"),
("60 - 80","📈 偏強勢"),
("40 - 60","➖ 普通"),
("20 - 40","📉 偏弱勢"),
("0 - 20","❄️ 非常弱勢")

]

for title, desc in energy_info:

    st.markdown(f"""
    <div class="info-card">

    <h2>{title}</h2>

    <p style="font-size:22px;">
    {desc}
    </p>

    </div>
    """, unsafe_allow_html=True)