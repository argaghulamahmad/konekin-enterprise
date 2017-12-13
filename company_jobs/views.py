from django.shortcuts import render
from company_profile.models import CompanyAccount
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from company_forum.models import CompanyForum

# Create your views here.

response = {}
def index(request):
	company = CompanyAccount.objects.all()
	forum = CompanyForum.objects.all()

	print(company)

	paginator = Paginator(company, 1) # Show 1 contacts per page

	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages) 

	response['contacts'] = contacts
	response['company'] = company
	response['kerja'] = forum
	response['is_company_jobs_html'] = True

	return render(request, "company_jobs/company_jobs.html", response)


