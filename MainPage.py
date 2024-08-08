import streamlit as st
from PIL import Image
import base64

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

# 이미지를 base64로 인코딩
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 이미지 파일을 base64로 인코딩
img_base64 = get_base64_of_bin_file('IMG_7287.png')

# CSS 스타일 정의
css = f"""
<style>
    .stApp {{
        background-color: #0A2F5A;  /* KPMG 파란색 배경 */
    }}
    .fullscreen-container {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }}
    .content-wrapper {{
        width: 100%;
        height: 100%;
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: contain;
        background-position: center;
        background-repeat: no-repeat;
        cursor: pointer;
    }}
    @media (max-aspect-ratio: 16/9) {{
        .content-wrapper {{
            width: 100%;
            height: auto;
            aspect-ratio: 16 / 9;
        }}
    }}
    @media (min-aspect-ratio: 16/9) {{
        .content-wrapper {{
            width: auto;
            height: 100%;
            aspect-ratio: 16 / 9;
        }}
    }}
</style>
"""

# HTML 구조
html = f"""
<div class="fullscreen-container">
    <a href="https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing" target="_blank">
        <div class="content-wrapper"></div>
    </a>
</div>
"""

# CSS와 HTML 적용
st.markdown(css, unsafe_allow_html=True)
st.markdown(html, unsafe_allow_html=True)

# 페이지 콘텐츠를 비워두어 전체 화면 이미지만 표시
st.empty()
