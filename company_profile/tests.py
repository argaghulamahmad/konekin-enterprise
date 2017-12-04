from django.test import TestCase
from .models import *


class CompanyProfileAppTest(TestCase):
    def test_model_company_account(self):
        new_company_account = CompanyAccount.objects.create(company_name="Konekin Enterprise",
                                                            company_industries="Computer Software",
                                                            company_website="https://konekin-enterprise.herokuapp.com/",
                                                            company_headquarters="Kota Depok, Jawa Barat",
                                                            company_year_founded="2017",
                                                            company_type="Self-Employed",
                                                            company_size="2-10 employees",
                                                            company_specialties="Web App Development",
                                                            company_description="This linkedin company page created to accomplish our college group ('https://gitlab.com/KelompokB10PPW2017') assignment.",
                                                            )

        counting_all_company_account = CompanyAccount.objects.all().count()
        self.assertEqual(counting_all_company_account, 1)
