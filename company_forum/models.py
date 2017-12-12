from django.db import models
from company_profile.models import CompanyAccount


# Create your models here.
class CompanyForum(models.Model):
    companyAccount = models.ForeignKey(CompanyAccount) #get the company you want here
    title = models.CharField(max_length=140)
    message = models.TextField()
    kode_message = models.CharField("Kode Message", max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    companyAccount = models.ForeignKey(CompanyAccount)
    companyForum = models.ForeignKey(CompanyForum)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
