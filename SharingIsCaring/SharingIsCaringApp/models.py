from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)



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
