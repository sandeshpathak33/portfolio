from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"name": 'Sandesh pathak'}
    return render(request, 'home.html',context)
    
def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')