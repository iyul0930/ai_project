import streamlit as st

st.title("🌏 여행지 추천 서비스")

budget = st.slider("예산(만원)", 50, 500, 200)

travel_type = st.selectbox(
    "여행 스타일",
    ["휴양", "도시", "자연"]
)

if st.button("추천받기"):

    if travel_type == "휴양":
        st.success("추천 여행지: 베트남 다낭")

    elif travel_type == "도시":
        st.success("추천 여행지: 일본 도쿄")

    else:
        st.success("추천 여행지: 뉴질랜드")
