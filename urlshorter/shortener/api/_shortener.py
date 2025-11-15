# Gelen URL'i al ve kıslatılmış URL oluştur

from django.http import HttpRequest
from .utils import create_unique_short_code

short_url = None

if (isinstance(HttpRequest, HttpRequest) and HttpRequest.method == 'POST'):
    original_url = HttpRequest.POST.get('original_url')
    short_code = create_unique_short_code(instance=None, Size=7)

    short_url = f"{HttpRequest.get_host()}/{short_code}"

    # Kısaltılmış Url'i veritabanına kayder
    from ..models import ShortURL

    new_short_url = ShortURL(original_url=original_url, short_code=short_code)
    new_short_url.save()