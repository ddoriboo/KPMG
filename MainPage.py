import streamlit as st

# 페이지 설정
st.set_page_config(page_title="KPMG AI 센터", layout="wide", initial_sidebar_state="collapsed")

# Streamlit 기본 요소 숨기기
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

# CSS 및 JavaScript 정의
css_js = """
<style>
    body {
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    .fullscreen-image {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        object-fit: contain;
        cursor: pointer;
    }
</style>
<script>
    function openLink() {
        window.open('https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing', '_blank');
    }
</script>
"""

# HTML 구조
html_content = f"""
<div onclick="openLink()">
    <img src="https://raw.githubusercontent.com/your-username/your-repo/main/IMG_7287.png" alt="KPMG AI 센터" class="fullscreen-image">
</div>
"""

# CSS, JavaScript, 및 HTML 적용
st.markdown(css_js, unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)

# 페이지 콘텐츠를 비워두어 전체 화면 이미지만 표시
st.empty()
