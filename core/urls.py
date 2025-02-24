from django.contrib import admin
from django.urls import path
from whatsjob import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home-page')
]
