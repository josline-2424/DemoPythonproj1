from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def detail(request):
    return render(request, "detail.html")

def thanks(request):
    return render(request, "thanks.html")