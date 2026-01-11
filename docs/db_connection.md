# Database Connection Guide

## Connection Details
현재 실행 중인 Docker PostgreSQL에 접속하기 위한 정보입니다.

- **Host**: `localhost`
- **Port**: `5532`
- **Database**: `pylon_db`
- **Username**: `postgres`
- **Password**: `postgres`

## DB Tool Recommendations

### 1. JetBrains DataGrip
- **장점**:
    - 강력한 자동 완성 및 인텔리전스 (PyCharm과 유사한 경험).
    - 다이어그램(ERD) 시각화 기능이 매우 뛰어남.
    - 쿼리 콘솔과 UI가 매우 직관적이고 세련됨.
- **단점**:
    - 유료 (30일 무료 체험 가능).
    - DBeaver보다 리소스를 좀 더 차지함.
- **추천**: JetBrains 생태계(PyCharm 등)에 익숙하시거나, 강력한 시각화/관리 기능이 필요하다면 **강력 추천**합니다.

### 2. DBeaver
- **장점**:
    - 완전 무료 (Community Edition).
    - 매우 가볍고 빠름.
    - 거의 모든 종류의 DB를 지원.
- **단점**:
    - UI가 다소 투박함 (Eclipse 기반).
    - 자동 완성 기능이 DataGrip보다는 조금 약함.
- **추천**: 무료로 가볍게 스키마를 확인하거나 데이터를 조회할 때 좋습니다.

## DataGrip 연결 방법
1.  **DataGrip 실행** -> **New Project** 또는 기존 프로젝트 열기.
2.  좌측 상단 **+** 버튼 -> **Data Source** -> **PostgreSQL**.
3.  **General** 탭에서 위 Connection Details 입력.
4.  **Test Connection** 클릭 (Drivers 파일 다운로드가 필요할 수 있음).
5.  성공 시 **OK** 또는 **Apply**.
