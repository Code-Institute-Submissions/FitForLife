from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product
import logging

logger = logging.getLogger(__name__) #name specifies the module name


# Create your views here.

def index(request):
    products_list = Product.objects.order_by('?')[:5] #retrieve last 5 items randomly
    template = loader.get_template('products/products.html')
    context = {
        'products_list': products_list,
    }
    logger.debug('Product Views:  ' + str(products_list.count()) )
    return HttpResponse(template.render(context, request))
