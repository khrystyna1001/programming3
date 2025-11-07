from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})