from django.shortcuts import render
from company_profile.models import CompanyAccount

# Create your views here.

response = {}
def company_jobs(request, id):
    selected_company = CompanyAccount.objects.get(company_id=id)

    response['company_logo'] = selected_company.company_logo
    response['is_company_jobs_html'] = True