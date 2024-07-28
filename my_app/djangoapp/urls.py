from django.urls import path
from . import views

urlpatterns = [
    path('readall/', views.getalerts),
    path('create/', views.addalert),
    path('read/<str:pk>', views.getalert),
    path('update/<str:pk>', views.updatealert),
    path('delete/<str:pk>', views.deletealert),
]