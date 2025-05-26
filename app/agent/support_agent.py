# support_ai_agent/app/agent/support_agent.py

from app.agent.function_router import dispatch
from app.agent.prompts.intent_classifier import classify_intent

class SupportAgent:
    def invoke(self, prompt: str) -> dict:
        parsed = classify_intent(prompt)
        if "intent" not in parsed or "variables" not in parsed:
            raise ValueError("Intent classification failed")
        result = dispatch(parsed["intent"], parsed["variables"])
        return {
            "intent": parsed["intent"],
            "response": result
        }
