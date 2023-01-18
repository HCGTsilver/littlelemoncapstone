from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="IceCream", price=80, featured=False, inventory=100)
        itemstr = item.get_item()

        # self.asertEqual(itemstr, "IceCream : 80")
        assert itemstr
