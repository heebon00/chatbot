from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests, os
from dotenv import load_dotenv

load_dotenv()  # .env의 키를 추출하는 함수
app = FastAPI()
print(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Msg(BaseModel):
    text: str


HF_URL = "https://router.huggingface.co/v1/chat/completions"
HF_MODEL = "Qwen/Qwen3-4B-Instruct-2507"


def ask_ai(q: str) -> str:
    token = os.getenv("HF_TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="HF_TOKEN is not configured")

    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "model": HF_MODEL,
        "messages": [{"role": "user", "content": q}],
        "max_tokens": 300,
    }
    try:
        res = requests.post(HF_URL, headers=headers, json=payload, timeout=30)
        data = res.json()
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail="Hugging Face request failed") from exc
    except ValueError as exc:
        raise HTTPException(status_code=502, detail="Hugging Face returned invalid JSON") from exc

    if not res.ok:
        detail = data.get("error", "Hugging Face rejected the request")
        raise HTTPException(status_code=res.status_code, detail=detail)

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise HTTPException(status_code=502, detail="Unexpected Hugging Face response") from exc


@app.post("/chat")
def chat(msg: Msg):
    reply = ask_ai(msg.text)
    return {"reply": reply}
