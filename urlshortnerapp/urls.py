from django.urls import path
from urlshortnerapp import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('shorten_url', views.shorten_url, name="shorten_url"),
    path('<str:short_code>/', views.redirect_url, name="redirect_url")

]