from django.shortcuts import render
from .models import mylogs
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    logs = mylogs.objects.all()
    paginator = Paginator(logs, 10)
    if request.method == "GET":
        page = request.GET.get('page')
    page = 2
    page_obj = paginator.page(page)

    
    context = {
        "logs":page_obj
    }
    return render(request, 'home.html', context)

def getData(request):
    logs = mylogs.objects.all()
    return JsonResponse({"logs":list(logs.values())})

def search(request):
    q = request.GET.get('search')
    vector = SearchVector('id','name','massage','time', 'ip_address')
    query = SearchQuery(q, search_type="raw") 
    logs = mylogs.objects.annotate(search=vector).filter(search=query)
    return JsonResponse({"logs":list(logs.values())})
  
