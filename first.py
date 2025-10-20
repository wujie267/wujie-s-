import streamlit as st
# 导入Streamlit并用st代表它
st.title("🕶学员 离开 - ow档案")
# 创建一个标题展示元素，内容是全中文的
st.header("🔑基本信息")
# 创建一个文本，介绍一下leave
st.text("学员ID：onceagain—LEAVE")

st.text("注册时间:2020-10-25 17:20:42|精神状态：✅ 正常")

st.text("当前教室：实训楼204|安全等级：机密")

st.subheader('📊 技能矩阵')
# 创建要显示技能矩阵的内容

st.subheader('战绩展示')
# 创建要显示战绩展示的内容
c1, c2, c3 = st.columns(3)
c1.metric(label="命中率", value="65%", delta="-5.2%")
c2.metric(label="近战击杀", value="5633", delta="92")
c3.metric(label="脉冲炸弹命中率", value="67%", delta="-3.2%", delta_color="off")
# 定义列布局，分成3列
st.markdown("### 上分进度")
st.caption("上分进度")
st.progress(85) 


import streamlit as st
# 导入Streamlit并用st代表它
st.title("任务与代码展示")

st.subheader("📋 任务日志")

task_data = {
    "日期": ["2020-10-01", "2020-10-05", "2020-10-12"],
    "任务": ["学员日常档案", "排位英杰排行", "平均排行展示"],
    "状态": ["✅ 完成", "⏳ 前5", "❌ 未完成"],
    "难度": ["★★★★★", "★★★★☆", "★★★★☆"]
}

st.table(task_data)

st.subheader("🔒 最新代码成果")

code = """def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stealth_evade()
"""

st.code(code, language="python")

st.markdown(':green[>> SYSTEM MESSAGE:]''下一个任务目标已解锁...')

st.markdown(':green[>> TARGET: ]''课程管理系统')

st.markdown(':green[>> COUNTDOWN:]'' 2025-10-20 17:22:43')

st.text("系统状态: 在线 连接状态: 已加密")
