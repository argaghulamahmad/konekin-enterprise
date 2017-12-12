from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.urls import reverse
from company_login.views import *

class Company_Login(TestCase):
    def test_company_login_url_is_exist(self):
        response = Client().get('/company/login/')
        self.assertEqual(response.status_code,200)

    def test_root_url_now_is_using_index_page_from_company_login(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 301)
        self.assertRedirects(response,'/company/login/',301,200)

    def test_company_login_using_index_func(self):
        found = resolve('/company/login/')
        self.assertEqual(found.func, index)

    def test_add_company_data(self):
        name =''
        id =''
        data={'name' : name,'id' : id}
        response_post = Client().post('/comapany/login')