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
        data={"companyType": {"code": "E","name": "Self Employed"},"description": "This linkedin company page created to accomplish our college group (Kelompok B 10 PPW 2017) assignment.","employeeCountRange": {"code": "B","name": "2-10"},"foundedYear": 2017,"id": 13597930,"industries": {"_total": 1,"values": [{"code": "4","name": "Computer Software" }]},"locations": {"_total": 2,"values": [{"address": {"city": "Kota Depok","postalCode": "16424","street1": "Kampus UI Depok"}},{"address": {"city": "Jakarta Selatan","postalCode": "12950","street1": "Jalan Dr. Ide Anak Agung Kav. E3.2 No. 1, Kuningan RT.5/RW.2, Setiabudi, Kuningan Timur, RT.5/RW.2, Kuningan Tim."}}]},"logoUrl": "https://media.licdn.com/mpr/mpr/AAIAAwDGAAoAAQAAAAAAAA7YAAAAJGQ5OGMxZWE0LTUwNDktNGRkMC1hMGI0LTg3MjlmMjZhNDE0NQ.png","name": "Konekin Enterprise","specialties": {"_total": 2,"values": ["Web App Development","Mobile App Development"]},"squareLogoUrl": "https://media.licdn.com/mpr/mpr/AAIAAwDGAAoAAQAAAAAAAAwwAAAAJDQ3ZDE5ZDcwLTk2MDItNDI3Zi1iOTVmLTk3NjM1MThkNDNlZQ.png","websiteUrl": "https://konekin-enterprise.herokuapp.com/"}
        response_post = Client().post('/company/login',data)
        self.assertEqual(response_post.status_code,200)


        