from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from company_profile.views import create_company_account
from django.views.decorators.csrf import csrf_exempt
import json


response = {}
def index(request):#pragma: no cover
    # response['author'] = "Claudio Yosafat"
    html = 'company_login/company_login.html'
    #html login
    response['is_logged_in'] = False
    response['is_company_login_html'] = True
    return render(request,html,response)


@csrf_exempt
def addCompanyData(request):#pragma: no cover
    print("masuk company data")
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['data[id]']
        print(request.POST['data[name]'])
        company_id = id
        company_name = request.POST['data[name]']
        company_industries = request.POST['data[industries][values][0][name]']
        company_website=request.POST['data[websiteUrl]']
        company_headquarters=request.POST['data[locations][values][0][address][city]']
        company_year_founded=request.POST['data[foundedYear]']
        company_type=request.POST['data[companyType][name]']
        company_size=request.POST['data[employeeCountRange][name]'] + " employees"
        company_specialties=request.POST['data[specialties][values][]']
        company_description=request.POST['data[description]']
        company_logo=request.POST['data[squareLogoUrl]']
        listResponse = {'id' : id}
        create_company_account(company_id,company_name,company_industries,company_website,company_headquarters,company_year_founded,company_type,company_size,company_specialties,company_description,company_logo)
        return JsonResponse(listResponse)
    return HttpResponse()


