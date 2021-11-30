from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_view, name='create_view'),
    path('<str:pk>',views.go_view, name='go_view' ),
]