import openai
from fastapi import FastAPI


app = FastAPI()

@app.get("/GPT")
async def training():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "おすすめの筋トレは？"}
        ]
    )
    
    return {"response": completion['choices'][0]['message']['content']}