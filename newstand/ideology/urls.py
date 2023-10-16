from django.urls import path
from .views import *
from django.views.generic import ListView,DetailView

urlpatterns = [
    path('', home, name='home'),
    path('ideology/bestworker/', bestworker, name='bestworker'),
    path('ideology/deskbest/', deskbest, name='deskbest'),
    path('ideology/edi/', edi, name='edi'),
    path(r'ideology/edi/<int:pk>', 
         DetailView.as_view(model=Edi, 
                            template_name="ideology/edi/edi-detail.html") ),
    path('ideology/govment/', govment, name='govment'),
    path('ideology/grafik/grafik', grafik, name='grafik' ),
    path(r'ideology/grafik/<int:pk>', 
         DetailView.as_view(model=Grafik, 
                            template_name="ideology/grafik/grafik-detail.html") ),
    path('ideology/news/', news, name='news'),
    path(r'ideology/news/<int:pk>', 
         DetailView.as_view(model=News, 
                            template_name="ideology/news/news-detail.html")),
    path('ideology/organizations/', organizations, name='organizations'), 
    path('ideology/organizations/<int:pk>', 
         DetailView.as_view(model=Organizations, 
                            template_name="ideology/organizations/organizations-detail.html")),  
    path('ideology/organizations/brsm', brsm, name='brsm'),   
  
    ]