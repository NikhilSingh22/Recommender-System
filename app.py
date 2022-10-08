import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d773fa58459eefea4b5d0f718cb1ae4c&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_id = []
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
         movie_id = movies.iloc[i[0]].movie_id
         #fetch poster
         recommended_movies_id.append(movie_id)
         recommended_movies.append(movies.iloc[i[0]].title)
         recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster , recommended_movies_id


movie_dict = pickle.load(open('./pickle/movie.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('./pickle/similarity.pkl', 'rb'))
st.title("Movie Recommendation System")

option = st.selectbox(
    'Select the movie for similar search',
    movies['title'].values)

if st.button('Recommend'):
    names,posters, m_id = recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
         st.text(names[0])
         st.image(posters[0])
         st.write(f'''
             <a target="_self" href="https://www.themoviedb.org/movie/{m_id[0]}">
                 <button>
                     watch
                 </button>
             </a>
             ''',
                  unsafe_allow_html=True
        )


    with col2:
         st.text(names[1])
         st.image(posters[1])
         st.write(f'''
                     <a target="_self" href="https://www.themoviedb.org/movie/{m_id[1]}">
                         <button>
                             watch
                         </button>
                     </a>
                     ''',
             unsafe_allow_html=True
         )
    with col3:
         st.text(names[2])
         st.image(posters[2])
         st.write(f'''
            <a target="_self" href="https://www.themoviedb.org/movie/{m_id[2]}">
                    <button>
                        watch
                    </button>
            </a>
            ''',
            unsafe_allow_html=True
         )
    with col4:
         st.text(names[3])
         st.image(posters[3])
         st.write(f'''
                    <a target="_self" href="https://www.themoviedb.org/movie/{m_id[3]}">
                            <button>
                                watch
                            </button>
                    </a>
                    ''',
             unsafe_allow_html=True
         )
    with col5:
         st.text(names[4])
         st.image(posters[4])
         st.write(f'''
                     <a target="_self" href="https://www.themoviedb.org/movie/{m_id[4]}">
                             <button>
                                 watch
                             </button>
                     </a>
                     ''',
                  unsafe_allow_html=True
         )

