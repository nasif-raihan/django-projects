from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to="categories")


class Products(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, related_name="product_images"
    )
    image = models.ImageField(upload_to="product")
