from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Languages(request):
    return render(request, 'languages.html')
def Contact(request):
    return render(request, 'contact.html')

def Services(request):
    return render(request, 'services.html')