from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

# Create your tests here.
# Create your tests here.
class Lab5UnitTest(TestCase):
	def test_url_is_exist(self):	
		response = Client().get('/company/jobs/')
		self.assertEqual(response.status_code, 200)

	def test_using_index_func(self):
		found = resolve('/company/jobs/')
		self.assertEqual(found.func, index)

	def test_page_not_integer(self):
		response = Client().get('/lab-7/?page=ancol')
		self.assertNotEqual(response.status_code,200)