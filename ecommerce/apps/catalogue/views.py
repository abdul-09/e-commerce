from django.shortcuts import get_object_or_404, render

from .models import Category, Product
from ecommerce.apps.basket.basket import Basket


def product_all(request):
    basket = Basket(request)
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "catalogue/index.html", {"products": products, "basket": basket})


def category_list(request, category_slug=None):
    basket = Basket(request)
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(slug=category_slug).get_descendants(include_self=True)
    )
    return render(request, "catalogue/category.html", {"category": category, "products": products, "basket": basket})


def product_detail(request, slug):
    basket = Basket(request)
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "catalogue/single.html", {"product": product, "basket": basket})
