from django.shortcuts import render
from prezident_ukaz.models import Prez_ukaz
# Create your views here.


def home(request):
    context = {'segment': 'index'}
    queryset = Prez_ukaz.objects.all()
    context = {'object_list': queryset}
    return render(request, 'prezident_ukaz/home.html', context)
