from django.http import JsonResponse
import json, uuid
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from settings import settings as parametres
from django.utils.translation import gettext as _
import stripe
from boutiqueApp.models import Produit
from vitrineApp.models import Participation
from boutiqueApp.models import Commande, LigneCommande
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
@csrf_exempt
def stripeTokenHandler(request):
    if request.method == "POST":
        datas = request.POST
        try:
            stripe.api_key = "sk_test_51O11ddBltzuPBBd1JY9carffmwRn2DXMOfc5uw7MabKtZhrbDUrWIPuryZ5qLsJQ9ZGeqlJWIkOmi3HDm0tS8jOz005BTmzl9u"
            participation = Participation.objects.get(id = datas["participation_id"])
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount= int(float(participation.price) * 100),
                currency='eur',
                # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            
            participation.client_secret = intent["client_secret"]
            participation.save()
            
            return JsonResponse({
                "status": True,
                'clientSecret': intent['client_secret']
            })

        except Exception as e:
            # Gérez les autres erreurs
            print("Error: " + str(e))
            return JsonResponse({"status": False, 'message': str(e)})

    return JsonResponse({"status": False, 'message': 'Invalid request'})