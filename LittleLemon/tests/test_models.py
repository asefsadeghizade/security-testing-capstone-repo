from django.test import TestCase
from LittleLemonAPI.models import MenuItem, Booking
from decimal import Decimal
from datetime import datetime


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream",
                                       price=80,
                                       inventory=100)
        itemstr = item.get_item()
        
        self.assertEqual(itemstr, "IceCream: 80")
        
        
class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            bookingDate=datetime(2023, 6, 24, 18, 0)
        )
        expected_str = "John Doe for 4 guests on 2023-06-24 18:00:00"
        self.assertEqual(str(booking), expected_str)