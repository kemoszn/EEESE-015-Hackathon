from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import EventForm
from django.http import HttpResponse

def news_list(request):
    glo_news = New.objects.filter(description='Global')
    elec_news = New.objects.filter(description='Electrical')
    chem_news = New.objects.filter(description='Chemical')
    civil_news = New.objects.filter(description='Civil')
    
    context = {
        'glo': glo_news,
        'elec_news': elec_news,
        'chem_news': chem_news,
        'civil_news':civil_news,        
    }
    
    return render(request, 'news.html', context)

def news_detail(request, year, month, day, news):
    news = get_object_or_404(New, slug=news, publish__year=year, publish__month=month, publish__day= day)
    
    return render(request, 'news_detail.html', {'g': news})
    
def events_list(request):
    elec_events = Event.objects.filter(department='Electrical')
    chem_events = Event.objects.filter(department='Chemical')
    civil_events = Event.objects.filter(department='Civil')
    context = {
        'elec_events': elec_events,
        'chem_events': chem_events,
        'civil_events':civil_events,       
    }
    return render(request,'events.html',{'a':elec_events ,'b': civil_events},)
    



def AddEvent(request):
    if request.method == 'POST':
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            new_event = event_form.save(commit=False)
            new_event.save()
            return render(request, 'thank_you.html') 
    else:
        event_form = EventForm()

        return render(request, 'new_event.html', {'event_form': event_form})
