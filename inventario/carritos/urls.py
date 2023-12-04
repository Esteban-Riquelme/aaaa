from django.urls import path

from carritos import views

urlpatterns =[
    path('home', views.home, name='home'),
    path('carros', views.carros, name='carros'),
    path('Buscar/<codigo>', views.buscar, name='buscar'),
    path('historico/<codigo>', views.historico, name='historico'),
    path('', views.sigin, name='login'),
    path('notebook', views.notebook, name='notebook'),
    path('contenido/<codigo>', views.contenido, name='contenido'),
    path('login', views.sigin, name='login'),
    path('historico/logout', views.sigout, name='sigout'),
    path('contenido/logout', views.sigout, name='sigout'),
    path('logout', views.sigout, name='sigout'),
    path('proyector',views.proyector, name='proyector'),
    path('pc',views.pc, name='pc'),

]