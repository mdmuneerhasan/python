import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

columns = ["user", "movie", "rating", "time"]
df = pd.read_csv("../ml-100k/u.data", sep="\t", names=columns)
movie_name = pd.read_csv("../ml-100k/u.item", sep="\|", header=None)
movie_name = movie_name[[0, 1]]
movie_name.columns = ['movie', 'name']

df = pd.merge(df, movie_name, on='movie')
rating = pd.DataFrame(df.groupby('name').mean()['rating'])
rating['number of ratings'] = pd.DataFrame(df.groupby('name').count()['rating'])

print(rating.sort_values(by='rating', ascending=False))

plt.figure(figsize=(10, 6))
plt.hist(rating['rating'], bins=70)
# plt.savefig("rating")

sns_plot = sns.jointplot(x='rating', y='number of ratings', data=rating, alpha=0.5)
# sns_plot.savefig("sns")

movie_mat = df.pivot_table(index="user", columns="name", values="rating")

print(movie_mat)


def predict_movies(movie_name):
    movie_user_ratings = movie_mat[movie_name]
    similar_movies=movie_mat.corrwith(movie_user_ratings)
    corr_movie=pd.DataFrame(similar_movies,columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie=corr_movie.join(rating['number of ratings'])
    predictions=corr_movie[corr_movie['number of ratings']>100].sort_values('Correlation',ascending=False)
    return predictions

print(predict_movies("Titanic (1997)"))