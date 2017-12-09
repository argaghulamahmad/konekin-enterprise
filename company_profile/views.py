from django.shortcuts import render
from .models import CompanyAccount

response = {}

def company_detail(request, id):
    html = "layout/company_profile.html"

    selected_company = CompanyAccount.objects.get(company_id=id)

    response['company_name'] = selected_company.company_name
    response['company_industries'] = selected_company.company_industries
    response['company_website'] = selected_company.company_website
    response['company_headquarters'] = selected_company.company_headquarters
    response['company_year_founded'] = selected_company.company_year_founded
    response['company_type'] = selected_company.company_type
    response['company_size'] = selected_company.company_size
    response['company_specialties'] = selected_company.company_specialties
    response['company_description'] = selected_company.company_description
    response['company_logo'] = selected_company.company_logo
    response['is_company_profile_html'] = True

    return render(request, html, response)