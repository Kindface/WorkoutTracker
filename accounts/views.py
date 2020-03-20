from django.shortcuts import render

from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return render(request, 'tracker.html', {'form': form})
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
