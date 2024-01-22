from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from .models import Donation, Institution


# Create your views here.


class LandingPageView(View):
    def get(self, request):
        total_bags = Donation.objects.aggregate(total_bags=Sum('quantity'))['total_bags'] or 0
        supported_organizations = Institution.objects.count()
        fundations = Institution.objects.filter(type='foundation')
        nonprofits = Institution.objects.filter(type='nonprofit_organization')
        local_collections = Institution.objects.filter(type='local_collection')



        context = {
            'total_bags': total_bags,
            'supported_organizations': supported_organizations,
            'fundations': fundations,
            'nonprofits': nonprofits,
            'local_collections': local_collections,
        }

        return render(request, 'index.html', context)


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

