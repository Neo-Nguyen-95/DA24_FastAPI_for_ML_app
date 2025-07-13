from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def root(name: str = "World"):
    ai_response = ai_greet(name)
    return {"message": ai_response}

def ai_greet(name: str) -> str:
    return f"Hellow {name}, I'm AI, nice to meet you"
