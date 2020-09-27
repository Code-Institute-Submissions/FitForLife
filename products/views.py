from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product
import logging


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '/tmp/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    products_list = Product.objects.order_by('?')[:5] #retrieve last 5 items randomly
    template = loader.get_template('products/products.html')
    context = {
        'products_list': products_list,
    }
    logger.debug('Product Views:  ' + str(products_list.count()) )
    return HttpResponse(template.render(context, request))
