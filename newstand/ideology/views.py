
from django.shortcuts import render
from django.core.paginator import Paginator
from ideology.models import Deskbest, Bestworker, Grafik, News, Edi, Govment, BRSM, BRSM_contacts, Organizations
# Create your views here.

def home(request):
    context = {'segment': 'index'}
    return render(request, 'ideology/home.html', context)

def bestworker(request):
    context = {'segment': 'index'}
    queryset = Bestworker.objects.all()
    context = {'object_list': queryset} 
    return render(request, 'ideology/bestworker/bestworker.html', context)

def deskbest(request):
    context = {'segment': 'index'}
    queryset = Deskbest.objects.all()
    context = {'object_list': queryset} 
    return render(request, 'ideology/deskbest/deskbest.html', context)

def govment(request):
    context = {'segment': 'index'}
    queryset = Govment.objects.all()
    context = {'object_list': queryset} 
    return render(request, 'ideology/govment/govment.html', context)

def grafik(request):
    context = {'segment': 'index'}
    queryset = Grafik.objects.all() 
    context = {'object_list': queryset}   
    return render(request, 'ideology/grafik/grafik.html', context)

def news(request):
    queryset = News.objects.all()    
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    
    context = {'object_list': page_obj,
               'list_post': queryset} 
    def get_queryset (self):
        return News.objects.filter( publish=True) 
    return render(request, 'ideology/news/news.html', context)


def edi(request):
    queryset = Edi.objects.all()
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'object_list': page_obj,
               'list_post': queryset}
    def get_queryset(self):
        return Edi.objects.filter(publish=True)
    return render(request, 'ideology/edi/edi.html', context)

def organizations(request):   
    queryset = Organizations.objects.all()
    context = {'object_list': queryset} 
    return render(request, 'ideology/organizations/organizations.html', context)

def brsm(request):    
    context = {'segment': 'index'} 
    queryset = BRSM.objects.all()
    querysets = BRSM_contacts.objects.all()
    context = {'object_list': queryset,
               'object_lists': querysets}  
    return render(request, 'ideology/organizations/brsm.html', context)


