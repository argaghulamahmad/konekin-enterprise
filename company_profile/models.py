from django.db import models

class CompanyAccount(models.Model):
    company_name = models.CharField(max_length=27)
    company_industries = models.CharField(max_length=100)
    company_website = models.URLField()
    company_headquarters = models.CharField(max_length=100)
    company_year_founded = models.CharField(max_length=4)
    company_type = models.CharField(max_length=50)
    company_size = models.CharField(max_length=100)
    company_specialties = models.CharField(max_length=100)
    company_description = models.TextField()
    company_logo = models.URLField()