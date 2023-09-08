from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name ='about'),
    path('menu/',views.menu , name= 'menu'),
    path('menu/<int:pk>',views.display_menu_item,name='menu_item'),
    path('book/',views.book, name='book'),
    path('api/menu/',views.MenuView.as_view(), name= "menu_view" ),
    path('api/menu/<int:pk>',views.Single_Menu_View.as_view()),
    path('api-auth-token/',obtain_auth_token),
    # path('booking/',views.BookingcreateView.as_view()),
]
