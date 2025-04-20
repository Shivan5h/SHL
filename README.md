
# SHL - Smart Hiring Leverager 🧠💼

A cutting-edge GenAI-powered assessment and recommendation engine built to revolutionize recruitment, upskilling, and role matching for candidates and companies alike.

## 🚀 Overview

**SHL** (Smart Hiring Leverager) is an intelligent hiring assistant that leverages Large Language Models (LLMs), embeddings, and custom scoring logic to:

- Recommend personalized assessments based on candidate profiles.
- Evaluate submissions to generate scores and feedback.
- Match candidates to relevant roles or skill-based upskilling paths.
- Help recruiters and L&D teams find the best-fit candidates faster.

## 📂 Project Structure

```
SHL/
│
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── recommender.py          # Recommendation logic
│   ├── utils.py                # Embedding, vector store, SHL data loader
│   ├── vectorstore/            # ChromaDB or FAISS vector store files
│
├── frontend/
│   ├── public/                 # Assets
│   ├── src/                    # ReactJS frontend source
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── ...
│
├── data/
│   ├── candidates.csv          # Candidate data
│   ├── questions.csv           # Assessment questions
│   └── roles.csv               # Role & skill mapping
│
├── requirements.txt            # Backend Python dependencies
├── package.json                # Frontend dependencies
├── README.md                   # Project documentation
└── .gitignore
```

## 🛠 Tech Stack

| Layer       | Tools/Tech                           |
|-------------|--------------------------------------|
| Backend     | FastAPI, SentenceTransformers, ChromaDB |
| Frontend    | React.js, Tailwind CSS               |
| Embeddings  | MiniLM (via HuggingFace)             |
| Vector Store| ChromaDB                             |
| Hosting     | (To be deployed)                     |

## 🧠 Features

- 🔍 **Candidate Similarity Search** using vector embeddings
- 🧪 **Assessment Generation** by role match
- 📊 **Score Evaluation** with semantic comparison
- 🧭 **Role Recommendation** based on skills and interests
- 🌐 **Interactive Frontend** for recruiters & candidates

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Shivan5h/SHL.git
cd SHL
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 4. Troubleshooting HuggingFace Cache

If you face an issue with missing models:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
```

Manually run this snippet once to download the required model into cache.

Or delete broken cache:

```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.cache\huggingface"
```

## 🤝 Contributions

PRs, ideas, and feedback are welcome! Let's make hiring smarter together.

## 📄 License

MIT License © 2024 [Shivan5h](https://github.com/Shivan5h)
