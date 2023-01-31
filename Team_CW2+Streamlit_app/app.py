import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

#load models
#content = pickle.load(open('C:/Users/PC/Documents/ExploreDataScience/Projects/My_Projects/Unsupervised/Deployment/Team_CW2/saved_models', 'rb'))
content = pickle.load(open('saved_models/content_algo.pkl', 'rb'))
content_similar = pickle.load(open('saved_models/content_similar.pkl', 'rb'))

collaborative = pickle.load(open('saved_models/collaborative_algo.pkl', 'rb'))
collaborative_similar = pickle.load(open('saved_models/collaborative_similar.pkl', 'rb'))


hybrid = pickle.load(open('saved_models/hybrid_algo.pkl','rb'))
hybrid_similar = pickle.load(open('saved_models/hybrid_similar.pkl','rb'))

movie_dict = pickle.load(open('saved_models/movie_list.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
#Creat sidebar
with st.sidebar:
    selected = option_menu('Movie Recommeder System',
    ['Content Filter',
    'Collaborative Filter',
    'Hybrid Filter'],
    icons=['lighting-fill','person-dash-fill','person-dash'])

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = content[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    movie_list = distances[1:11]

    reccomended_movie_names = []
    for i in movie_list:
        #movie_id = movies.iloc[i[0]].movie_id
        reccomended_movie_names.append(movies.iloc[i[0]].title)
    return reccomended_movie_names

# Content Based Filter
if(selected == 'Content Filter'):
    # Page title
    st.title('Content Based Recommender')

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the List",
        movie_list
    )
    #title = st.text_input('Movie Title')

    # Create Predictions

    if st.button('Content Based Result'):
        reccomended_movie_names = recommend(selected_movie)

        st.text(reccomended_movie_names[0])
        st.text(reccomended_movie_names[1])
        st.text(reccomended_movie_names[2])
        st.text(reccomended_movie_names[3])
        st.text(reccomended_movie_names[4])
        st.text(reccomended_movie_names[5])
        st.text(reccomended_movie_names[6])
        st.text(reccomended_movie_names[7])
        st.text(reccomended_movie_names[8])
        st.text(reccomended_movie_names[9])


# Collaborative Based Filter
if(selected == 'Collaborative Filter'):
    # Page title
    st.title('Collaborative Based Recommender')

    title = st.text_input('Movie Title')

    # Create Predictions

    if st.button('Collaborative Based Result'):
        content_model = content.predict([title])

# Hybrid Based Filter
if(selected == 'Hybrid Filter'):
    # Page title
    st.title('Hybrid Based Recommender')

    title = st.text_input('Movie Title')

    # Create Predictions

    if st.button('Hybrid Based Result'):
        content_model = content.predict([title])