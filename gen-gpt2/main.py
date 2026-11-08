from pydantic import BaseModel
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

class TextRequest(BaseModel):
    prompt: str

generator = pipeline(
    'text-generation',
    model='gpt2'
)

@app.post('/generate')
async def text_generation(request: TextRequest):
    result = generator(
        request.prompt,
        max_new_tokens=55,
        num_return_sequences=1
    )

    generated_text = result[0]['generated_text']

    return {'generated_text': generated_text }