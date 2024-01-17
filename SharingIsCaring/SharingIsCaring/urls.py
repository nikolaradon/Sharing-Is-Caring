"""
URL configuration for SharingIsCaring project.

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
from django.contrib import admin
from django.urls import path
from SharingIsCaringApp.views import (LandingPageView, AddDonationView, LoginView, RegisterView,
                                      StepsView, AboutUsView, HelpView, FormConfirmationView
                                      )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='index'),
    path('add_donation/', AddDonationView.as_view(), name='form'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('steps/', StepsView.as_view(), name='steps'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('help/', HelpView.as_view(), name='help'),
    path('confirmation', FormConfirmationView.as_view(), name='help'),
]
