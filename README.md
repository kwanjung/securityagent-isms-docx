# ISMS-P 취약점 점검(모의침투) 결과보고서 생성기  (PDF → DOCX)

이 코드는 AWS Security Agent 워크샵에서 사용하기 위한 실습용 코드로, AWS Security Agent 모의침투 테스트 리포트(PDF)에서 정보를 추출하여 ISMS-P 2.11.2 점검 결과보고서 양식의 .docx 를 생성합니다.

<주의 : Security Agent 가 생성한 PDF 파일을 Doc 로 변환하여 결과보고서로 활용해 볼 수 있음을 보여주기 위한 Concept 코드 입니다. >

## 사용법:
    python generate_isms_report.py <pentest_report.pdf> [output.docx]
    python generate_isms_report.py report.pdf --no-translate          # 영문 원문 유지
    python generate_isms_report.py report.pdf --region ap-northeast-2  # Bedrock 리전 지정
    python generate_isms_report.py report.pdf --model us.anthropic.claude-opus-4-6-v1
    python generate_isms_report.py report.pdf --workers # 번역 병렬 스레드 수 (Default 8) 더 빠르게 하려면 --workers 12

## 의존성:
    pip install pdfplumber python-docx
    번역 사용 시(기본 ON): pip install boto3  +  Bedrock 모델 접근 권한/자격증명

## 번역:
    PDF에서 추출한 영문(취약점 설명·재현 절차·위험평가 근거)은 기본적으로
    Amazon Bedrock Claude 로 한국어 번역됩니다. Bedrock 미사용/오류 시 영문 원문을
    유지하고 경고만 출력합니다(--no-translate 로 비활성화).
    명령어·경로·페이로드·식별자는 번역하지 않고 원문 그대로 보존합니다.
    -workers 사용하다가 ThrottlingException 뜨는 경우 --workers 4 처럼 스레드 수를 낮춰주세요.

## 설계:
    extract_report()  : PDF 파싱 → dict (데이터)
    translate_data()  : 영문 서술 → 한국어 (Bedrock)
    build_docx()      : dict → ISMS-P 양식 .docx (렌더링)
    자동 채움 = 흰색 / 〔작성 필요〕 수기 입력 = 노랑(FFF2CC) 음영으로 구분
