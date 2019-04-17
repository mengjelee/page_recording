"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from helloworld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    #path('home/', views.home, name='home'),
    #path('c/', views.createEvent, name='createEvent'),
    # re_path('user/[-\w]+/$', views.newEvent),  #
    # re_path('user/[-\w]+/result', views.resultpage, name='resulturl'),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout, name='logout'),
    path('A/', views.A_page),
    path('B/', views.B_page),
    path('C/', views.C_page),
    # path('D/', views.D_page),
    # path('E/', views.E_page),
    # path('F/', views.F_page),
    # path('G/', views.G_page),
    # path('H/', views.H_page),
    # path('I/', views.I_page),
    # path('J/', views.J_page),
]
