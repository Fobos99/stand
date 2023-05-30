from django.shortcuts import render
from another_info.models import Bank, About_message, Dop_info, El_message

# Create your views here.


def about_message(request):
    context = {'segment': 'index'}
    queryset = About_message.objects.all() 
    context = {'object_list': queryset}  
    return render(request, 'another_info/about_message.html', context)

def el_message(request):
    context = {'segment': 'index'}
    queryset = El_message.objects.all() 
    context = {'object_list': queryset}  
    return render(request, 'another_info/el_message.html', context)

def dop_info(request):
    context = {'segment': 'index'}
    queryset = Dop_info.objects.all() 
    context = {'object_list': queryset}  
    return render(request, 'another_info/dop_info.html', context)

def bank(request):
    context = {'segment': 'index'}
    queryset = Bank.objects.all() 
    context = {'object_list': queryset}  
    return render(request, 'another_info/bank.html', context)

