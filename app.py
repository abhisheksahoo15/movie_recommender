import pickle
import requests
import streamlit as st

# Google Drive File URL
drive_file_url = "https://drive.google.com/uc?id=1hgLYVg5WcCz2Fr4JrGguQ2VIqwS4dTX8"

try:
    # Fetch the file from Google Drive
    response = requests.get(drive_file_url)
    response.raise_for_status()  # Raise an error for HTTP issues
    
    # Validate content type
    if "text/html" in response.headers["Content-Type"]:
        raise ValueError("Google Drive returned an HTML page instead of the pickle file. Check the file's permissions.")
    
    # Load pickle content
    similarity = pickle.loads(response.content)
except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch similarity.pkl from Google Drive. Network Error: {e}")
    similarity = None
except ValueError as e:
    st.error(f"Validation Error: {e}")
    similarity = None
except pickle.UnpicklingError as e:
    st.error(f"Failed to load pickle file. Unpickling Error: {e}")
    similarity = None

# Streamlit App
st.header('Movie Recommender System')

if similarity:
    # Load movie data
    movies = pickle.load(open('movie_list.pkl', 'rb'))

    # Movie selection
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
else:
    st.error("Similarity data could not be loaded. Please check the configuration.")
