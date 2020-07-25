from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('admin/', admin.site.urls),
    path('covid/', views.covid, name = 'covid'),
    path('login/', views.Login, name = 'login'),
    path('register/', views.Register, name = 'register'),
    path('patients/', views.Patients, name = 'patients'),
    path('logout/', views.Logout, name = 'logout')

]