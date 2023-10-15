from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
import json, uuid
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from settings import settings as parametres
from django.utils.translation import gettext as _
import stripe

# Create your views here.
@csrf_exempt
def stripeTokenHandler(request):
    if request.method == "POST":
        datas = request.POST
        
        try:
            stripe.api_key = "sk_test_51O11ddBltzuPBBd1JY9carffmwRn2DXMOfc5uw7MabKtZhrbDUrWIPuryZ5qLsJQ9ZGeqlJWIkOmi3HDm0tS8jOz005BTmzl9u"

            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount= 4500,
                currency='eur',
                # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            print(intent)
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })

        except Exception as e:
            # Gérez les autres erreurs
            print("Error: " + str(e))
            return JsonResponse({"status": False, 'message': str(e)})

    return JsonResponse({"status": False, 'message': 'Invalid request'})
