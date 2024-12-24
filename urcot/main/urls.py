"""
URL configuration for urcot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

"""
     
EVERYTHING FOR LABOR SAFETY (ВCЁ ДЛЯ ОХРАНЫ ТРУДА) = efls
ABOUT THE ORGANIZATION (Об организации) = about_organization
TO THE MANAGER (Руководителю) = manager 
LITERATURE (ЛИТЕРАТУРА) = literature
SERVICES (УСЛУГИ) = services
ABOUT US (О нас) = about_us
PERSONAL ACCOUNT (Личный кабинет) = personal_account

"""

urlpatterns = [
    path('', views.index, name='home'),
    # path('efls', views.efls),
    # path('about_organization', views.about_organization),
    path('manager', views.manager, name='manager'),
    path('literature', views.literature, name='literature'),
    path('services', views.services, name='services'),
    path('about_us', views.about_us, name='about_us'),
    path('personal_account', views.personal_account, name='personal_account'),
]
