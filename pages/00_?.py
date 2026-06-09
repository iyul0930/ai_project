import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI 여행지 추천기",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI 여행지 추천 서비스")

st.write("여행 정보를 입력하면 추천 여행지를 알려드립니다.")

travel_data = [
    {
        "국가":"일본 도쿄",
        "스타일":"도시",
        "예산":150,
        "기간":3,
        "설명":"쇼핑과 맛집, 가까운 해외여행"
    },
    {
        "국가":"베트남 다낭",
        "스타일":"휴양",
        "예산":100,
        "기간":5,
        "설명":"가성비 최고의 휴양지"
    },
    {
        "국가":"태국 푸켓",
        "스타일":"휴양",
        "예산":200,
        "기간":5,
        "설명":"리조트와 바다"
    },
    {
        "국가":"스위스",
        "스타일":"자연",
        "예산":450,
        "기간":7,
        "설명":"알프스와 자연풍경"
    },
    {
        "국가":"뉴질랜드",
        "스타일":"자연",
        "예산":400,
        "기간":7,
        "설명":"대자연 체험"
    }
]

budget = st.slider(
    "예산 (만원)",
    50,
    500,
    200
)

days = st.slider(
    "여행 기간",
    1,
    14,
    5
)

style = st.selectbox(
    "여행 스타일",
    ["도시","휴양","자연"]
)

if st.button("추천받기"):

    result = []

    for place in travel_data:

        if (
            place["스타일"] == style
            and place["예산"] <= budget
            and place["기간"] <= days
        ):
            result.append(place)

    if result:

        st.success("추천 결과")

        for place in result:

            st.subheader(place["국가"])

            st.write(
                f"💰 예상비용 : {place['예산']}만원"
            )

            st.write(
                f"📅 추천기간 : {place['기간']}일"
            )

            st.write(
                f"📌 {place['설명']}"
            )

            st.divider()

    else:

        st.warning(
            "조건에 맞는 여행지가 없습니다."
        )
