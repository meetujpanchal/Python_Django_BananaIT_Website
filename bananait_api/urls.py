from django.urls import path  
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('data/',views.getData,name="get-data"),
    path('detail-data/<str:pk>/',views.detailview,name="detailed-data"),
    path('add/', views.addPerson,name="add-data"),
    path('update/<str:pk>/',views.updatePerson,name="update-data"),
    path('delete/<str:pk>/',views.deleteperson,name="delete-data"),
]