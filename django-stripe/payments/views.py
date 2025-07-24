import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CoffeePurchase

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
