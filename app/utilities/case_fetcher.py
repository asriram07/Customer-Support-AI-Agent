 # app/utilities/case_fetcher.py

from sqlalchemy.orm import Session
from app.db.models import CaseTask
from typing import List

def fetch_similar_cases(session: Session, query: str, customer_id: str = None) -> List[dict]:
    """
    Fetch cases that contain the query in the title or summary.
    Optionally filter by customer_id for personalization.
    """
    q = session.query(CaseTask).filter(
        CaseTask.summary.ilike(f"%{query}%")
    )
    if customer_id:
        q = q.filter(CaseTask.customer_id == customer_id)
    results = q.limit(5).all()

    return [
        {
            "case_id": c.id,
            "summary": c.summary,
            "link": f"/cases/{c.id}"
        }
        for c in results
    ]

def get_customer_cases(session: Session, customer_id: str) -> List[dict]:
    """
    Return all cases for a given customer from the database.
    """
    results = session.query(CaseTask).filter_by(customer_id=customer_id).limit(10).all()
    return [
        {
            "case_id": c.id,
            "title": c.title,
            "status": c.status,
            "link": f"/cases/{c.id}"
        }
        for c in results
    ]
