from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'GET':
        return render(request, "register.html", 
                      {'form': RegisterForm()})

