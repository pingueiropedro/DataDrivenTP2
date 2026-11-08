## Projetos de LLMs com FastAPI e LangChain

Este repositório reúne exercícios de integração de modelos de linguagem e tradução com FastAPI, Hugging Face e LangChain.

## Projetos desenvolvidos

Parte 1

- Geração de texto (GPT-2): API que recebe um prompt e gera texto usando Hugging Face Transformers.
- Tradução inglês → francês: API com o modelo Helsinki-NLP/opus-mt-en-fr.

Parte 2

- Chatbot Fake LLM: simulação de respostas predefinidas com FakeListLLM e LangChain. As respostas são retornadas em sequência, sem interpretar a pergunta.
- Tradução inglês → francês com OpenAI: integração entre FastAPI, LangChain e ChatOpenAI.
- Tradução inglês → alemão: integração com o modelo local Helsinki-NLP/opus-mt-en-de via LangChain.

## Tecnologias

Python, FastAPI, Pydantic, LangChain, Hugging Face Transformers e OpenAI API.

## Como executar

Em cada pasta de projeto, instale as dependências correspondentes e execute:

uvicorn main:app --reload

Acesse http://127.0.0.1:8000/docs para testar os endpoints. Os caminhos das rotas podem variar entre os projetos.

