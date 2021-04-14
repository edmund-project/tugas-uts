from django.contrib import admin
from django.urls import path
from main.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('prevention/', prevention, name='prevention'),
    path('symptoms/', symptoms, name='symptoms'),
    path('treatments/', treatments, name='treatments')
]
