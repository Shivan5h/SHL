from fastapi import FastAPI, Request
from pydantic import BaseModel
from recommender import recommend_assessments

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/recommend")
def recommend(query: Query):
    recommendations = recommend_assessments(query.query)
    return {"query": query.query, "results": recommendations}
