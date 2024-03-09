import logging

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Product

logger = logging.getLogger(__name__)


class ProductView(View):
    def __init__(self):
        super(ProductView, self).__init__()
        logger.debug(f"ProductView called")

    @staticmethod
    def get(request):
        trending_deals = Product.objects.filter(
            (Q(category="mobile") & Q(discounted_price__lte=10000))
            | (Q(category="laptop") & Q(brand="apple"))
            | (Q(category="top_wear") & Q(selling_price__gte=500))
            | (
                Q(category="bottom_wear") & Q(discounted_price__lte=800)
                | Q(selling_price__gte=500)
            )
        )
        context = {
            "top_wears": Product.objects.filter(category="top_wear"),
            "bottom_wears": Product.objects.filter(category="bottom_wear"),
            "mobiles": Product.objects.filter(category="mobile"),
            "laptops": Product.objects.filter(category="laptop"),
            "trending_deals": trending_deals,
        }
        logger.debug(f"{context=}")
        return render(request, "app/home.html", context=context)


class ProductDetailView(View):
    def get(self, request, pk):
        queryset = get_object_or_404(Product, pk=pk)
        product = {
            "title": queryset.title,
            "selling_price": queryset.selling_price,
            "discounted_price": queryset.discounted_price,
            "description": queryset.description,
            "brand": queryset.brand,
            "category": queryset.category,
            "product_image": queryset.product_image,
        }
        print(product)
        return render(request, "app/product_detail.html", {"product": product})


def add_to_cart(request):
    return render(request, "app/addtocart.html")


def buy_now(request):
    return render(request, "app/buynow.html")


def profile(request):
    return render(request, "app/profile.html")


def address(request):
    return render(request, "app/address.html")


def orders(request):
    return render(request, "app/orders.html")


def change_password(request):
    return render(request, "app/changepassword.html")


def mobile(request, slug_field=None):
    slug_field = slug_field.lower() if slug_field else None
    if slug_field in ("samsung", "iphone"):
        mobiles = Product.objects.filter(category="mobile").filter(brand=slug_field)
    elif slug_field == "below":
        mobiles = Product.objects.filter(
            Q(category="mobile") & Q(discounted_price__lte=10000)
        )
    elif slug_field == "above":
        mobiles = Product.objects.filter(
            Q(category="mobile") & Q(discounted_price__gte=10000)
        )
        print(mobiles)

    else:
        mobiles = Product.objects.filter(category="mobile")

    return render(request, "app/mobile.html", {"mobiles": mobiles})


def login(request):
    return render(request, "app/login.html")


def registration(request):
    return render(request, "app/registration.html")


def checkout(request):
    return render(request, "app/checkout.html")
