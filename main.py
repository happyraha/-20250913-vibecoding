import streamlit as st
st.title('나의 첫 웹앱')
st.write('2025. 9. 13. 서울 MS 본사에서 연수를 받았다')
import streamlit as st
from random import choice

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 명상 추천 💫", page_icon="🌸", layout="centered")

# 타이틀
st.title("🌿 MBTI 유형별 맞춤 명상 추천 🧘‍♀️✨")
st.write("당신의 MBTI 유형을 선택하면, 마음에 꼭 맞는 명상법을 추천해드려요 💖")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 유형별 추천 명상
meditation_recommendations = {
    "ISTJ": "✨ 규칙적인 호흡 명상 — 일정한 패턴을 유지하며 마음의 질서를 찾아보세요.",
    "ISFJ": "🌸 따뜻한 자기 연민 명상 — 스스로를 다정히 안아주는 시간을 가져보세요.",
    "INFJ": "🌌 시각화 명상 — 원하는 미래를 마음속에 그리며 평화를 느껴보세요.",
    "INTJ": "📖 분석적 명상 — 생각을 글로 정리한 후 마음을 비워보세요.",
    "ISTP": "🌊 자연소리 명상 — 파도, 바람 소리에 집중하며 자유를 느껴보세요.",
    "ISFP": "🎨 감각 명상 — 좋아하는 향기, 음악에 집중하며 감각을 깨워보세요.",
    "INFP": "💫 자비 명상 — 세상 모든 존재에게 따뜻한 마음을 보내보세요.",
    "INTP": "🔮 통찰 명상 — 스스로의 생각을 관찰하며 새로운 깨달음을 얻어보세요.",
    "ESTP": "🔥 에너지 호흡 명상 — 깊게 들이마시고 강하게 내쉬며 활력을 불어넣으세요.",
    "ESFP": "🎶 리듬 명상 — 음악에 맞춰 호흡하며 즐거운 흐름을 느껴보세요.",
    "ENFP": "🌈 창의적 명상 — 자유롭게 상상하며 마음의 날개를 펼쳐보세요.",
    "ENTP": "⚡ 아이디어 명상 — 떠오르는 생각들을 흘려보내며 에너지를 순환시켜보세요.",
    "ESTJ": "🪷 집중 명상 — 호흡에만 주의를 두며 질서를 세워보세요.",
    "ESFJ": "🤝 감사 명상 — 소중한 사람들을 떠올리며 따뜻한 마음을 전해보세요.",
    "ENFJ": "🌍 연결 명상 — 모두가 하나로 이어져 있음을 느껴보세요.",
    "ENTJ": "🎯 목표 명상 — 미래의 비전을 그리며 마음을 다잡아보세요."
}

# MBTI 선택
selected_mbti = st.selectbox("👉 MBTI 유형을 선택하세요:", mbti_types, index=None, placeholder="당신의 MBTI는?")

# 결과 출력
if selected_mbti:
    st.subheader(f"🌟 {selected_mbti} 님을 위한 추천 명상법")
    st.success(meditation_recommendations[selected_mbti])

    # 효과음 추가 (랜덤)
    sounds = [
        "https://www.soundjay.com/buttons/sounds/button-16.mp3",
        "https://www.soundjay.com/buttons/sounds/button-10.mp3",
        "https://www.soundjay.com/buttons/sounds/button-3.mp3"
    ]

    st.audio(choice(sounds))

    st.balloons()

# 푸터
st.write("---")
st.write("🌸 오늘도 당신의 마음이 고요하고 평화롭길 바랍니다 💖")
