from django.shortcuts import render
from django.views import View


# Create your views here.


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class StepsView(View):
    pass


class AboutUsView(View):
    pass


class HelpView(View):
    pass


class FormConfirmationView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')