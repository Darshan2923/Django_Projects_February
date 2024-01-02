from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),


# User authentication
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_user,name='logout_user'),
    path('register/',views.register_page,name='register_page'),
]
