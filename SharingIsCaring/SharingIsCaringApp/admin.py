from django.contrib import admin
from .models import Institution, Category

# Register your models here.


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'display_categories')


    def display_categories(self, obj):
            return ", ".join([category.name for category in obj.categories.all()])
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
      list_display = ('name',)
      