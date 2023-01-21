from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('kakao/', views.kakao),
    path('db/', views.dbrequest)
    path('',)
]