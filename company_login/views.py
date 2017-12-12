from django.shortcuts import render

response = {}
def index(request):    
    # response['author'] = "Claudio Yosafat"
    html = 'company_login/company_login.html'
    return render(request, html, response)