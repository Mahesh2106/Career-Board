from django.urls import path
from CareerApp import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('career_chatbot/',views.career_chatbot,name="career_chatbot"),

    path('register_pg/',views.register_pg,name="register_pg"),
    path('register_save/',views.register_save,name="register_save"),

    path('Login_pg/',views.Login_pg,name="Login_pg"),
    path('Login_Fn/',views.Login_Fn,name="Login_Fn"),

    path('Logout_fn/',views.Logout_fn,name="Logout_fn"),
]