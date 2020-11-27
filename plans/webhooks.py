import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import logging
import logging.config
from checkout.webhook_handler import StripeWH_Handler

import stripe

logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger

#@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    logger.warn('Webhook called')

    for key in request.POST:
        logger.warn('Request Key:' + str(key) + ' = ' request.POST[key])
    for key in request.META:
        logger.warn('Request Key:' + str(key) + ' = ' request.POST[key])

    logger.warn('Webhook:Completing')
    return response
