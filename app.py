import pandas as pd
import streamlit as st
import joblib

movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity.pkl")


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    movie_indices = similarity[movie_index]

    recommendations = []
    for index in movie_indices:
        recommendations.append(movies.iloc[index]["title"])

    return recommendations


st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie recommendations.")

movie = st.selectbox(
    "Choose a movie",
    movies["title"].values
)

if st.button("Recommend"):
    recommendations = recommend(movie)

    st.subheader("Movies you may like:")

    for i, movie_name in enumerate(recommendations, 1):
        st.write(f"{i}. {movie_name}")
