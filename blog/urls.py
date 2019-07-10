from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('list/', views.users),
    path('list/delete/<int:id>/', views.delete)
]