import streamlit as st

st.set_page_config(page_title="연애 코칭 앱", page_icon="💖")

st.title("💖 연애 코칭 앱")
st.write("간단한 연애 고민 상담 앱입니다!")

name = st.text_input("이름을 입력하세요")
problem = st.text_area("연애 고민을 적어주세요")

if st.button("코칭 받기"):
    if problem == "":
        st.warning("고민을 입력해주세요!")
    else:
        st.success(f"{name}님을 위한 연애 코칭 결과 💌")

        text = problem.lower()

        if "고백" in text:
            st.write("👉 너무 완벽한 타이밍을 기다리지 말고 자연스럽게 표현해보세요!")

        elif "싸움" in text:
            st.write("👉 감정보다 상대 입장을 먼저 들어보는 게 중요해요.")

        elif "짝사랑" in text:
            st.write("👉 작은 대화부터 시작하면서 친해져보세요!")

        elif "헤어" in text:
            st.write("👉 힘든 시간을 보내고 있겠지만 스스로를 먼저 챙겨주세요.")

        else:
            st.write("👉 솔직한 대화와 배려가 가장 중요해요!")
