from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name  = 'categories'
        verbose_name_plural = 'categories'


    def __str__(self):
        return  '{}' .format(self.name)  

    def __str__(self):
        return self.name


class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def __str__(self):
        return '{}' .format(self.name, self.category.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
  # Call the "real" save() method.