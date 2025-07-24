from django.db import models
from category.models import category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name        = models.CharField(max_length=200, unique=True)
    slug                = models.SlugField(max_length=200, unique=True)
    description         = models.TextField(max_length=500, blank=True)
    price               = models.IntegerField()
    images              = models.ImageField(upload_to='photos/products')
    stock               = models.IntegerField()
    is_available        = models.BooleanField(default=True)
    category            = models.ForeignKey('category.category', on_delete=models.CASCADE)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now=True)

     # Add this field:
    video_link = models.URLField(blank=True, null=True, help_text="Paste full YouTube URL here")


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Message"
        verbose_name_plural = "Users Messages"

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"



class PriceInquiry(models.Model):
    PURPOSE_CHOICES = [
        ('Reselling', 'Reselling'),
        ('End Use', 'End Use'),
        ('Raw Material', 'Raw Material'),
    ]
    purpose = models.CharField(max_length=100, choices=PURPOSE_CHOICES)
    requirement = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Price inquiry"
        verbose_name_plural = "Price inquiries"  # ✅ FIX: Correct plural

    def __str__(self):
        return f"{self.purpose} - {self.requirement[:30]}"