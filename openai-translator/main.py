from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from openai import RateLimitError, APITimeoutError
from langchain_core.messages import SystemMessage, HumanMessage

app = FastAPI()

class TextRequest(BaseModel):
    text: str

openai = ChatOpenAI(
    model='gpt-4.1-mini',
    temperature=0,
    max_retries=2,
    timeout=15
)

@app.post('/translation')
def translate_en_fr(request: TextRequest):
    try:
        response = openai.invoke([
            SystemMessage(
                content='Translate the following English text into French. ' \
                'Return only the accurate translation'
            ),
            HumanMessage(
                content=request.text
            )
        ])
    except RateLimitError:
        raise HTTPException(
            status_code=503,
            detail='OpenAI API rate limit exceeded'
        )
        
    return {'translation': response.content}