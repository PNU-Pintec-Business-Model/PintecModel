from django.urls import path
from . import views

urlpatterns = [
    path('price_predict/', views.landing),
    path('', views.setting_data),
    path('kakao/', views.kakao),
    path('db/', views.dbrequest),
    path('predict<company>0/', views.predict0),
    path('predict<company>1/', views.predict1)
]