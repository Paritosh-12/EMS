from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('insert/', views.insert),
    path('display/', views.display),
    path('update/', views.update),
    path('delete/', views.delete),
]
