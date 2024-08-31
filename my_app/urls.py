from django.contrib.auth.views import LogoutView
from django.urls import path

from sporify.views import UserLoginView, RegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout' ),
    path('register/', RegisterView.as_view(), name='register' ),
]