import streamlit as st
from PIL import Image
import base64

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

# 배경 이미지 설정
def set_bg_hack(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
        padding: 0;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 배경 이미지 설정
set_bg_hack('IMG_7287.png')

# 전체 화면 클릭 가능 영역 스타일 및 HTML
clickable_area_style = """
<style>
    .clickable-fullscreen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        cursor: pointer;
        z-index: 9999;
    }
</style>
"""

clickable_area_html = f"""
<a href="https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing" target="_blank" class="clickable-fullscreen">
</a>
"""

# 스타일과 클릭 가능한 영역 추가
st.markdown(clickable_area_style, unsafe_allow_html=True)
st.markdown(clickable_area_html, unsafe_allow_html=True)

# 페이지 콘텐츠를 비워두어 전체 화면 이미지만 표시
st.empty()
