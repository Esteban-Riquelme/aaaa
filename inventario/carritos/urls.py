from django.urls import path

from carritos import views

urlpatterns =[
    path('', views.home),
    path('index/', views.index, name='index'),
    path('vista/', views.vista, name='vista'),
    path('Buscar/<codigo>', views.buscar, name='buscar'),
    path('historico/<codigo>', views.historico, name='historico'),
    path('login/', views.sigin, name='login'),
    path('notebook/', views.notebook, name='notebook'),
    path('contenido/', views.contenido, name='contenido'),
    path('index/login/', views.sigin, name='login'),
    path('index/logout', views.sigout, name='sigout'),

]