from fastapi import FastAPI, status

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return "Health check OK"

@app.get("/")
async def root():
    return {"message": "Hello World"}
