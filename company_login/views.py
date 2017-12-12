from django.shortcuts import render
from company_profile.views import create_company_account

response = {}
def index(request):    
    # response['author'] = "Claudio Yosafat"
    html = 'company_login/company_login.html'
    return render(request, html, response)