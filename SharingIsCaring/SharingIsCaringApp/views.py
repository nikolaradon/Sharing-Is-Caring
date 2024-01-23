from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from .models import Donation, Institution, Category
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



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


class AddDonationView(LoginRequiredMixin, View):
    login_url = 'login' 

    def get(self, request):
        categories = Category.objects.all()
        insitutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'institutions': insitutions})
    


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                if User.objects.filter(email=email).exists():
                    form.add_error('password', 'Invalid password')
                else:
                    messages.error(request, "This user doesn't exist.")
                    return redirect('register')
            
        return render(request, 'login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
            form = RegisterForm()
            return render(request, "register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = form.cleaned_data['email']
                user.save()
                return redirect('login')
            except IntegrityError:
                form.add_error('email', 'User with this email is already registered')

        return render(request, "register.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


class UserProfileView(View):
    def get(self, request):
        return render(request, 'user_profile.html', {'user': request.user})