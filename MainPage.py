import streamlit as st
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

# 이미지를 base64로 인코딩
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 이미지 파일 경로 (실제 경로로 변경 필요)
image_path = "IMG_7287.png"

try:
    img_base64 = get_image_base64(image_path)
except FileNotFoundError:
    st.error("이미지 파일을 찾을 수 없습니다. 'IMG_7287.png' 파일이 스크립트와 같은 디렉토리에 있는지 확인해주세요.")
    st.stop()

# HTML과 CSS를 사용하여 클릭 가능한 이미지 생성
html_code = f"""
<style>
    .image-link {{
        display: block;
        width: 100%;
        text-align: center;
    }}
    .image-link img {{
        max-width: 100%;
        height: auto;
    }}
</style>
<a href="https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing" target="_blank" class="image-link">
    <img src="data:image/png;base64,{img_base64}" alt="KPMG AI 센터">
</a>
"""

# HTML 렌더링
st.markdown(html_code, unsafe_allow_html=True)

# 추가 설명
st.write("이미지를 클릭하여 자세한 내용을 확인하세요.")

# 기존의 버튼 유지 (선택 사항)
if st.button("자세히 보기 (버튼)"):
    st.markdown("[KPMG AI 센터 자료 다운로드](https://drive.google.com/file/d/1FcBc0E9W6pW97JaDMgE1HODSlqZFFmWF/view?usp=sharing)")
