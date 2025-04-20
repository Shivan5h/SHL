import json
from utils import get_embedding, load_vector_store, shl_data

VECTOR_STORE = load_vector_store("shl_data.json")

def recommend_assessments(user_query: str):
    query_vec = get_embedding(user_query)
    top_k = VECTOR_STORE.similarity_search_with_score(query_vec, k=10)

    recommendations = []
    for doc, score in top_k:
        item = {
            "Assessment Name": doc['name'],
            "URL": doc['url'],
            "Remote Support": doc['remote_support'],
            "Adaptive Support": doc['adaptive_support'],
            "Duration": doc['duration'],
            "Test Type": doc['test_type'],
            "Score": score
        }
        recommendations.append(item)
    return recommendations
