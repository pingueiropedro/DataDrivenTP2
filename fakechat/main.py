from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.language_models.fake import FakeListLLM

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

fake_llm = FakeListLLM(
    responses=[
        "Olá! Como posso ajudar?",
        "Python é uma linguagem de programação.",
        "FastAPI é um framework para criar APIs."
    ]
)

@app.post("/generate")
def generate_text(request: ChatRequest):
    response = fake_llm.invoke(request.message)

    return {"response": response}