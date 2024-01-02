"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from books import views
app_name='books'
urlpatterns = [

    path('',views.home,name="home"),
    path('addbooks/',views.addbooks,name="addbooks"),
    path('viewbooks/',views.viewbooks,name="viewbooks"),
    path('factorial',views.factorial,name="factorial"),
    path('viewb<int:p>/',views.viewb,name="viewb"),
    path('deletebook<int:p>/',views.deletebook,name="deletebook"),
    path('editbook<int:p>/',views.editbook,name="editbook"),
]