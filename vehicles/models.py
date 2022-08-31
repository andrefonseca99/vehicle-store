from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    TRANSMISSION = [
        ('Manual', 'Manual'),
        ('Automático', 'Automático')
    ]
    FUEL_TYPE = [
        ('Diesel', 'Diesel'),
        ('Elétrico', 'Elétrico'),
        ('Etanol', 'Etanol'),
        ('Flex', 'Flex'),
        ('Gasolina', 'Gasolina'),
        ('GNV', 'GNV'),
        ('Híbrido', 'Híbrido'),
    ]


    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField()
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=65, choices=TRANSMISSION)
    manufacture_year = models.IntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(2100)
        ]
    )
    fuel_type = models.CharField(max_length=65, choices=FUEL_TYPE)
    interior_color = models.CharField(max_length=65)
    exterior_color = models.CharField(max_length=65)
    engine = models.CharField(max_length=65)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='vehicles/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
     
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vehicles:vehicle', args=(self.id,))

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            while Vehicle.objects.filter(slug=slug).exists():
                slug = slug + '-' + get_random_string(length=4)
            self.slug = slug

        return super().save(*args, **kwargs)
