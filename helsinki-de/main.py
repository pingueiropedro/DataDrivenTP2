from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

app = FastAPI(title='English to German Translator!')

class TextRequest(BaseModel):
    text: str

translator_pipeline = pipeline(
    task='translation',
    model='Helsinki-NLP/opus-mt-en-de'
)

llm = HuggingFacePipeline(
    pipeline=translator_pipeline
)

@app.post('/Translation')
def german_translation(request: TextRequest):
    try:
        response = llm.invoke(request.text)

        return {'translation': response}

    except Exception:
        raise HTTPException(
            status_code=500,
            detail='Rate limit exceeded'
        )
    