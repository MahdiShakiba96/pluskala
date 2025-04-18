from django.db import models
from django.urls import reverse

# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True )
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField(max_length=255 , blank=True)
    cat_image = models.ImageField(upload_to = 'photos/categories' , blank=True)


    # change the default behavior of models and its fields
    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    # for make url for each category name 
    def get_url(self):
        return reverse('products_by_category' , args=[self.slug])

    # use name field of category table to show in Category table in django admin panel
    def __str__(self):
        return self.category_name