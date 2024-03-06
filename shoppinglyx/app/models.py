from django.contrib.auth.models import User
from django.db import models

DIVISIONS = {
    "dhaka": "Dhaka",
    "khulna": "Khulna",
    "sylhet": "Sylhet",
    "rangpur": "Rangpur",
    "barishal": "Barishal",
    "rajshahi": "Rajshahi",
    "mymensingh": "Mymensingh",
    "chattogram": "Chattogram",
}

CATEGORY = {
    "Mobile": "Mobile",
    "Laptop": "Laptop",
    "Top Wear": "Top Wear",
    "Bottom Wear": "Bottom Wear",
}

STATUS = {
    "packed": "Packed",
    "accepted": "Accepted",
    "canceled": "Canceled",
    "delivered": "Delivered",
    "on_the_way": "On the way",
}


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    zipcode = models.IntegerField(max_length=100)
    division = models.CharField(choices=DIVISIONS, max_length=100)

    def __str__(self):
        return f"{self.id}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY, max_length=100)
    product_image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return f"{self.id}"


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
