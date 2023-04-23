from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request, "index.html")

def Dashboard(request):
    return render(request, 'dashboard.html')