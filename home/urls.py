from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("add-card-data",views.add_card_data,name="add_card_data"),
]
