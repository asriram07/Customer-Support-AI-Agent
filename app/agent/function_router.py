# support_ai_agent/app/agent/function_router.py

from app.utilities.email import send_email
from app.utilities.case_fetcher import fetch_similar_cases, get_customer_cases

def dispatch(intent: str, variables: dict):
    if intent == "send_email":
        return send_email(**variables)
    elif intent == "fetch_similar_cases":
        return fetch_similar_cases(**variables)
    elif intent == "get_customer_cases":
        return get_customer_cases(**variables)
    else:
        raise ValueError(f"Unknown intent: {intent}")
