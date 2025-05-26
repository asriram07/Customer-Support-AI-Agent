# support_ai_agent/app/api/routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agent.support_agent import SupportAgent

router = APIRouter()
agent = SupportAgent()

class SupportAgentRequest(BaseModel):
    prompt: str

@router.post("/support-agent")
async def support_agent_handler(req: SupportAgentRequest):
    try:
        result = agent.invoke(req.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
