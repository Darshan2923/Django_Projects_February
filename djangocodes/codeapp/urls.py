from django.urls import path
from . import views

urlpatterns = [
    # blogs
    path('',views.index,name='index'),
    path('add_blogs/',views.add_blogs,name='add_blogs'),
    path('delete_blogs/<str:slug>/',views.delete_blogs,name='delete_blogs'),

# User authentication
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_user,name='logout_user'),
    path('register/',views.register_page,name='register_page'),
]
