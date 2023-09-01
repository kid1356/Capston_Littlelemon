from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('api/menu/',views.MenuView.as_view()),
    path('api/menu/<int:pk>',views.Single_Menu_View.as_view()),
   
]
