from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name="about_view"),
    path('mode/dark/', views.dark_view, name="dark_view"),
    path('mode/light/', views.light_view, name="light_view")
]





