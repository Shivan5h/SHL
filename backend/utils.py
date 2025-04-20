import json
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # or Gemini API

def get_embedding(text: str):
    return model.encode([text])[0]

def load_vector_store(filepath):
    with open(filepath) as f:
        data = json.load(f)

    db = chromadb.Client()
    collection = db.create_collection("shl_assessments")

    for item in data:
        collection.add(
            documents=[item['description']],
            metadatas=[item],
            ids=[item['id']]
        )
    return collection

def shl_data():
    with open("shl_data.json") as f:
        return json.load(f)
