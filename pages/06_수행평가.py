import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI 여행 추천 서비스",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI 여행 추천 서비스")
st.write("CSV 데이터를 활용한 여행지 추천 시스템")

# CSV 파일 불러오기
df = pd.read_csv("pages/travel_data.csv")

col1, col2, col3 = st.columns(3)

with col1:
    budget = st.slider("예산(만원)", 50, 500, 200)

with col2:
    days = st.slider("여행기간(일)", 1, 14, 5)

with col3:
    style = st.selectbox(
        "여행스타일",
        ["도시", "휴양", "자연", "문화"]
    )

keyword = st.text_input("여행지 검색")

if st.button("추천받기"):

    result = []

    for _, row in df.iterrows():

        score = 0

        if row["스타일"] == style:
            score += 50

        score += max(
            0,
            50 - abs(row["예산"] - budget)
        )

        score += max(
            0,
            30 - abs(row["기간"] - days) * 5
        )

        result.append({
            "국가": row["국가"],
            "스타일": row["스타일"],
            "예산": row["예산"],
            "기간": row["기간"],
            "점수": score
        })

    result_df = pd.DataFrame(result)

    if keyword:
        result_df = result_df[
            result_df["국가"].str.contains(
                keyword,
                case=False,
                na=False
            )
        ]

    result_df = result_df.sort_values(
        by="점수",
        ascending=False
    )

    st.success("추천 결과 TOP 10")

    for _, row in result_df.head(10).iterrows():

        st.subheader(f"🌍 {row['국가']}")

        st.write(f"스타일 : {row['스타일']}")
        st.write(f"예산 : {row['예산']}만원")
        st.write(f"기간 : {row['기간']}일")
        st.write(f"추천점수 : {row['점수']:.0f}")

        st.progress(min(int(row["점수"]), 100))

        st.divider()

st.subheader("전체 여행지 데이터")
st.dataframe(df, use_container_width=True)
