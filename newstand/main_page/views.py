from django.shortcuts import render
from main_page.models import Services
# Create your views here.

def home(request):
    context = {'segment': 'index'}
    queryset = Services.objects.all()
    context = { 'object_list': queryset}
    return render(request, 'main_page/home.html', context)

