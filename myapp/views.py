from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

# Create your views here.

# create function


def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')

        # page = requests.get('https://www.google.com') own 2
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

#    link_address = []  own 1

#     for link in soup.find_all('a'):
#         link_address.append(link.get('href'))

# save result in database
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        # take data from database
        data = Link.objects.all()

    # return render(request, 'myapp/result.html', {'link_address': link_address}) own 1
    return render(request, 'myapp/result.html', {'data': data})


def clear(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result.html')
