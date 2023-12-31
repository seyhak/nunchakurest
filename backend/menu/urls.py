# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    MenuSetViewSet,
    MenuViewSet,
    OrderViewSet,
    ProductViewSet,
)

router = DefaultRouter()
router.register(r"products", ProductViewSet, "products")
router.register(r"categories", CategoryViewSet, "categories")
router.register(r"menus", MenuViewSet, "menus")
router.register(r"orders", OrderViewSet, "orders")
router.register(r"menu-sets", MenuSetViewSet, "menu-sets")

app_name = "menu"
urlpatterns = [
    path("", include(router.urls)),
]
