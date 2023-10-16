from django.shortcuts import render
from about_rup.models import About_rup, Functions, Map, Terretory
# Create your views here.
def home(request):
    context = {'segment': 'index'}
    queryset = Functions.objects.all()
    queryset2 = About_rup.objects.all()
    queryset3 = Map.objects.all()
    queryset4 = Terretory.objects.all()
    context = {'object_list': queryset,
               'object_list2': queryset2,
               'object_list3': queryset3,
               'object_list4': queryset4} 
    return render(request, 'about_rup/home.html', context)
