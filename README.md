# FastAPI Example Project

FastAPI, PostgreSQL, SQLAlchemy, Docker, Kubernetes를 활용한 REST API 예제 프로젝트입니다.

## 🚀 주요 기능 (Features)

- **FastAPI**: 고성능 Python 웹 프레임워크 사용
- **PostgreSQL**: Docker를 이용한 데이터베이스 환경 구성
- **SQLAlchemy ORM**: 유연한 데이터베이스 연동
- **Bcrypt Security**: `passlib`와 `bcrypt`를 이용한 안전한 비밀번호 해싱
- **API Documentation**:
    - **Redoc**: 깔끔한 API 문서 제공 ([/redoc](http://localhost:8000/redoc))
    - **Swagger UI**: 대화형 API 테스트 도구 제공 ([/docs](http://localhost:8000/docs))
- **Docker & Kubernetes**: 컨테이너 기반 배포 설정 (`Dockerfile`, `k8s/` manifests)

## 🛠️ 시작 가이드 (Quick Start)

### 1. 사전 요구사항 (Prerequisites)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for Mac/Windows)
- Python 3.9+

### 2. 프로젝트 설치
```bash
# Repository 클론
git clone https://github.com/jsangmin/fastapi-example.git
cd fastapi-example

# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### 3. 데이터베이스 실행 (Docker)
로컬 개발 환경에서는 Docker Compose를 사용하여 PostgreSQL을 실행합니다.
```bash
docker-compose up -d
```
- **DB 접속 정보**: `localhost:5432` (User: `postgres`, Password: `postgres`, DB: `fastapi_db`)

### 4. 애플리케이션 실행
```bash
uvicorn app.main:app --reload
```
서버가 정상적으로 실행되면 `http://localhost:8000` 에서 접속 가능합니다.

## ✅ 테스트 방법

1.  **API 문서 접속**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
2.  **사용자 목록 조회**: `GET /api/v1/users/`
3.  **사용자 생성**: `POST /api/v1/users/`
    - 비밀번호는 자동으로 Bcrypt로 해싱되어 저장됩니다.

## 📂 프로젝트 구조
```
.
├── app
│   ├── api         # API 라우터 및 엔드포인트
│   ├── core        # 설정(Config), 보안(Security), DB 연결
│   ├── models      # SQLAlchemy 모델
│   ├── schemas     # Pydantic 스키마
│   └── main.py     # 애플리케이션 진입점
├── docs            # 개발 문서 및 가이드
├── k8s             # Kubernetes 배포 매니페스트
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```
