import streamlit as st
import pickle
import requests



# Header
st.header("Movies Recommendation System")
movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list = movies['title'].values

selected_movie=st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path', '')
    if poster_path:
        full_path = "http://image.tmdb.org/t/p/w500" + poster_path
    else:
        full_path = "https://via.placeholder.com/500x750?text=No+Image"
    return full_path



def recommend(movie):
    index = movies[movies['title']== movie].index[0]
    distances= sorted(list(enumerate(similarity[index])),reverse=True, key= lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster


 
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
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