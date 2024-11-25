from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("checkout/", include("ecommerce.apps.checkout.urls", namespace="checkout")),
    path("basket/", include("ecommerce.apps.basket.urls", namespace="basket")),
    path("account/", include("ecommerce.apps.account.urls", namespace="account")),
    path("orders/", include("ecommerce.apps.orders.urls", namespace="orders")),
    path("coupons/", include("ecommerce.apps.coupons.urls", namespace="coupons")),
    path("", include("ecommerce.apps.catalogue.urls", namespace="catalogue")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
