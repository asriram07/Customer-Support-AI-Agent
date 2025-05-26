# support_ai_agent/app/main.py

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Support AI Agent")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
