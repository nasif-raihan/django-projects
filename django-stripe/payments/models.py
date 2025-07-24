from django.db import models


class CoffeePurchase(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField(default=500)  # in cents
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase #{self.id} - {'Paid' if self.is_paid else 'Pending'}"
