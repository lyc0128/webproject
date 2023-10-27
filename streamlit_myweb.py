import streamlit as st


st.title('매천고 20720 이예찬')

checkbox_btn = st.checkbox('자기소개')
if checkbox_btn:
    st.write('이름:이예찬')
    st.write('생일 : 2006년 1월 28일')
    st.write('학교: 매천고등학교 2학년 7반 20번')
    st.write('MBTI : INTJ')

checkbox_btn = st.checkbox('동아리소개')
if checkbox_btn:
    st.write('소프트웨어 메이킹 동아리')
    st.write('장점 : 소프트웨어에 관해 자세하고 쉽게 이해할 수 있는 수업을 듣는다.')
    st.write('선생님이 마호돌 선생님이라 이해가 잘 되게 설명해 주신다.')

checkbox_btn = st.checkbox('학교소개')
if checkbox_btn:
    st.write('이름 : 매천고등학교')
    st.write('특징 : 학교가 만들어진지 얼마 안되서 시설이 좋다.')
    st.write('도서관이 매우 커서 책 읽기 편하다.')
    st.write('교조:독수리')
    st.write('교훈:필요한 사람이 되자 ')
    st.write('교화:매화')
    st.write('교목:소나무')
checkbox_btn = st.checkbox('관심분야')
if checkbox_btn:
    st.write('관심분야는 축구이다.')
    st.write('그이유는 단순한 스포츠이고 경기 자체가 열렬하기 떄문이다.')