"""
URL configuration for travelingbears project.

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
from . import views


urlpatterns = [
    path('', views.redirect_to_login),  
    path('admin/', admin.site.urls),
    path('matchPage.html', views.api_matched_pairs, name='matchPage'),
    path('feedback.html', views.submit_feedback, name='feedback'),
    path('login.html', views.login_view, name='login'),
    path('signup.html', views.signup_view, name='signup'),
    path('homePage.html', views.login_view, name='homePage'),
]

