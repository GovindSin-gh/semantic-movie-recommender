## 🎬 Semantic Movie Recommender System

A **semantic, content-based movie recommendation system** that suggests movies based on **meaning and narrative similarity**, not just shared keywords or predefined clusters.

The system uses **transformer-based NLP embeddings** to understand movie plots and recommends the most semantically similar movies using similarity ranking.

---

## 🚀 Live Demo

👉 **Deployed App:** https://<your-render-url>.onrender.com

---

## 🧠 Project Overview

Traditional movie recommenders rely on keyword overlap or clustering-based grouping, which often fails to capture deeper narrative similarity.

This project addresses that limitation by:

* Representing each movie as a **semantic embedding**
* Comparing movies based on **contextual meaning**
* Ranking recommendations by **semantic similarity**

The result is a recommender that feels more **human-like and intuitive**.

---

## ⚙️ How the Recommendation Works

1. Movie overviews are converted into **dense semantic vectors** using a pretrained transformer model.
2. Each movie becomes a point in a **semantic embedding space**.
3. When a user selects a movie:

   * Its embedding is retrieved
   * Similarity scores are computed against all other movies
4. Movies are **ranked by cosine similarity**
5. Top-K most semantically similar movies are recommended

> No ratings, labels, or supervised training are required.

---

## 🛠️ Tech Stack

* **Python**
* **Sentence Transformers (SBERT)** – semantic embeddings
* **NumPy** – numerical operations
* **Scikit-learn** – cosine similarity
* **Pandas** – data handling
* **Streamlit** – frontend UI
* **Render** – deployment

---

## 📂 Project Structure (Minimal & Clean)

```
semantic-movie-recommender/
│
├── movies.csv              # Movie metadata
├── embeddings.npy          # Precomputed semantic embeddings
├── recommender.ipynb       # Offline embedding generation & testing
├── app.py                  # Streamlit application
├── requirements.txt
└── README.md
```

---

## 🧩 Design Decisions

* **Embeddings are generated offline** to avoid memory constraints during deployment.
* The deployed app performs **lightweight inference only**, mirroring real-world production systems.
* Heavy preprocessing (stopwords, stemming) is intentionally avoided, as transformer models learn contextual importance internally.

---

## 🎯 Key Learnings

* Semantic representation learning using transformer models
* Designing recommendation systems without labeled data
* Separating offline computation from online inference
* Building deployable ML systems under resource constraints
* Understanding the difference between clustering and ranking-based recommendation logic

---

## 📌 Future Improvements

* Add user profile embeddings (multi-movie preference)
* Introduce unsupervised clustering for exploration and diversity
* Optimize similarity search using FAISS
* Add feedback-based personalization
* Convert backend to FastAPI for scalability

---

## 👤 Author

**Govind Singh**
Aspiring **MLOps Engineer** | ML, NLP & Deployment Enthusiast

---

⭐ If you found this project useful, consider giving it a star!

---

