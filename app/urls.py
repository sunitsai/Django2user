from django.urls import path,include
from . import views
urlpatterns = [

    path("",views.IndexPage,name="index"),
    path("login/",views.LoginPage,name="login"),
    path("home/",views.Hompage,name="homepage"),
    path("jsPage/",views.JSPage,name="jspage"),
    path("welcome/",views.WelcomePage,name="welcomepage"),
    path("register/",views.RegisterUser,name="register"),
    path("loginev/",views.LoginEvaluation,name="loginev"),
    path("logout/",views.Logout,name="logout"),

]
