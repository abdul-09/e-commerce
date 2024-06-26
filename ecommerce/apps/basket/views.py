from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from ecommerce.apps.catalogue.models import Product
from ecommerce.apps.coupons.forms import CouponApplyForm

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    coupon_apply_form = CouponApplyForm()
    return render(request, "basket/summary.html", {"basket": basket, "coupon_apply_form": coupon_apply_form})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({"qty": basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"qty": basketqty, "subtotal": baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        basketsubtotal = basket.get_subtotal_price()
        response = JsonResponse({"qty": basketqty, "subtotal": basketsubtotal})
        return response
