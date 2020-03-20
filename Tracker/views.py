from django.shortcuts import render
from django.shortcuts import redirect

def check_auth(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        return render(request, 'tracker.html')
