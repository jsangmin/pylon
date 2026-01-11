# Docker Desktop Installation Guide (Mac)

PostgreSQL 데이터베이스를 실행하기 위해 Docker Desktop 설치가 필요합니다.

## 1. 다운로드 및 설치
1.  **공식 홈페이지 접속**: [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
2.  사용 중인 Mac의 칩셋에 맞는 버전을 다운로드하세요.
    - **Apple Chip (M1/M2/M3)**: "Apple Chip" 버튼 클릭
    - **Intel Chip**: "Intel Chip" 버튼 클릭
3.  다운로드된 `.dmg` 파일을 열고, Docker 아이콘을 Applications(응용 프로그램) 폴더로 드래그하여 설치합니다.

## 2. 실행 및 설정
1.  `응용 프로그램` 폴더에서 **Docker**를 찾아 실행합니다.
2.  상단 메뉴바에 고래 모양 아이콘이 나타나면 실행 중인 것입니다.
3.  초기 설정 화면이 나오면 모두 기본값(Accept/Finish)으로 진행해도 좋습니다.

## 3. 설치 확인
터미널을 열고 다음 명령어를 입력하여 버전이 출력되면 성공입니다.
```bash
docker --version
docker-compose --version
```

## 4. 데이터베이스 실행
설치가 완료되면, 다시 프로젝트 폴더에서 DB를 실행해주세요.
```bash
docker-compose up -d
```
