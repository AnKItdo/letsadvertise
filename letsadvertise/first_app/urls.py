from django.conf.urls import url
from first_app import views


urlpatterns = [

url('',views.index,name = 'index'),
url('first_app/login',views.login,name = 'login'),
url('register',views.register,name = 'register'),
url('sms',views.sms,name = 'sms'),
# url('mail',views.mail,name ='mail')
]
