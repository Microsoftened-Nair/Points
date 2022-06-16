from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addm', views.addm, name='addm'),
    path('addr', views.addr, name='addr'),
]
