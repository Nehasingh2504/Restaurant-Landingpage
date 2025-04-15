"""
URL configuration for landingpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('book_alert/',book_alert),
    path('book/',book),
    path('login/',login),
    path('signup/',signup),
    path('home_after/',home_after),
    path('insert_booking/',insert_booking),
    path('signup_detail/',signup_detail),
    path('login_detail/',login_detail),
]
