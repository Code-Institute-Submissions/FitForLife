from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import logging
import logging.config
from checkout.webhook_handler import StripeWH_Handler

import stripe

logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger
webhook_debug = False # used for debuging issues with Stripe Signature Verification

def show_request_data(request):
    if request.POST:
        for key in request.POST:
            logger.warn('Request Key POST:' + str(key) + ' = ' + str(request.POST[key]))
    if request.META:
        for key in request.META:
            logger.warn('Request Key META:' + str(key) + ' = ' + str(request.META[key]))

@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    if webhook_debug == True:   
        logger.warn('Webhook called')
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY


    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        if webhook_debug == True:
            logger.warn('Webhook: creating event')
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        if webhook_debug == True:
            logger.warn('Webhook:Invalid payload')
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        if webhook_debug == True:
            logger.warn('Webhook:Invalid signature using wh_s:[' + str(wh_secret) + ']')
            logger.warn('Webhook:Invalid signature using api_s:[' + str(stripe.api_key) + ']')
        # Invalid signature
        if webhook_debug == False:
            return HttpResponse(content=e, status=400)
    except Exception as e:
        if webhook_debug == True:
            logger.warn('Webhook:An unknown exception occured')
        if webhook_debug == False:
            return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    if webhook_debug == True:
        logger.warn('Webhook:Calling Stripe Handler')
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    if webhook_debug == True:
        logger.warn('Webhook:Processing event Handler')
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    if webhook_debug == True:
        logger.warn('Webhook:Completing: ' + str(response))
    return response
