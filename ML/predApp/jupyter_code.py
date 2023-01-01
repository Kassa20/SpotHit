import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
import gdown
from IPython.display import display  
from ipywidgets import interact, Text

# for the ML
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from IPython import display
import ipywidgets as widgets


from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings("ignore")


data_url = 'https://drive.google.com/uc?id=1MIkOcP2JY_foloYAR5-Y60YyRVbRhQMs'

data_path = './spotify_data_urls.csv'
#gdown.download(data_url, data_path , True)

## Load in data
data = pd.read_csv(data_path)


X = data[['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']]
y = data[['Label']]


for lr_score in range(3):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

  lr = LogisticRegression()
  lr.fit(X_train,y_train)

  lr_score = lr.score(X_test,y_test)
  #print ("LR Score:", lr_score)



X_2 = data[['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']]
y_2 = data[['Label']]

X_train, X_test, y_train, y_test = train_test_split(X_2, y_2, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
#print("accuracy: ", accuracy)


music_data_url = 'https://drive.google.com/uc?id=1Q4UAv4FPPOlhmFWHkn4Y83dG6M51xnoM'
music_data_path = './data_with_most_lyrics.csv'
#gdown.download(music_data_url, music_data_path, True)

music_data = pd.read_csv(music_data_path)
music_data = music_data.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.2'])
music_data['lyrics'] = music_data['lyrics'].str.replace('\n', ' ')
available_songs = music_data["track_name"] 
available_songs = available_songs.tolist()

X_new = music_data[['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']]
music_data['hit_prediction'] = model.predict(X_new)



