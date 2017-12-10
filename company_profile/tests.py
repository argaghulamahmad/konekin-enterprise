from django.test import TestCase
from django.urls import reverse
from company_profile.views import *

from .models import *


class CompanyProfileAppTest(TestCase):
    def setUp(self):
         self.company = CompanyAccount.objects.create(
            company_id="13597930",
            company_name="Konekin Enterprise",
            company_industries="Computer Software",
            company_website="https://konekin-enterprise.herokuapp.com/",
            company_headquarters="Kota Depok, Jawa Barat",
            company_year_founded="2017",
            company_type="Self-Employed",
            company_size="2-10 employees",
            company_specialties="Web App Development",
            company_description="This linkedin company page created to accomplish our college group ('https://gitlab.com/KelompokB10PPW2017') assignment.",
            company_logo="https://media.licdn.com/mpr/mpr/shrink_200_200/AAIAAwDGAAoAAQAAAAAAAArvAAAAJDM1OGUyZGRiLTcxMWUtNGQzZC1hNWY3LWJjZDlhM2ZhNzA3Ng.png",
        )

    def test_model_company_account(self):
        counting_all_company_account = CompanyAccount.objects.all().count()
        self.assertEqual(self.company.__str__(), "Konekin Enterprise")
        self.assertEqual(counting_all_company_account, 1)

    def test_company_detail(self):
        response = self.client.post(reverse('company-profile:company-detail', kwargs={'id': '13597930'}))
        html_response = response.content.decode('utf8')
        self.assertIn("Konekin Enterprise", html_response)
        self.assertEqual(response.status_code, 200)

    def test_create_company_account_function(self):
        counting_all_company_account = CompanyAccount.objects.all().count()
        create_company_account("13597930", "", "", "", "", "", "", "", "", "", "")
        self.assertEqual(counting_all_company_account, 1)

        counting_all_company_account = CompanyAccount.objects.all().count()
        create_company_account("12912120", "", "", "", "", "", "", "", "", "", "")
        self.assertEqual(counting_all_company_account, 2)
