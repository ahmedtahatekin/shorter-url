from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def redirect_short_url(request, short_code):
    # Logic to redirect to the original URL based on the short_code
    pass