"""letsadvertise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from first_app import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from first_app import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('first_app/',include('first_app.urls')),
    path('login/',auth_views.LoginView.as_view(template_name = 'register/login.html' ),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'register/logout.html'),name = 'logout'),
    path('register/',views.register,name = 'register'),
    path('profile/',views.profile,name = 'profile'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
    path('mail/',views.mail,name ='mail'),
    path('gmail/',views.mail,name ='gmail'),
    path('sms/',views.sms,name = 'sms'),
    path('whatsapp/',views.whatsapp,name = 'whatsapp'),

]



if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)








#
# SOCIAL_AUTH_FACEBOOK_KEY = '601383703703964'  # App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = 'da2f444b7db979a65b605fe977d89189'  # App Secret
