from django.shortcuts import render

from .models import CompanyAccount

response = {}


def company_detail(request, id):
    html = "layout/company_profile.html"

    selected_company = CompanyAccount.objects.get(company_id=id)

    response['sub_title'] = selected_company.company_name + ' Profil Page'
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
    response['url_company_forum'] = '/company/forum/' + id + '/'
    response['url_company_jobs'] = '/company/jobs/'
    response['is_company_profile_html'] = True
    response['is_logged_in'] = True

    return render(request, html, response)


def create_company_account(id, name, industries, website, headquarters,
                           year_founded, type, size, specialties, description, logo_url):
    count = CompanyAccount.objects.filter(company_id=id).count()
    if (count == 0):
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
        print("Account with " + id + ' created.')
    elif (count != 0):
        existAccount = CompanyAccount.objects.get(company_id=id)
        if (industries != existAccount.company_industries):
            existAccount.company_industries = industries
        if (website != existAccount.company_website):
            existAccount.company_website = website
        if (headquarters != existAccount.company_headquarters):
            existAccount.company_headquarters = headquarters
        if (year_founded != existAccount.company_year_founded):
            existAccount.company_year_founded = year_founded
        if (type != existAccount.company_type):
            existAccount.company_type = type
        if (size != existAccount.company_size):
            existAccount.company_size = size
        if (specialties != existAccount.company_specialties):
            existAccount.company_specialties = specialties
        if (description != existAccount.company_description):
            existAccount.company_description = description
        if (logo_url != existAccount.company_logo):
            existAccount.company_logo = logo_url
        existAccount.save()
        print("Account with " + id + ' has been updated.')