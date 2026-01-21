import streamlit as st
import pickle
import requests

st.set_page_config(page_title="Movie Recommender", layout="wide")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return ""

# Load data
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies["title"].values

st.title("🎬 Movie Recommendation System")

# --- Top Posters (Carousel replacement) ---
st.subheader("🔥 Popular Movies")

poster_ids = [
    1632, 299536, 17455, 2830, 429422,
    9722, 13972, 240, 155, 598
]

cols = st.columns(5)
for i, movie_id in enumerate(poster_ids):
    with cols[i % 5]:
        st.image(fetch_poster(movie_id), use_container_width=True)

# --- Recommendation Logic ---
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# --- UI ---
selected_movie = st.selectbox("🎥 Select a movie", movies_list)

if st.button("✨ Show Recommendations"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i], use_container_width=True)
