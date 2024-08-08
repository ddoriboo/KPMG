import streamlit as st

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
    .content-wrapper {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }
</style>
"""

# HTML 구조
html = f"""
<div class="fullscreen-container">
    <a href="https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing" target="_blank">
        <img src="IMG_7287.png" alt="KPMG AI 센터" class="content-wrapper">
    </a>
</div>
"""

# CSS와 HTML 적용
st.markdown(css, unsafe_allow_html=True)
st.markdown(html, unsafe_allow_html=True)

# 페이지 콘텐츠를 비워두어 전체 화면 이미지만 표시
st.empty()
