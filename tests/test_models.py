from django.test import TestCase
from restaurant.models import Menu

class Menutest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title = "IceCream", Price = 80, Inventory = 100)
        item_from_db = Menu.objects.get(pk=item.pk)

        # Check individual attributes
        self.assertEqual(item_from_db.Title, "IceCream")
        self.assertEqual(item_from_db.Price, 80)
        self.assertEqual(item_from_db.Inventory, 100)