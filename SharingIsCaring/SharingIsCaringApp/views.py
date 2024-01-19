from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from .models import Donation, Institution


# Create your views here.


class LandingPageView(View):
    def get(self, request):
        total_bags = Donation.objects.aggregate(total_bags=Sum('quantity'))['total_bags'] or 0
        supported_organizations = Institution.objects.count()

        context = {
            'total_bags': total_bags,
            'supported_organizations': supported_organizations,
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

