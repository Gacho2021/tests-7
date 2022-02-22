from django.test import TestCase
from django.config.models import user
from .models import TechType, product, Review
import datetime

# Create your tests here.
class TechTypeTest(TestCase):
    def setup(self):
        self.type=TechType(typename='Lenovo Laptop')

        def test_typestring(self):
            self.assertEqual(str(self.type), 'Lenovo Laptop')

            def test_tablename(self):
                self.assertEqual(str(TechType._meta.db_table), 'techtype')

class productTest(TestCase):
    def setup(self):
        self.type=TechType(typename='Laptop')
        self.user=user(username='user1')
        self.product= product(productname='Lenovo',producttype=self.type, user=self.user, dateentered=date('2/10/2021'),price=1200.99,producturl='http://www.lenovo.com',description="lenovo Laptop")

    def test_string(self):
           self.assertEqual(str(product), 'Lenovo')

    def test_discount(self):
        disc = self.product.price * .05
        self.assertEqual(self.product.discountAmount(), disc)

    def test_discountAmount(self):
        disc=self.product.price * (1 -.05)
        self.assertEqual(self.product.discountPrice(),disc)
