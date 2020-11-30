import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from product_app.models import Product
from product_app.serializer import ProductSerializer


# initialize the APIClient app
client = Client()


class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Product.objects.create(
            name='Printer',
            description='This is printer')
        Product.objects.create(
            name='iPhone',
            description='This is iPhone')
        Product.objects.create(
            name='Toaster',
            description='This is toaster')

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('get_products'))
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(TestCase):
    """ Test module for GET single product API """
    def setUp(self):
        self.printer = Product.objects.create(
            name='Printer',
            description='This is printer')
        self.iphone = Product.objects.create(
            name='iPhone',
            description='This is iPhone')
        self.toaster = Product.objects.create(
            name='Toaster',
            description='This is toaster')

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('get_single_product', kwargs={'pk': self.toaster.uuid}))
        product = Product.objects.get(uuid=self.toaster.uuid)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('get_single_product', kwargs={'pk': 'wrong uuid'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """
    def setUp(self):
        self.valid_payload = {
            'name': 'Toaster',
            'description': 'This is toaster',
        }
        self.invalid_payload = {
            'name': '',  # should not be empty
            'description': 'This is a mistake',
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('create_product'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('create_product'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProductTest(TestCase):
    """ Test module for updating an existing product record """
    def setUp(self):
        self.iphone = Product.objects.create(
            name='iPhone',
            description='This is iPhone')
        self.toaster = Product.objects.create(
            name='Toaster',
            description='This is toaster')
        self.valid_payload = {
            'name': 'iPhone 12',
            'description': 'This is iPhone 12 !!!',
        }
        self.invalid_payload = {
            'name': '',  # should not be empty
            'description': 'This is a mistake',
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('update_product', kwargs={'pk': self.iphone.uuid}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('update_product', kwargs={'pk': self.toaster.uuid}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):
    """ Test module for deleting an existing product record """
    def setUp(self):
        self.iphone = Product.objects.create(
            name='iPhone',
            description='This is iPhone')
        self.toaster = Product.objects.create(
            name='Toaster',
            description='This is toaster')

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('delete_product', kwargs={'pk': self.iphone.uuid}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(
            reverse('delete_product', kwargs={'pk': 'wrong uuid'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class Update2TimesTest(TestCase):
    """ Test module for not updating product more then one time """
    def setUp(self):
        self.iphone = Product.objects.create(
            name='iPhone',
            description='This is iPhone')
        self.toaster = Product.objects.create(
            name='Toaster',
            description='This is toaster')
        self.first_payload = {
            'name': 'iPhone 12',
            'description': 'This is iPhone 12 !!!',
        }
        self.second_payload = {
            'name': 'iPhone 13',
            'description': 'This is iPhone 13 !!!',
        }

    def test_2_times_update(self):
        response = client.put(
            reverse('update_product', kwargs={'pk': self.iphone.uuid}),
            data=json.dumps(self.first_payload),
            content_type='application/json'
        )
        response = client.put(
            reverse('update_product', kwargs={'pk': self.iphone.uuid}),
            data=json.dumps(self.second_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
