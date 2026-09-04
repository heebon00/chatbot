# AI Chatbot Web Application

FastAPI(백엔드)와 React + Vite(프론트엔드) 기반의 AI 챗봇 웹 애플리케이션입니다.
Hugging Face의 `Qwen/Qwen3-4B-Instruct-2507` 모델 API를 사용하여 실시간 답변을 생성합니다.

## 프로젝트 구조

```
chatbot/
├── backend/             # FastAPI 백엔드
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/            # React + Vite 프론트엔드
│   ├── src/
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## 시작하기

### 1. 백엔드 설정 및 실행

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

# .env 파일 생성 및 Hugging Face API 토큰 설정
# .env 파일에 다음 내용 추가:
# HF_TOKEN=your_huggingface_token

uvicorn main:app --reload
```

백엔드 서버는 기본적으로 `http://localhost:8000`에서 실행됩니다.

### 2. 프론트엔드 설정 및 실행

```bash
cd frontend
npm install
npm run dev
```

프론트엔드 개발 서버는 기본적으로 `http://localhost:5173`에서 실행됩니다.
나의 챗봇 주소 ~ https://frontend-chatbot-2fti.onrender.com/
