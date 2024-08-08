import streamlit as st
import base64

# 페이지 설정
st.set_page_config(page_title="KPMG AI 센터", layout="wide")

# 스타일 설정
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")  # style.css 파일을 만들어 스타일을 정의해야 합니다.

# 헤더
st.markdown("<h1 style='color: white;'>KPMG AI 센터</h1>", unsafe_allow_html=True)

# 서브헤더
st.markdown("""
    <p style='color: #FFD700;'>
    KPMG 도메인 전문성과 AI기술 개발 역량을 결합하여 기업 비즈니스 혁신을 위한<br>
    전략적 파트너로 역할을 수행하고, 단발성 프로젝트가 아닌 지속적 가치 창출 관점으로 접근
    </p>
""", unsafe_allow_html=True)

# 메인 컨텐츠
col1, col2 = st.columns([3, 1])

with col1:
    # 4개의 박스 생성
    st.markdown("""
        <div class='grid-container'>
            <div class='grid-item'>
                <h3>α 신성장 동력 창출</h3>
                <p>사업 지속가능성 제고 및 신사업 창출 위한 인텔리전스 강화</p>
                <ul>
                    <li>AI 도입전략 및 Use Case 도출</li>
                    <li>AI 기업 인수/매각/JV 등 지원</li>
                </ul>
            </div>
            <div class='grid-item'>
                <h3>+ 생산성/경쟁력 강화</h3>
                <p>미래 비즈니스 예측 및 경영 리스크 대응 분석 강화</p>
                <ul>
                    <li>AI 고객 마케팅 및 판매수익 강화</li>
                    <li>가격수요 예측 및 설비 최적화</li>
                </ul>
            </div>
            <div class='grid-item'>
                <h3>- 업무 재정립/최적화</h3>
                <p>AI (OCR, GenAI, NLP 등) 신기술 기반 업무 재구성, 효율화 달성</p>
                <ul>
                    <li>AI 기반 결산 업무 전반 혁신</li>
                    <li>자동화 플랫폼 구축</li>
                </ul>
            </div>
            <div class='grid-item'>
                <h3>% 리스크 예측/예방</h3>
                <p>과거에 탐지하지 못했던 리스크 식별 및 리스크 예방 강화</p>
                <ul>
                    <li>AI 부실 거래선/채권 예측</li>
                    <li>AI 보안 및 정보 유출 모니터링</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # AI Driven 이미지
    st.image("ai_driven_image.png", width=100)  # AI Driven 이미지를 추가해야 합니다.

    # 두 개의 원
    st.markdown("""
        <div style='display: flex; justify-content: space-around;'>
            <div class='circle'>AI를 접목한<br>Business<br>Transformation<br>파트너</div>
            <div class='circle'>AI를 활용한<br>Operational<br>Excellence 파트너</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<h3>AI 상품 List (selective)</h3>", unsafe_allow_html=True)
    
    # Google Drive 링크 (예시 링크, 실제 파일 링크로 교체 필요)
    ai_pi_link = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_1"
    ai_governance_link = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_2"
    ai_internal_control_link = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_3"

    if st.button('AI 상시 PI'):
        st.markdown(f'<a href="{ai_pi_link}" target="_blank">AI 상시 PI 문서 다운로드</a>', unsafe_allow_html=True)

    if st.button('AI 거버넌스'):
        st.markdown(f'<a href="{ai_governance_link}" target="_blank">AI 거버넌스 문서 다운로드</a>', unsafe_allow_html=True)

    if st.button('AI 내부통제'):
        st.markdown(f'<a href="{ai_internal_control_link}" target="_blank">AI 내부통제 문서 다운로드</a>', unsafe_allow_html=True)

# 푸터
st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; background-color: #333; color: white; text-align: center; padding: 10px;'>
        © 2024 KPMG Samjong Accounting Corp., a Korea Limited Liability Company and a member firm of the KPMG global organization of independent member firms affiliated with KPMG International Limited, a private English company limited by guarantee. All rights reserved.
    </div>
""", unsafe_allow_html=True)
