from django.contrib import admin
from django.urls import path
from homeapi import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include('homeapi.url'))
    path('students', views.homeapi,name='home')

]
