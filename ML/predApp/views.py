from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from joblib import load
from .jupyter_code import *


model = load('./savedModels/model.joblib')


class MyForm(forms.Form):
    choices = available_songs
    select = forms.CharField(label='Select a song', 
    widget=forms.TextInput(attrs={'list': 'choices',
    'placeholder': 'Search'}))


def main(request):
    is_in_database = ''
    is_hit = ''
    select = ''
    accuracy = 0

    X_2 = data[['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']]
    y_2 = data[['Label']]

    X_train, X_test, y_train, y_test = train_test_split(X_2, y_2, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    a = (model.score(X_test, y_test)) * 100
    accuracy = round(a, 2)

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data['select']
            hit_songs = music_data.loc[music_data['hit_prediction'] == 1]
            is_hit = select in hit_songs['track_name'].values
            is_in_database = select in available_songs

            form = MyForm()
    else:
        form = MyForm()
        
    return render(request, "predApp/main.html", {
        'form': form,
        'acc': accuracy,
        'is_hit': is_hit,
        'song': select,
        'is_in_database': is_in_database
        })

def about(request):

    coef = lr.coef_
    features = pd.DataFrame(list(zip(X, coef[0])), columns=['feature', 'coef'])
    main_data = music_data[['artist_name', 'track_name', 'danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']].head().reset_index(drop=True)
    return render(request, "predApp/about.html", {
        'features': features,
        'main_data': main_data
    })





