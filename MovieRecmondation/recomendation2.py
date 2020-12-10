import warnings
import pandas as pd

warnings.filterwarnings('ignore')
col_name = ['user', 'movie', 'rating', 'time']
df = pd.read_csv("../ml-100k/u.data", sep="\t", names=col_name)
name = pd.read_csv("../ml-100k/u.item", sep="\|", header=None)
name = name[[0, 1]]
name.columns = ['movie', 'name']

df = pd.merge(df, name, on='movie')

movie_mat = df.pivot_table(index='user', columns='name', values='rating')
rating = pd.DataFrame(df.groupby('name').count()['rating'])


def predict_movies(movie_name):
    movie_user_rating = movie_mat[movie_name]
    similar_movie = movie_mat.corrwith(movie_user_rating)
    similar_movie.dropna(inplace=True)
    similar_movie2 = pd.DataFrame(similar_movie, columns=['correlation'])
    similar_movie2 = similar_movie2.join(rating)
    similar_movie2 = similar_movie2[similar_movie2['rating'] > 100].sort_values('correlation', ascending=False)
    return similar_movie2


print(predict_movies("Titanic (1997)"))
