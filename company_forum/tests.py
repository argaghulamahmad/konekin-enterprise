from django.test import TestCase
from django.urls import reverse
from company_forum.views import *

from company_profile.models import *
from company_forum.models import *


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

        self.forum = CompanyForum.objects.create(
            companyAccount=self.company,
            title = "Test",
            message = "1. Web Dev"
        )
        #
        # for x in range(2, 10):
        #     a = CompanyForum(companyAccount=self.company, title='Jobs',
        #                 message='Test')
        #     a.save()


    def test_model_company_account(self):
        counting_all_forum_account = CompanyForum.objects.all().count()
        self.assertEqual(self.forum.__str__(), "Konekin Enterprise")
        self.assertEqual(counting_all_forum_account, 1)

    def test_company_detail(self):
        response = self.client.post(reverse('company-forum:company-forum', kwargs={'id': '13597930'}))
        html_response = response.content.decode('utf8')
        self.assertIn("Konekin Enterprise", html_response)
        self.assertEqual(response.status_code, 200)

    # def test_create_company_account_function(self):
    #     create_company_account("13597920", "", "", "", "", "", "", "", "", "", "")
    #     existAccount1 = CompanyAccount.objects.get(company_id="13597920")
    #     self.assertEqual(existAccount1.company_name, "")
    #
    #     create_company_account("13597920", "", "industries", "website", "headquarters", "2018", "type", "size",
    #                            "specialties", "description", "logo")
    #     existAccount2 = CompanyAccount.objects.get(company_id="13597920")
    #     self.assertEqual(existAccount2.company_industries, "industries")
    #     self.assertEqual(existAccount2.company_website, "website")
    #     self.assertEqual(existAccount2.company_headquarters, "headquarters")
    #     self.assertEqual(existAccount2.company_year_founded, "2018")
    #     self.assertEqual(existAccount2.company_type, "type")
    #     self.assertEqual(existAccount2.company_size, "size")
    #     self.assertEqual(existAccount2.company_specialties, "specialties")
    #     self.assertEqual(existAccount2.company_description, "description")
    #     self.assertEqual(existAccount2.company_logo, "logo")

    def test_paginator(self):
        paginator = Paginator(CompanyForum.objects.all(), 5)
        self.assertEqual(1, paginator.count)
        self.assertEqual(1, paginator.num_pages)
        self.assertEqual([1], list(paginator.page_range))

    def test_empty_page(self):
        paginator = Paginator(CompanyForum.objects.all(), 5)
        self.assertRaises(EmptyPage, paginator.page, 0)
        self.assertRaises(EmptyPage, paginator.page, 2)

        # Empty paginators with allow_empty_first_page=True.
        paginator = Paginator(CompanyForum.objects.filter(title="Test2"), 5,
                              allow_empty_first_page=True)
        self.assertEqual(0, paginator.count)
        self.assertEqual(1, paginator.num_pages)
        self.assertEqual([1], list(paginator.page_range))

        # Empty paginators with allow_empty_first_page=False.
        paginator = Paginator(CompanyForum.objects.filter(title="Test2"), 5,
                              allow_empty_first_page=False)
        self.assertEqual(0, paginator.count)
        self.assertEqual(0, paginator.num_pages)
        self.assertEqual([], list(paginator.page_range))

    def test_invalid_page(self):
        paginator = Paginator(CompanyForum.objects.all(), 5)
        self.assertRaises(PageNotAnInteger, paginator.page, 'a')
