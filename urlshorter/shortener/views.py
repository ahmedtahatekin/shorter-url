from django.shortcuts import render, redirect
from .api._shortener import short_url

# Create your views here.

if (short_url == None):
    shortened_url = None
else:
    shortened_url = short_url

def index(request):
    return render(request, 'index.html', {
        'shortened_url': shortened_url,
    })

def redirect_short_url(request, short_code):

    from .models import ShortURL

    try:
        short_url_entry = ShortURL.objects.get(short_code=short_code)
        return redirect(short_url_entry.original_url)
    except ShortURL.DoesNotExist:
        return render(request, 'notExist.html', status=404)
    
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Eğer views.py içinde bu fonksiyon yoksa, ekleyin:
@require_POST
def short_url_api(request):
    # API mantığınız buraya gelir (POST verisini işleme)
    # Örn: original_url = request.POST.get('url')
    # ...
    return JsonResponse({'message': 'URL kısaltıldı.'})