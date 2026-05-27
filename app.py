import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# APP設定
st.set_page_config(
    page_title="股市天氣",
    page_icon="☀️",
    layout="centered"
)

# 標題
st.title("☀️ 股市天氣")
st.caption("人人看得懂的股票分析 APP")

# 股票輸入
stock_id = st.text_input(
    "輸入股票代碼",
    "2330.TW"
)

# 分析按鈕
if st.button("開始分析"):

    # 下載股票資料
    df = yf.download(
        stock_id,
        period="3mo",
        progress=False
    )

    # 防呆
    if len(df) < 5:

        st.error("股票資料不足")
        st.stop()

    # 價格
    current_price = float(df['Close'].iloc[-1])

    old_price = float(df['Close'].iloc[-5])

    # 五日漲跌
    change = (
        (current_price - old_price)
        / old_price
    ) * 100

    # 股票天氣
    if change >= 5:

        weather = "🌋 火山爆發"

        mood = "超級強勢"

        color = "red"

    elif change >= 2:

        weather = "☀️ 大晴天"

        mood = "多頭發動"

        color = "orange"

    elif change >= -2:

        weather = "🌤️ 多雲"

        mood = "觀望整理"

        color = "gray"

    else:

        weather = "🌧️ 暴風雨"

        mood = "空頭弱勢"

        color = "blue"

    # 顯示結果
    st.header(weather)

    st.subheader(mood)

    st.metric(
        "五日漲跌",
        f"{change:.2f}%"
    )

    st.metric(
        "目前價格",
        f"{current_price:.2f}"
    )

    # 圖表
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Close'],
            mode='lines',
            name='股價'
        )
    )

    fig.update_layout(
        title="股價走勢圖",
        xaxis_title="日期",
        yaxis_title="價格"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # AI建議
    st.divider()

    st.subheader("🤖 AI 股票人格")

    if change >= 5:

        st.success("這支股票像火箭，市場情緒極度樂觀。")

    elif change >= 2:

        st.info("這支股票像陽光型人格，偏強勢上漲。")

    elif change >= -2:

        st.warning("這支股票目前像觀察者，正在等待方向。")

    else:

        st.error("這支股票像暴風雨人格，市場偏悲觀。")