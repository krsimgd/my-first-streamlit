
import streamlit as st

st.title('안녕하세요!')
st.write('제 첫 번째 스트림릿 앱입니다.')

name = st.text_input('이름을 입력하세요')
if name:
    st.write(f'안녕하세요, {name}님!')

number = st.slider('숫자를 선택하세요', 0, 100)
st.write(f'선택한 숫자: {number}')
