from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginIndex', views.loginIndex, name='loginIndex'),
    path('logout', views.logout_view, name='logout'),
]