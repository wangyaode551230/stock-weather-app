import streamlit as st
import random

st.set_page_config(
    page_title="股市天氣",
    page_icon="📈",
    layout="centered"
)

# ======================
# CSS
# ======================

st.markdown("""
<style>

html, body, [class*="css"]{
    background:#03153a;
    color:white;
    font-family:sans-serif;
}

.block-container{
    padding-top:1rem;
    padding-bottom:3rem;
}

/* 主卡片 */

.weather-card{
    background:linear-gradient(135deg,#ffb347,#ffd93d);
    padding:35px;
    border-radius:30px;
    margin-bottom:30px;
    color:white;
}

/* 股票卡 */

.stock-card{
    background:#071633;
    padding:25px;
    border-radius:28px;
    margin-top:20px;
    box-shadow:0 8px 30px rgba(0,0,0,0.3);
}

/* 能量值 */

.energy{
    font-size:60px;
    font-weight:bold;
    color:#57f287;
}

/* 標題 */

.title{
    font-size:52px;
    font-weight:bold;
    margin-bottom:20px;
}

/* 搜尋框 */

.stTextInput input{
    background:rgba(255,255,255,0.08) !important;
    color:white !important;

    border:1px solid rgba(255,255,255,0.08) !important;

    border-radius:18px !important;

    height:52px !important;

    font-size:20px !important;

    padding-left:20px !important;

    backdrop-filter: blur(10px);

    box-shadow:0 4px 20px rgba(0,0,0,0.25);

}

</style>
""", unsafe_allow_html=True)

# ======================
# 主天氣卡
# ======================

st.markdown("""
<div class="weather-card">

<h3>今日市場天氣</h3>

<h1 style="font-size:72px;">
晴天 ☀️
</h1>

<h2>市場偏樂觀</h2>

<h2>資金流入，人氣上升中！</h2>

</div>
""", unsafe_allow_html=True)

# ======================
# 搜尋
# ======================

st.markdown('<div class="title">🔥熱門股票人格榜</div>', unsafe_allow_html=True)

stock_code = st.text_input(
    "",
    placeholder="輸入股票代號，例如 2330",
    label_visibility="collapsed"
)
# ======================
# 股票資料
# ======================

stocks = [

{
    "rank":"#1",
    "code":"2330",
    "name":"台積電",
    "animal":"獅王型",
    "icon":"🦁",
    "weather":"☀️ 晴天",
    "energy":"82"
},

{
    "rank":"#2",
    "code":"2603",
    "name":"長榮",
    "animal":"狼型",
    "icon":"🐺",
    "weather":"⛈️ 暴風雨",
    "energy":"76"
},

{
    "rank":"#3",
    "code":"2317",
    "name":"鴻海",
    "animal":"穩健型",
    "icon":"🐢",
    "weather":"☁️ 多雲",
    "energy":"65"
},

{
    "rank":"#4",
    "code":"2454",
    "name":"聯發科",
    "animal":"狡猾型",
    "icon":"🦊",
    "weather":"🌧️ 下雨",
    "energy":"45"
},

{
    "rank":"#5",
    "code":"2881",
    "name":"富邦金",
    "animal":"海豚型",
    "icon":"🐬",
    "weather":"☁️ 多雲",
    "energy":"58"
}

]

# ======================
# 顯示股票卡
# ======================

for s in stocks:

    if stock_code == "" or stock_code in s["code"]:

        st.markdown(f"""
        <div class="stock-card">

        <h1>
        {s["rank"]} {s["code"]} {s["name"]}
        </h1>

        <h2>
        {s["icon"]} {s["animal"]}
        </h2>

        <h2>
        {s["weather"]}
        </h2>

        <div class="energy">
        能量值：{s["energy"]}
        </div>

        </div>
        """, unsafe_allow_html=True)

# ======================
# 圖表解釋
# ======================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="title">
📚 圖表解釋
</div>
""", unsafe_allow_html=True)

# 天氣解釋

st.markdown("""
<div class="stock-card">

<h2>☀️ 晴天</h2>
<h3>市場偏樂觀，股價穩定上升。</h3>

<hr>

<h2>☁️ 多雲</h2>
<h3>市場觀望中，方向不明。</h3>

<hr>

<h2>🌧️ 下雨</h2>
<h3>市場偏弱，容易震盪。</h3>

<hr>

<h2>⛈️ 暴風雨</h2>
<h3>波動劇烈，高風險。</h3>

</div>
""", unsafe_allow_html=True)

# 動物人格

st.markdown("""
<div class="stock-card">

<h2>🦁 獅王型</h2>
<h3>市場領導者，人氣高。</h3>

<hr>

<h2>🐺 狼型</h2>
<h3>波動大，攻擊性強。</h3>

<hr>

<h2>🐢 穩健型</h2>
<h3>適合長期持有。</h3>

<hr>

<h2>🦊 狡猾型</h2>
<h3>容易突然爆發。</h3>

<hr>

<h2>🐬 海豚型</h2>
<h3>穩定成長型股票。</h3>

</div>
""", unsafe_allow_html=True)

# 能量值解釋

st.markdown("""
<div class="stock-card">

<h2>🔥 80 - 100</h2>
<h3>市場非常強勢</h3>

<hr>

<h2>📈 60 - 80</h2>
<h3>偏強勢</h3>

<hr>

<h2>➖ 40 - 60</h2>
<h3>普通</h3>

<hr>

<h2>📉 20 - 40</h2>
<h3>偏弱勢</h3>

<hr>

<h2>❄️ 0 - 20</h2>
<h3>非常弱勢</h3>

</div>
""", unsafe_allow_html=True)