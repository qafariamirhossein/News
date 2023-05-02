from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def contact_view(request):
    return render(request, 'contact.html')

def category_view(request):
    return render (request, 'category.html')