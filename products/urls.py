from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('products/', views.index, name="index"),
    path("products/<int:product_id>", views.show, name="show"),
    path("", lambda request: redirect(reverse_lazy("index")))
]