"""performance URL Configuration

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
from admins import views as admins
from users import views as usr
from django.urls import path
from . import views as mainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', mainView.index, name='index'),
    path('', mainView.index, name='index'),
    path("UserRegister/", mainView.UserRegister,name="UserRegister"),
    path("AdminLogin/", mainView.AdminLogin, name = "AdminLogin"), 
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),

### User Side Views
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("Userdata/", usr.Userdata, name="Userdata"),
    path("prediction_form/", usr.prediction_form,name="prediction_form"),
    path("user_machine_learning/",usr.user_machine_learning, name="user_machine_learning"),
    path("rbf_kernel/",usr.rbf_kernel, name="rbf_kernel"),
    path("hybrid/",usr.hybrid, name="hybrid"),
    path("prediction_form/", usr.prediction_form, name="prediction_form"),



    ### Admin Side Views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewRegisteredUsers/", admins.ViewRegisteredUsers, name="ViewRegisteredUsers"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers")
    #path("AdminDataPreProcess/", admins.AdminDataPreProcess, name="AdminDataPreProcess"),
]



