from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_code>', views.redirect_short_url, name='redirect_short_url'),
    path('api/', views.short_url_api, name='short_url_api'),
]