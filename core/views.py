from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request, "dashboard.html")

def Dashboard(request):
    return render(request, 'dashboard.html')