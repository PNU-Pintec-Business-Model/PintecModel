from django.urls import path
from . import views

urlpatterns = [
    path('price_predict/', views.landing),
    path('', views.setting_data),
    path('kakao/', views.kakao),
    path('db/', views.dbrequest)
]