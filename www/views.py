from django.utils import timezone
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from www.models import Gig, Intro


def index(request):
    today = datetime.datetime.today()
    today = datetime.datetime(today.year, today.month, today.day, tzinfo=timezone.get_current_timezone())
    next_gig = Gig.objects.filter(when__gt=today).order_by('when')[:1]
    if next_gig:
        next_gig = '%s @ %s' % (next_gig[0].where, next_gig[0].when)
    else:
        next_gig = 'Nothing :('
    intro = Intro.objects.get(name='Intro')
    return render(request, 'www/home.html', {'intro': intro.intro.split('\n'), 'next_gig': next_gig})

def bio(request):
    return HttpResponse("Bio")

def music(request):
    return HttpResponse("Music")

def gigs(request):
    return HttpResponse("Gigs")

def contact_us(request):
    return HttpResponse("Contact Us")