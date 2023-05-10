from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def IndexView(request):
    return render(request, "dashboard.html")

@login_required(login_url=settings.LOGIN_URL)
def Dashboard(request):
    return render(request, 'dashboard.html')