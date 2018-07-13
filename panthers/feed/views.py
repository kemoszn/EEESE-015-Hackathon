from django.shortcuts import render, get_object_or_404
from .models import *


def news_list(request):
    glo_news = New.objects.filter(description='Global')
    elec_news = New.objects.filter(description='Electrical')
    chem_news = New.objects.filter(description='Chemical')
    civil_news = New.objects.filter(description='Civil')
    
    context = {
        'glo_news': glo_news,
        'elec_news': elec_news,
        'chem_news': chem_news,
        'civil_news':civil_news,        
    }
    
    return render(request, 'news.html', context)

def news_detail(request, year, month, day, news):
    news = get_object_or_404(New, slug=post, publish__year=year, publish__month=month, publish__day= day)
    
    return render(request, 'news_detail.html', {'news': news})
    
def events_list(request):
    elec_news = New.objects.filter(description='Electrical')
    chem_news = New.objects.filter(description='Chemical')
    civil_news = New.objects.filter(description='Civil')
    context = {
        'elec_news': elec_news,
        'chem_news': chem_news,
        'civil_news':civil_news,       
    }
    return render(request,'events.html',context)
    