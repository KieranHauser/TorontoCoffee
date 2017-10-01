from django.test import TestCase
from .models import Shop

class ShopTestCase(TestCase):
    def setUp(self):
        Shop.objects.create(name='Starbucks', location='4 King St. W', description='Starbucks chain', slug='starbucks')
        Shop.objects.create(name='Second Cup', location='48 College St. ', description='Second Cup chain',
                            slug='second-cup')

    def testCreate(self):
        sb = Shop.objects.get(name='Starbucks')
        sc = Shop.objects.get(name='Second Cup')
        self.assertEqual(sb.get_absolute_url(), '/shop/starbucks/')
        self.assertEqual(sc.get_absolute_url(), '/shop/second-cup/')
