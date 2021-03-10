"""E4Sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import home_view
from signup.views import signup_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',include('sportnew.urls')),
    path('categories/',include('sportnew.urls_category')),
    path('',home_view),
    # authentications 
    path('signup/',signup_view, name='signup'),
    path('accounts/',include("django.contrib.auth.urls")),
    path('change_password', auth_view.PasswordChangeView.as_view(
        template_name = 'registration/password_change.html',
        success_url = '/'
    ), name='change_password' ),
    path('reset_password', auth_view.PasswordResetView.as_view(
    template_name = 'registration/password_reset.html',
    success_url = 'accounts/login'),
    name='reset_password' ),
] 
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)