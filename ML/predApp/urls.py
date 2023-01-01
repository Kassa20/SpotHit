from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("result", views.formInfo, name="result")
    #path("add", views.add, name="add")
]

