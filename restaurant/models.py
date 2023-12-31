from django.db import models

# Create your models here.
class Booking(models.Model): 
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    Booking_Date =  models.DateTimeField()

    def __str__(self):
      return f'{self.Name} : {str(self.Booking_Date)}'

class Menu(models.Model):
    Title = models.CharField(max_length=200)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    description =models.TextField(max_length=1000, default='')
    Inventory = models.IntegerField()

    def __str__(self):
      return f'{self.Title} : {str(self.Price)}'