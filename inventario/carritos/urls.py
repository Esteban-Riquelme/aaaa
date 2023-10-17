from django.urls import path

from carritos import views

urlpatterns =[
    path('', views.home),
    path ('vista', views.vista),
    path('Buscar/<codigo>',views.buscar),
    path('historico/<codigo>',views.historico),
    path('login/', views.login),
    path('login/auteticate/',views.autenticate)
]