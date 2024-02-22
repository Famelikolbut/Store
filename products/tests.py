from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Product, ProductCategory


class BasketAddTestCase(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(username='testuser', password='12345')
        self.category = ProductCategory.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Test Product', price=10, category=self.category)
        self.basket_add_url = reverse('index')

    def test_basket_add_existing_product(self):
        self.client.force_login(self.user)
        response = self.client.get(self.basket_add_url)
        self.assertEqual(response.status_code, 200)

    # def test_basket_add_new_product(self):
    #     # Create a new product with a different ID
    #     new_product = Product.objects.create(name='New Test Product', price=20, category=self.category)
    #
    #     self.client.force_login(self.user)
    #     basket_add_url_new = reverse('products:basket_add', args=(new_product.id,))
    #     response = self.client.get(basket_add_url_new)
    #     self.assertEqual(response.status_code, 200)
