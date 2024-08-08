import streamlit as st
from PIL import Image
import os

# 페이지 설정
st.set_page_config(page_title="KPMG AI 센터", layout="wide", initial_sidebar_state="collapsed")

# Streamlit 기본 요소 및 Manage app 버튼 숨기기
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    .viewerBadge_container__1QSob {display: none !important;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# 이미지 파일의 절대 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'IMG_7287.png')

# 이미지 로드
try:
    image = Image.open(image_path)
except IOError:
    st.error(f"이미지를 불러올 수 없습니다. 파일 경로를 확인해주세요: {image_path}")
    st.stop()

# CSS 스타일 정의
css = """
<style>
    body {
        margin: 0;
        padding: 0;
        background-color: #0A2F5A;
    }
    .fullscreen-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }
    .content-wrapper img {
        max-width: 100%;
        max-height: 100vh;
        object-fit: contain;
    }
</style>
"""

# CSS 적용
st.markdown(css, unsafe_allow_html=True)

# 이미지 표시
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image(image, use_column_width=True)

# 클릭 가능한 영역 생성
if st.button('', key='fullscreen_button'):
    import webbrowser
    webbrowser.open_new_tab("https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing")

# 버튼 스타일 조정
st.markdown("""
    <style>
    .stButton>button {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: none;
        border: none;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)
