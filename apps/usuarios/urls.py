from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_logout, name = ''),
    path('signin', views.page_signin, name = 'signin'),
    path('signup', views.page_signup, name = 'signup'),
    path('user_profile', views.page_user_profile, name = 'user_profile'),
    path('logout', views.user_logout, name = 'logout')
]