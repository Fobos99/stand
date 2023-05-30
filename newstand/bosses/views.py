from django.shortcuts import render

from bosses.models import Director, Filials, First_Zam, Zam

# Create your views here.


def home(request):    
    context = {'segment': 'index'}
    dir = Director.objects.all()
    fzam = First_Zam.objects.all()
    zam = Zam.objects.all()
    filials = Filials.objects.all()
    context = {'object_list': dir,
               'fzam_list': fzam,
               'zam_list' : zam,
               'filials_list' : filials
               } 
    return render(request, 'bosses/home.html', context)

