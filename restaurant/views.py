from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import  generics,viewsets,permissions
from .serializers import MenuSerializers,UserSerializers,BookingSerializers
from .models import Menu,Booking
# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class UserView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
    

    

class MenuView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class Single_Menu_View(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers 
    
