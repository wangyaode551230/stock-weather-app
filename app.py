import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# =========================
# 頁面設定
# =========================

st.set_page_config(
    page_title="AI 台股情緒 App",
    page_icon="🔥",
    layout="centered"
)

# =========================
# 超清楚 UI
# =========================

st.markdown("""
<style>

/* 背景 */

.stApp{
    background:#020b1c;
}

/* 全站 */

html, body, [class*="css"]{
    color:#ffffff;
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
}

/* 主標題 */

.main-title{

    font-size:64px;

    font-weight:900;

    margin-bottom:25px;

    color:#ffffff;

    text-shadow:0 0 15px rgba(255,255,255,0.3);
}

/* 搜尋框 */

div[data-baseweb="select"] > div{

    background:#1d4d8f !important;

    border:3px solid #63b3ff !important;

    border-radius:20px !important;

    color:white !important;

    font-size:24px !important;

    font-weight:700 !important;

    min-height:65px !important;
}

/* 卡片 */

.stock-card{

    background:#12326b;

    border-radius:35px;

    padding:35px;

    margin-top:25px;

    box-shadow:0 10px 30px rgba(0,0,0,0.45);
}

/* 股票名稱 */

.stock-card h1{

    font-size:48px;

    font-weight:900;

    color:#ffffff;
}

/* 一般文字 */

.big-text{

    font-size:34px;

    font-weight:800;

    margin-top:18px;

    color:#ffffff;
}

/* 能量值 */

.energy{

    color:#00ff88;

    font-size:66px;

    font-weight:900;

    margin-top:25px;

    text-shadow:0 0 15px rgba(0,255,136,0.5);
}

/* AI解釋卡 */

.info-box{

    background:#ffffff;

    color:#000000;

    border-radius:30px;

    padding:30px;

    margin-top:30px;
}

/* 解釋標題 */

.info-box h1{

    font-size:42px;

    font-weight:900;

    color:#000000;
}

/* 解釋內容 */

.info-box p{

    font-size:28px;

    line-height:1.9;

    color:#111111;

    font-weight:700;
}

/* 圖表 */

.js-plotly-plot .plotly text{

    font-size:18px !important;

    fill:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 標題
# =========================

st.markdown(
    '<div class="main-title">🔥 AI 台股情緒 App</div>',
    unsafe_allow_html=True
)

# =========================
# 自動抓全部台股
# =========================
def load_stock_list():

    url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"

    try:
        tables = pd.read_html(url)

        df = tables[0]

        df.columns = df.iloc[0]

        df = df[1:]

        df[['code', 'name']] = df['有價證券代號及名稱'].str.split('　', expand=True)

        df = df[['code', 'name']]

        return df

     except:
            stock_data = [
            ("2330", "台積電"),
            ("2317", "鴻海"),
            ("2454", "聯發科"),
            ("2308", "台達電"),
            ("2603", "長榮"),
            ("2881", "富邦金"),
            ("2891", "中信金"),
            ("0050", "元大台灣50"),
    ]

    return pd.DataFrame(stock_data, columns=["code", "name"])
# 載入股票資料
stock_list = load_stock_list()

# 搜尋選單
stock_options = stock_list.apply(
    lambda x: f"{x['code']} {x['name']}",
    axis=1
)

# =========================
# 搜尋股票
# =========================

selected_stock = st.selectbox(
    "搜尋股票",
    stock_options
)

# 股票代號
stock_code = selected_stock.split(" ")[0]

# =========================
# 股票資料
# =========================

try:

    # 自動判斷台股市場
    ticker = None

    for suffix in [".TW", ".TWO"]:
        try:
            test = yf.Ticker(f"{stock_code}{suffix}")
            info = test.info

            if info and info.get("regularMarketPrice"):
                ticker = test
                break
        except:
            pass
        
    if ticker is None:
        st.error("查無股票資料")
        st.stop()

    info = ticker.info

    # 即時資訊
    fast = ticker.fast_info

    # 歷史資料
    hist = ticker.history(period="1mo")

    # 股價
    price = fast.get("lastPrice", 0)

    # 前一天價格
    previous = fast.get("previousClose", price)

    # 漲跌幅
    if previous:
        change = ((price - previous) / previous) * 100
    else:
        change = 0

    # =========================
    # AI 情緒分析
    # =========================

    if change >= 4:

        animal = "🦁 獅王型"

        weather = "☀️ 晴天"

        energy = 95

        mood = """
        今天市場非常熱。

        很多人正在買進這支股票，

        市場信心非常強。
        """

    elif change >= 1:

        animal = "🦊 狐狸型"

        weather = "🌤️ 多雲"

        energy = 75

        mood = """
        市場偏向樂觀。

        資金持續流入，

        熱度穩定增加。
        """

    elif change >= -2:

        animal = "🐱 貓咪型"

        weather = "🌧️ 小雨"

        energy = 50

        mood = """
        市場正在觀望。

        買盤沒有特別強，

        波動開始增加。
        """

    else:

        animal = "🐺 狼型"

        weather = "⛈️ 暴風雨"

        energy = 20

        mood = """
        市場有點緊張。

        賣壓增加，

        風險偏高。
        """

    # =========================
    # 股票卡片
    # =========================

    st.markdown(f"""
    <div class="stock-card">

    <h1>{selected_stock}</h1>

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
        line=dict(width=4)
    ))

    fig.update_layout(

        template="plotly_dark",

        height=450,

        paper_bgcolor="#12326b",

        plot_bgcolor="#12326b",

        font=dict(
            color="white",
            size=18
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =========================
    # AI 圖表解釋
    # =========================

    st.markdown(f"""
    <div class="info-box">

    <h1>📚 AI 圖表解釋</h1>

    <p>
    {mood}
    </p>

    <p>
    {animal} 代表目前市場情緒。

    能量值越高，

    代表市場越強勢。
    </p>

    <p>
    ☀️ 晴天：市場偏強<br>
    🌤️ 多雲：市場穩定<br>
    🌧️ 小雨：市場觀望<br>
    ⛈️ 暴風雨：市場風險較高
    </p>

    </div>
    """, unsafe_allow_html=True)

except:

    st.error("目前查不到資料")