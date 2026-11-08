from pydantic import BaseModel
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

class TextRequest(BaseModel):
    text: str

generator = pipeline(
    'translation',
    model='Helsinki-NLP/opus-mt-en-fr',
)

@app.post('/en-fr')
def translator(request: TextRequest):
    response = generator(
        request.text,
        max_new_tokens=55,
        num_return_sequences=1
    )

    translated_text = response[0]['translation_text']

    return {'translated_text': translated_text}