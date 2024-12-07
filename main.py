import streamlit as st
import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('movies.csv')
    selected_cols = ['genres', 'keywords', 'cast', 'director', 'tagline']
    for col in selected_cols:
        data[col] = data[col].fillna('')
    data['combined_data'] = data['genres'] + ' ' + data['keywords'] + ' ' + data['cast'] + ' ' + data['director'] + ' ' + data['tagline']
    return data

# Compute TF-IDF vectors
@st.cache_data
def compute_similarity(data):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data['combined_data'])
    similarity = cosine_similarity(vectors)
    return similarity

# Function to recommend movies
def recommend_movies(movie_title, data, similarity_matrix):
    list_of_movies = data['title'].tolist()
    find_match = difflib.get_close_matches(movie_title, list_of_movies)
    
    if not find_match:
        return None
    
    closest_match = find_match[0]
    index = list_of_movies.index(closest_match)
    similar_scores = list(enumerate(similarity_matrix[index]))
    sorted_movies = sorted(similar_scores, reverse=True, key=lambda x: x[1])
    
    recommendations = []
    for i in range(1, 11):  # Skip the first movie as it is the input movie itself
        movie_index = sorted_movies[i][0]
        recommendations.append(data['title'].iloc[movie_index])
    return recommendations

# Streamlit App
st.set_page_config(page_title="Movie Recommender", layout="wide", page_icon="🎥")

# Sidebar for user input
st.sidebar.title("Movie Recommender System 🎬")
st.sidebar.write("Find movies similar to your favorites!")
user_input = st.sidebar.text_input("Enter your favorite movie:", "")

# Main content
st.title("Movie Recommendation System")
st.markdown("""
This application uses **Natural Language Processing (NLP)** and **Cosine Similarity** to recommend movies based on your favorite movie.  
Simply type the name of a movie you like in the sidebar, and let the system do the rest!  
""")

# Load data and compute similarity
data = load_data()
similarity_matrix = compute_similarity(data)

# Display recommendations
if user_input:
    st.subheader(f"Recommendations for '{user_input}':")
    recommendations = recommend_movies(user_input, data, similarity_matrix)
    
    if recommendations:
        for idx, movie in enumerate(recommendations, start=1):
            st.write(f"**{idx}. {movie}**")
    else:
        st.warning("Sorry, we couldn't find a match for your input. Please try again with a different movie.")
else:
    st.info("Enter the name of a movie in the sidebar to get recommendations.")
