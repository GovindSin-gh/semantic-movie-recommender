import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")
embeddings = np.load("embeddings.npy")

st.title("🎬 Semantic Movie Recommender")

movie = st.selectbox("Choose a movie", df['title'])

if st.button("Recommend"):
    idx = df[df['title'] == movie].index[0]
    sims = cosine_similarity([embeddings[idx]], embeddings)[0]
    top_idx = sims.argsort()[::-1][1:6]

    for i in top_idx:
        st.write(df.iloc[i]['title'])
