from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from .models import Donation, Institution, Category
from .forms import RegisterForm, LoginForm, EditUserProfileForm
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
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'institutions': institutions})

    def post(self, request):
        if request.method == 'POST':
            quantity = request.POST.get('quantity')
            categories_ids = request.POST.getlist('categories')
            institution_id = request.POST.get('institution')
            address = request.POST.get('address')
            phone_number = request.POST.get('phone')
            city = request.POST.get('city')
            zip_code = request.POST.get('postcode')
            pick_up_date = request.POST.get('data')
            pick_up_time = request.POST.get('time')
            pick_up_comment = request.POST.get('more_info')

            institution = Institution.objects.get(id=institution_id)
            donation = Donation.objects.create(
                quantity=quantity,
                institution=institution,
                address=address,
                phone_number=phone_number,
                city=city,
                zip_code=zip_code,
                pick_up_date=pick_up_date,
                pick_up_time=pick_up_time,
                pick_up_comment=pick_up_comment,
                user=request.user
            )

            for category_id in categories_ids:
                category = Category.objects.get(id=category_id)
                donation.categories.add(category)

            donation.save()

            return redirect('form-confirmation')

    
class ConfirmationFormView(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')



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
        user_donations = Donation.objects.filter(user=request.user)
        return render(request, 'user_profile.html', {'user': request.user, 'user_donations': user_donations})
    

class EditUserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditUserProfileForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': form})

    def post(self, request):
        form = EditUserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
        return render(request, 'edit_profile.html', {'form': form})


class ChangePasswordView(View):
    def get(self, request):
        pass