"""osc URL Configuration

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
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from app.vender import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.vender.urls')),
    path('app/',include('app.product.urls')),  
    # path('app/',include('app.user.urls')),

    path('',TemplateView.as_view(template_name='index.html'),name='home'), 

    #templates
    path(
        'about/', 
        views.about, 
        name = "about"
    ),
    path(
        'contact/', 
        views.contact, 
        name = "contact"
    ),
    
    path(
        'index/', 
        views.index, 
        name = "index"
    ),
    path(
        'men/', 
        views.mens, 
        name = "mens"
    ),
    path(
        'single/<pid>/', 
        views.single, 
        name = "single"
    ),
    path(
        'womens/', 
        views.womens, 
        name = "womens"
    ),
   
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
