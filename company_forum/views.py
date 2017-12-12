from django.shortcuts import render
from company_profile.models import CompanyAccount
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

response = {}

def company_forum(request, id):
    print(id)

    count = CompanyAccount.objects.count()
    print(count)
    selected_company = CompanyAccount.objects.get(company_id=id)
    print(selected_company.company_id)

    forum = CompanyForum.objects.filter(companyAccount=selected_company)
    print(forum.count())

    response['sub_title'] = selected_company.company_name + ' Forum'
    response['id'] = id
    response['logo'] = selected_company.company_logo
    response['company'] = selected_company

    response['forum']: forum
    response['company_form'] = Forum_Form
    response['forum_list'] = forum

    forum_list = forum
    paginator = Paginator(forum_list, 5)
    page = request.GET.get('page', 1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    response['forum_list'] = users
    response['is_logged_in'] = True
    html = "company_forum/company_forum.html"
    return render(request, html, response)

def add_forum(request, id):

    form = Forum_Form(request.POST or None)

    if (request.method == 'POST' and form.is_valid()):
        selected_company = CompanyAccount.objects.get(company_id=id)
        print(selected_company)

        response['CompanyAccount'] = selected_company
        response['title'] = request.POST['title']
        response['message'] = request.POST['post']

        forumpost = CompanyForum(companyAccount=response['CompanyAccount'],title=response['title'], message=response['message']) #model
        forumpost.save()

        # html = "company_forum/add_post.html"
        # return render(request,html,response)
        return HttpResponseRedirect('/company/forum/' + id + '/')


def paginate_page(page, data_list):
    paginator = Paginator(data_list, 5)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    # Get the index of the current page
    index = data.number - 1
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 10, so lets calculate where to slice the list
    start_index = index if index >= 5 else 0
    end_index = 5 if index < max_index - 5 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]
    paginate_data = {'data':data, 'page_range':page_range}
    return paginate_data