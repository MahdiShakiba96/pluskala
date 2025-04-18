from django.contrib import admin
from .models import Category

# ModelAdmin class to create models interface in admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name' , 'slug')


# model registration 
admin.site.register(Category ,CategoryAdmin )