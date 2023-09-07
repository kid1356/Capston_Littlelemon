from django.test import TestCase
from restaurant import models
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

class MenuviewTest(TestCase):
    def setUp(self):
        models.Menu.objects.create(Title = "noodles" , Price =30.01, Inventory = 39)
        models.Menu.objects.create(Title = "chicken tikka" , Price =40.21, Inventory = 10)
        models.Menu.objects.create(Title = "soup" , Price =20.00, Inventory = 9)

    def test_getall(self):
        client = APIClient()

        url = reverse('menu_view')
        response = client.get(url)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

        serialized_data = response.data
        serialized_data_without_id = [{'Title': item['Title'], 'Price': item['Price'], 'Inventory': item['Inventory']} for item in serialized_data]

        

        expected_data  =[
            {'Title':'noodles','Price':'30.01','Inventory':39},
            {'Title':'chicken tikka','Price':'40.21','Inventory':10},
            {'Title':'soup','Price':'20.00','Inventory':9},
                        
        ]

        self.assertEqual(serialized_data_without_id,expected_data)
