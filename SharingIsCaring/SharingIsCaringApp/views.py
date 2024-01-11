from django.shortcuts import render
from django.views import View


# Create your views here.

class LandingPageView(View):
    def get(self, request):
        return render(request, 'index2.html')

class AddDonationView(View):
    def get(self, request):
        return render(request, 'form2.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')