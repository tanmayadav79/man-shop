from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Sign_up, name='signup'),
    path('signin/', views.Sign_in, name='signin'),  # changed from 'login'
    path('logout/', views.Logout, name='logout'),
]
