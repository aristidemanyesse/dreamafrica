from django.http import JsonResponse
import json, uuid
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from settings import settings as parametres
from django.utils.translation import gettext as _
import stripe
from boutiqueApp.models import Produit
from vitrineApp.models import Participation
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



def panier_price(request):
    if request.method == "POST":
        try:
            total = 0
            panier = json.loads(request.session.get("dreamteam-panier", "[]"))
            produits = Produit.objects.filter(deleted = False, id__in = [key for key in panier])
            for prod in produits:
                total += prod.price * panier[str(prod.id)]

            
            return JsonResponse({
                "status": True,
                'price': total
            })

        except Exception as e:
            # Gérez les autres erreurs
            print("Error: " + str(e))
            return JsonResponse({"status": False, 'message': str(e)})

    return JsonResponse({"status": False, 'message': 'Invalid request'})



def connexion(request):
    if request.method == "POST":
        datas = request.POST
        user = authenticate(request, username=datas["email"], password=datas["password"])
        if user is not None:
            try:
                if user.is_superuser:
                    request.session["user_id"] = user.id
                    
                login(request, user)
                return JsonResponse({"status":True})
            except Exception as e:
                print("**----------------------------------", e)
                return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors de l'opération, veuillez recommencer !")})
        else:
            return JsonResponse({"status":False, "message":_("Login et/ou mot de passe incorrect !")})



def inscription(request):
    if request.method == "POST":
        try:
            datas = request.POST
            if len(datas["password"]) < 4:
                return JsonResponse({"status":False, "message":_("Le mot de passe n'est pas valide !")})
            
            if datas["password"] != datas["password2"]:
                return JsonResponse({"status":False, "message":_("Les mots de passe de concordent pas !")})
            
            if User.objects.filter(username = datas["email"]).count() > 0:
                return JsonResponse({"status":False, "message":_("Un compte avec cette adresse email existe déjà !")})
            
            user = User(
                username        = datas["email"],
                email           = datas["email"],
                first_name      = datas["fullname"],
                last_name       = "",
                is_superuser    = False,
                is_staff        = False,
            )
            user.set_password(datas["password"])
            user.save()
            return JsonResponse({"status":True, "message":_("ok")})
    
        except Exception as e:
            print("**----------------------------------", e)
            return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors de l'opération, veuillez recommencer !")})