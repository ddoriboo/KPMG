import streamlit as st

# 페이지 설정
st.set_page_config(page_title="KPMG AI 센터", layout="wide")

# CSS 스타일 정의
css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
    
    body {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #f0f0f0;
        color: #333;
    }
    .main-content {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #00338D;
        font-weight: 700;
    }
    .subtitle {
        color: #005EB8;
        font-weight: 500;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }
    .grid-item {
        background-color: #f8f8f8;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
    .grid-item h3 {
        color: #00338D;
        font-weight: 500;
    }
    .circle {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background-color: #00338D;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 10px;
        font-weight: 500;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .button {
        background-color: #00338D;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
        border: none;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #005EB8;
    }
    .ai-driven {
        font-size: 24px;
        font-weight: bold;
        color: #00338D;
        text-align: center;
        margin: 20px 0;
    }
    .footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# 메인 컨텐츠
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# 헤더
st.markdown("<h1>KPMG AI 센터</h1>", unsafe_allow_html=True)

# 서브헤더
st.markdown("""
    <p class="subtitle">
    KPMG 도메인 전문성과 AI기술 개발 역량을 결합하여 기업 비즈니스 혁신을 위한<br>
    전략적 파트너로 역할을 수행하고, 단발성 프로젝트가 아닌 지속적 가치 창출 관점으로 접근
    </p>
""", unsafe_allow_html=True)

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

    # AI Driven 텍스트
    st.markdown("<div class='ai-driven'>AI Driven</div>", unsafe_allow_html=True)

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

    st.markdown(f'<a href="{ai_pi_link}" target="_blank" class="button">AI 상시 PI</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{ai_governance_link}" target="_blank" class="button">AI 거버넌스</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{ai_internal_control_link}" target="_blank" class="button">AI 내부통제</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 푸터
st.markdown("""
    <div class='footer'>
        © 2024 KPMG Samjong Accounting Corp., a Korea Limited Liability Company and a member firm of the KPMG global organization of independent member firms affiliated with KPMG International Limited, a private English company limited by guarantee. All rights reserved.
    </div>
""", unsafe_allow_html=True)
