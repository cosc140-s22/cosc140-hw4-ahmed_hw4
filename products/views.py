from itertools import product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all().order_by('name')
    return render(request, "products/index.html", context={"products":products})

def show(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/show.html", context={"product": product})