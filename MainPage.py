import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="KPMG AI 센터", layout="wide", initial_sidebar_state="collapsed")

# Streamlit 기본 요소 숨기기
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# 이미지 로드 (이미지 파일이 스크립트와 동일한 디렉토리에 있다고 가정)
try:
    image = Image.open("IMG_7287.png")
except FileNotFoundError:
    st.error("이미지 파일을 찾을 수 없습니다. 'IMG_7287.png' 파일이 스크립트와 같은 디렉토리에 있는지 확인해주세요.")
    st.stop()

# 이미지 표시
st.image(image, use_column_width=True)

# 링크 버튼
if st.button("자세히 보기"):
    st.markdown("[KPMG AI 센터 자료 다운로드](https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing)")

# 추가 설명 (선택사항)
st.write("위 이미지를 클릭하거나 '자세히 보기' 버튼을 눌러 자세한 내용을 확인하세요.")
