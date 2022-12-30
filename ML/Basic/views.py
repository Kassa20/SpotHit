from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "logistic/index.html")

def user(request):
    username = request.GET['username']
    return render(request, "logistic/user.html", {
        'name': username
    })
    