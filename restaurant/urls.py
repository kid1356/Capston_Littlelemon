from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.index, name="index"),
    path('api/menu/',views.MenuView.as_view(), name= "menu_view" ),
    path('api/menu/<int:pk>',views.Single_Menu_View.as_view()),
    path('api-auth-token/',obtain_auth_token),
   
]
