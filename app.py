import streamlit as st
import pickle
import pandas as pd
import requests





movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))
# similarity = 'https://drive.google.com/file/d/1fxYE-iXTvkGRKUuYyZ0bT3lrQPqCLunb/view?usp=drive_link'
st.title('Movie Recommender System')

selected_movies_name = st.selectbox('Movies', movies_list['title'].values)

# getting title  from DataSet
def recommend(movies):
    index = movies_list[movies_list['title'] == movies].index[0]
    distance = similarity[index]
    recommended_movies_list = sorted(list(enumerate(distance)),reverse= True ,key = lambda x:x[1])[1:6]

    recommended_movies = []
  
    
    for i in recommended_movies_list:
        recommended_movies.append(movies_list.iloc[i[0]].title)

    return recommended_movies 

if st.button('Recommend'):
    recommendation = recommend(selected_movies_name)
    for i in recommendation:
        st.write(i)
