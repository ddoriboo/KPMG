import streamlit as st
from PIL import Image
import base64

# 페이지 설정
st.set_page_config(page_title="KPMG AI 센터", layout="wide")

# 이미지 파일 경로 
img_path = "IMG_7287.png"

# 이미지를 base64로 인코딩
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 배경 이미지 설정 함수
def set_bg_hack(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 배경 이미지 설정
set_bg_hack(img_path)

# CSS 스타일 정의
css = """
<style>
    .link-button {
        background-color: rgba(255, 255, 255, 0.7);
        color: #00338D;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
        border: none;
        transition: background-color 0.3s, color 0.3s;
    }
    .link-button:hover {
        background-color: #00338D;
        color: white;
    }
    .container {
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: white;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# AI 상품 List 컨테이너
st.markdown("""
    <div class="container">
        <div class="title">AI 상품 List (selective)</div>
        <a href="https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=drive_link">AI 상시 PI</a><br>
        <a href="https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=drive_link">AI 거버넌스</a><br>
        <a href="https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=drive_link">AI 내부통제</a>
    </div>
""", unsafe_allow_html=True)

# 푸터
st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; background-color: rgba(0, 0, 0, 0.5); color: white; text-align: center; padding: 10px; font-size: 12px;'>
        © 2024 KPMG Samjong Accounting Corp., a Korea Limited Liability Company and a member firm of the KPMG global organization of independent member firms affiliated with KPMG International Limited, a private English company limited by guarantee. All rights reserved.
    </div>
""", unsafe_allow_html=True)
