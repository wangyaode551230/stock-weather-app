import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# =========================
# 頁面設定
# =========================

st.set_page_config(
    page_title="AI 台股人格分析",
    page_icon="🔥",
    layout="centered"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* 整體背景 */

.stApp{
    background:#020b1c;
}

/* 全站字體 */

html, body, [class*="css"]{
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    color:#ffffff;
}

/* 主標題 */

.main-title{
    font-size:64px;
    font-weight:900;
    margin-bottom:30px;
    color:#ffffff;
}

/* 搜尋框 */

.stTextInput input{

    background:#183766 !important;

    color:#ffffff !important;

    border:2px solid #4da3ff !important;

    border-radius:22px !important;

    height:65px !important;

    font-size:28px !important;

    padding-left:25px !important;

    box-shadow:0 6px 20px rgba(0,0,0,0.25);
}

/* 股票卡 */

.stock-card{

    background:#102b63;

    border-radius:35px;

    padding:35px;

    margin-top:25px;

    box-shadow:0 12px 30px rgba(0,0,0,0.35);
}

/* 股票名稱 */

.stock-title{

    font-size:48px;

    font-weight:900;

    margin-bottom:20px;

    color:white;
}

/* 大文字 */

.big-text{

    font-size:32px;

    font-weight:700;

    margin-top:15px;

    color:white;
}

/* 能量值 */

.energy{

    color:#00ff88;

    font-size:62px;

    font-weight:900;

    margin-top:20px;
}

/* 解釋卡 */

.info-box{

    background:white;

    color:black;

    border-radius:30px;

    padding:30px;

    margin-top:30px;

    box-shadow:0 6px 20px rgba(0,0,0,0.15);
}

/* 解釋標題 */

.info-box h1{

    font-size:42px;

    color:black;
}

.info-box h2{

    font-size:32px;

    color:black;
}

/* 解釋文字 */

.info-box p{

    font-size:24px;

    color:#111111;

    line-height:1.8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 主標題
# =========================

st.markdown(
    '<div class="main-title">🔥 AI 台股人格分析</div>',
    unsafe_allow_html=True
)

# =========================
# 搜尋框
# =========================

stock_code = st.text_input(
    "",
    placeholder="輸入台股代號，例如 2330、0050、00878",
    label_visibility="collapsed"
)

# =========================
# 股票搜尋
# =========================

if stock_code:

    try:

        # 股票資料
        ticker = yf.Ticker(f"{stock_code}.TW")

        # 基本資訊
        info = ticker.info

        # 即時資訊
        fast = ticker.fast_info

        # 歷史資料
        hist = ticker.history(period="1mo")

        # =========================
        # 股票資訊
        # =========================

        name = info.get("shortName", stock_code)

        price = fast.get("lastPrice", 0)

        change = info.get("regularMarketChangePercent", 0)

        if change is None:
            change = 0

        volume = info.get("volume", 0)

        market_cap = info.get("marketCap", 0)

        pe = info.get("trailingPE", "N/A")

        # =========================
        # AI 人格系統
        # =========================

        if change >= 4:

            animal = "🦁 獅王型"

            weather = "☀️ 晴天"

            energy = 95

            mood = """
            市場極度強勢。
            主力資金大量流入，
            多頭氣氛非常明顯。
            """

        elif change >= 1:

            animal = "🦊 狐狸型"

            weather = "🌤️ 多雲"

            energy = 75

            mood = """
            市場偏多。
            人氣持續增加，
            資金流動穩定。
            """

        elif change >= -2:

            animal = "🐱 貓咪型"

            weather = "🌧️ 小雨"

            energy = 50

            mood = """
            市場觀望中。
            波動增加，
            買盤力量減弱。
            """

        else:

            animal = "🐺 狼型"

            weather = "⛈️ 暴風雨"

            energy = 20

            mood = """
            市場恐慌。
            空方力量強勢，
            波動風險偏高。
            """

        # =========================
        # 股票卡片
        # =========================

        st.markdown(f"""
        <div class="stock-card">

            <div class="stock-title">
            {stock_code} {name}
            </div>

            <div class="big-text">
            {animal}
            </div>

            <div class="big-text">
            {weather}
            </div>

            <div class="energy">
            ⚡ 能量值：{energy}
            </div>

            <div class="big-text">
            💰 即時股價：{round(price,2)}
            </div>

            <div class="big-text">
            📈 漲跌幅：{round(change,2)}%
            </div>

            <div class="big-text">
            📊 成交量：{volume:,}
            </div>

            <div class="big-text">
            🏦 市值：{market_cap:,}
            </div>

            <div class="big-text">
            💎 本益比：{pe}
            </div>

        </div>
        """, unsafe_allow_html=True)

        # =========================
        # 股價圖
        # =========================

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=hist.index,
            y=hist["Close"],
            mode="lines",
            name="股價"
        ))

        fig.update_layout(

            template="plotly_dark",

            height=450,

            paper_bgcolor="#102b63",

            plot_bgcolor="#102b63",

            font=dict(
                size=18,
                color="white"
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        # =========================
        # AI 圖表解釋
        # =========================

        st.markdown(f"""
        <div class="info-box">

        <h1>📚 AI 圖表解釋</h1>

        <h2>{weather}</h2>

        <p>
        {mood}
        </p>

        <h2>🧠 動物人格分析</h2>

        <p>
        {animal} 代表目前市場主力資金風格。
        能量值越高，
        代表市場越強勢。
        </p>

        <h2>⚡ 能量值說明</h2>

        <p>
        80 以上：市場非常強勢<br>
        60 - 80：偏多行情<br>
        40 - 60：震盪整理<br>
        20 - 40：偏弱行情<br>
        20 以下：市場恐慌
        </p>

        </div>
        """, unsafe_allow_html=True)

    except:

        st.error("查無股票資料")