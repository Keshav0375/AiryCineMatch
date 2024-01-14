import streamlit as st
import pickle
import requests
def fetch_Poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d8dc0488688424fc3912a0f9e27e1ff2&languages=enUS'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    
def recommend(movie):
    index = movies_data[movies_data['title'] == movie].index[0]
    distances=similarity[index]
    movie_lists = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_lists:
        movie_id=movies_data.iloc[i[0]].id
        recommended_movies.append(movies_data.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_Poster(movie_id))
    return recommended_movies,recommended_movies_posters
        
    
similarity=pickle.load(open('similarity.pkl','rb'))
movies_data=pickle.load(open('movies.pkl','rb'))
movies_list=movies_data['title'].values
st.title("AiryCineMatch")

selected_movie_name=st.selectbox("search a movie",movies_list)

if st.button("recommend"):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3 , col4 , col5= st.columns(5, gap='medium')
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])