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


def create_company_account(id, name, industries, website, headquarters,
                           year_founded, type, size, specialties, description, logo_url):
    CompanyAccount.objects.create(
        company_id=id,
        company_name=name,
        company_industries=industries,
        company_website=website,
        company_headquarters=headquarters,
        company_year_founded=year_founded,
        company_type=type,
        company_size=size,
        company_specialties=specialties,
        company_description=description,
        company_logo=logo_url,
    )
