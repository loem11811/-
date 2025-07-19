import streamlit as st
st.set_page_config(page_title="친환경 약국 자가 평가", page_icon="💊")
st.title("💊 친환경 약국 자가 평가 프로그램")
st.write("각 항목에 대해 귀하의 약국에 해당하는 내용을 선택하거나 입력해주세요.")
total_score = 0
st.header("1. 폐의약품 수거함 설치 여부")

c1_choice = st.selectbox(
    '수거함 설치 상태를 선택하세요.',
    ('설치되어 있지 않음', '설치되어 있으나 접근이 어려움 (예: 약사에게 요청 필요)', '설치되어 있고 시민이 자유롭게 접근 가능')
)
if c1_choice == '설치되어 있지 않음':
    c1_score = 0
elif c1_choice == '설치되어 있으나 접근이 어려움 (예: 약사에게 요청 필요)':
    c1_score = 5
else:
    c1_score = 10
total_score += c1_score
st.header("2. 연간 폐의약품 회수량 (kg)")

c2_amount = st.number_input('연간 폐의약품 회수량을 kg 단위로 입력하세요.', min_value=0.0, format="%.1f")
if c2_amount < 1:
    c2_score = 2
elif 1 <= c2_amount < 3:
    c2_score = 5
elif 3 <= c2_amount < 6:
    c2_score = 8
else:
    c2_score = 10
total_score += c2_score
st.header("3. 에너지 절감 실천 여부")

c3_choice = st.radio(
    "에너지 절감 실천 상태를 선택하세요.",
    ('실천 없음', '일부만 적용', '주요 설비 모두 에너지 절감형으로 교체')
)
if c3_choice == '실천 없음':
    c3_score = 0
elif c3_choice == '일부만 적용':
    c3_score = 5
else:
    c3_score = 10
total_score += c3_score

st.header("4. 친환경 포장재 취급 비율 (%)")
c4_ratio = st.slider('친환경 포장재 취급 비율을 선택하세요.', 0, 100, 25)
if c4_ratio < 10:
    c4_score = 2
elif 10 <= c4_ratio < 30:
    c4_score = 4
elif 30 <= c4_ratio < 50:
    c4_score = 6
elif 50 <= c4_ratio < 70:
    c4_score = 8
else:
    c4_score = 10
total_score += c4_score

st.header("5. 환경 교육/캠페인 참여 횟수 (연간)")
c5_count = st.number_input('연간 참여 횟수를 입력하세요.', min_value=0, step=1)
if c5_count == 0:
    c5_score = 0
elif c5_count == 1:
    c5_score = 3
elif 2 <= c5_count <= 3:
    c5_score = 6
else:
    c5_score = 10
total_score += c5_score

st.markdown("---")
if st.button('📈 결과 확인하기'):
    if 45 <= total_score <= 50:
        grade, desc = "A등급 (Smart Green Pharmacy)", "스마트 친환경 약국 인증 대상"
    elif 35 <= total_score <= 44:
        grade, desc = "B등급 (Green Pharmacy)", "우수한 친환경 실천 약국"
    elif 25 <= total_score <= 34:
        grade, desc = "C등급 (Eco-aware Pharmacy)", "친환경 개선 여지 있는 약국"
    else: # 24점 이하
        grade, desc = "D등급 (Non-compliant)", "친환경 기준 미달 약국"

   
    st.success(f"**📊 총점: {total_score}점**")
    st.info(f"**🏅 최종 등급: {grade}**\n\n📝 설명: {desc}")
    
    
    st.balloons()
