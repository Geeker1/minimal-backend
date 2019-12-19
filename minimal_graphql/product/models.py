from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.URLField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()
    stock = models.PositiveIntegerField()
    image = models.URLField(max_length=1000)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

