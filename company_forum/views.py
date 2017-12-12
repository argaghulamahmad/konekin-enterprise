from django.shortcuts import render
from company_profile.models import CompanyAccount

# Create your views here.

response = {}


def company_forum(request, id):
    html = "company_forum/company_forum.html"
    #selected_company = CompanyAccount.objects.get(company_id=id)

    return render(request, html, response)
