from django.shortcuts import render
from django.http import HttpResponse
from .search import search



# Create your views here.


def home(request):
    search_temp = search("Genesis Photography")
    return render(request, 'index_test.html', {'search': search_temp})



def my_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        company_values = search(q)
        companies = company_values.values()
        company_name = company_values['COMPANY_NAME']
        email_address = company_values['EMAIL_ADDRESS']
        state = company_values['STATE']
        phone_number = company_values['PHONE_NUMBER']


        return render(request, 'search_results.html',
                      {'company': companies,
                       'query': q,
                       'company_name': company_name,
                       'email_address': email_address,
                       'state': state,
                       'phone_number': phone_number})
    else:
        return HttpResponse('Please submit a search term.')


def welcome(request):
    return HttpResponse("Hello My Lovely User!!!")


