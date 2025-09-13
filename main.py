import streamlit as st
import pandas as pd
import altair as alt
import os

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 국가별 분포 Top10", layout="wide")

# 데이터 불러오기 함수
@st.cache_data
def load_data():
    file_path = "countriesMBTI_16types.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            st.stop()
    return df

df = load_data()

st.title("🌍 MBTI 유형별 국가 Top 10 비교")
st.write("데이터를 기반으로 특정 MBTI 유형이 가장 많은 국가 Top 10을 확인할 수 있습니다.")

# MBTI 유형 선택
mbti_types = df.columns[1:]  # 첫 번째 열은 Country, 나머지는 MBTI 유형
selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

# Top 10 데이터 추출
top10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)

# Altair 차트 생성
chart = (
    alt.Chart(top10)
    .mark_bar(color="#4C78A8")
    .encode(
        x=alt.X(f"{selected_type}:Q", title=f"{selected_type} 비율"),
        y=alt.Y("Country:N", sort="-x", title="국가"),
        tooltip=["Country", selected_type]
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)
