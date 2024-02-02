from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.contrib.auth.hashers import make_password

class UserManager(DjangoUserManager):

    def _create_user(self, first_name, last_name, email, password, **extra_fields):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.password = make_password(password)
        user.save(self.db)

        return user

    def create_user(self, email, first_name, last_name, password, is_staff=False, is_superuser=False, **extra_fields):
        return self._create_user(first_name, last_name, email, password, is_staff=is_staff, is_superuser=is_superuser,
                                 **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, is_staff=True, is_superuser=True, **extra_fields):
        return self._create_user(first_name, last_name, email, password, is_staff=is_staff,
                                 is_superuser=is_superuser, **extra_fields)


# Create your models here.
    
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = UserManager()

    

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name



INSTITUTION_TYPES = (
    ('foundation', 'Foundation'),
    ('nonprofit_organization', 'Nonprofit Organization'),
    ('local_collection', 'Local Collection'),
)

class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=INSTITUTION_TYPES, default='fundacja')
    categories = models.ManyToManyField(Category)



class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Donation {self.id} - {self.quantity} bags'
