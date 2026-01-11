<!--
[용도]
이 파일은 에이전트(AI)가 따라야 할 프로젝트별 규칙과 선호 사항을 정의합니다.
언어 설정, 기술 스택, 코딩 스타일, 행동 지침 등을 명시하여 에이전트의 일관된 출력을 보장합니다.

[사용법]
- 에이전트가 기억해야 할 절대적인 규칙을 추가합니다.
- 프로젝트 중간에 규칙이 변경되면 이 파일을 업데이트합니다.
-->
# Project Rules

## Communication
- **Language**: Korean (한국어) for all questions and answers.

## Technology Stack
- **Framework**: Python FastAPI
- **API Documentation**: Redoc
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy

## Agent Behavior
- **Proactive Execution**: Execute tasks immediately without unnecessary questions.
- **Autonomy**: Drive the development process proactively.
- **Git Workflow**: Always `commit` and `push` changes BEFORE making new changes to files. This ensures a save point exists.

## Project Context
- REST API Server implementation.

