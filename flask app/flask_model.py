# 1. Imports

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 2. Data loading

df = pd.read_csv("../data/movie_metadata.csv")

# 3. Data preprocessing

df.dropna(axis=0,subset=['director_name', 'num_critic_for_reviews','duration','director_facebook_likes','actor_3_facebook_likes','actor_2_name',
                         'actor_1_facebook_likes','actor_1_name','actor_3_name','facenumber_in_poster','num_user_for_reviews','language','country',
                         'actor_2_facebook_likes','plot_keywords', 'color', 'content_rating', 'aspect_ratio'],inplace=True)

df["budget"].fillna(df["budget"].median(),inplace=True)
df['gross'].fillna(df['gross'].median(),inplace=True)
df.drop_duplicates(inplace=True)

# 4. Cleaning outliers

Q1 = df['budget'].quantile(0.25)
Q3 = df['budget'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['budget'] >= lower_bound) & (df['budget'] <= upper_bound)]

Q1 = df['cast_total_facebook_likes'].quantile(0.25)
Q3 = df['cast_total_facebook_likes'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['cast_total_facebook_likes'] >= lower_bound) & (df['cast_total_facebook_likes'] <= upper_bound)]

# 5. Prepare data for model

X = df[['num_critic_for_reviews', 'duration', 'num_voted_users',
       'num_user_for_reviews', 'imdb_score', 'movie_facebook_likes']]
y = df['imdb_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 6. Modelling

model = DecisionTreeRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error: ", mae)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error: ", mse)

# 7. 
