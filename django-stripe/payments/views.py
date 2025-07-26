from rest_framework.response import Response
from rest_framework import status

import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from .models import CoffeePurchase

stripe.api_key = settings.STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET = settings.STRIPE_WEBHOOK_SECRET
stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyCoffeeView(APIView):
    def post(self, request):
        try:
            amount = 500  # $5.00

            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {"name": "Buy Me a Coffee ☕"},
                            "unit_amount": amount,
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=settings.STRIPE_SUCCESS_URL,
                cancel_url=settings.STRIPE_CANCEL_URL,
            )

            CoffeePurchase.objects.create(session_id=session.id, amount=amount)

            return Response({"checkout_url": session.url})

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class StripeWebhookView(APIView):
    authentication_classes = []  # Allow unauthenticated
    permission_classes = []

    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, STRIPE_WEBHOOK_SECRET
            )
        except ValueError:
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError:
            return HttpResponse(status=400)

        # Handle the event
        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]
            session_id = session.get("id")

            try:
                purchase = CoffeePurchase.objects.get(session_id=session_id)
                purchase.is_paid = True
                purchase.save()
            except CoffeePurchase.DoesNotExist:
                pass

        return HttpResponse(status=200)


def success(request):
    return JsonResponse({"status": "Success"})


def cancel(request):
    return JsonResponse({"status": "Cancel"})
