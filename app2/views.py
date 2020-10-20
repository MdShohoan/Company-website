from django.shortcuts import render
from .models import about, client
from .models import slider,service,portfolio
from django.views.generic import DetailView

def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    servicedata = service.objects.all()
    portfoliodata = portfolio.objects.all()

    context = {
        'about': aboutdata,
        'slider': sliderdata,
        'client': clientdata,
        'service': servicedata,
        'portfolio': portfoliodata,

    }

    return render(request, 'app2/home.html', context)

class Servicedetails(DetailView):
    model = service
    template_name = 'app2/servicedetails.html'

def aboutus(request):
    return render(request, 'app2/about.html')



def sliderus(request):
    return render(request, 'app2/slider.html')


def profile(request):
    return render(request, 'app2/profile.html')


def team(request):
    return render(request, 'app2/team.html')

