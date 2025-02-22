from django.urls import path

from .views import signup, signin, signout, profile

app_name = 'auth'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('profile/', profile, name='profile'),
]
