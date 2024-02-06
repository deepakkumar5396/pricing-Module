from django.db import models
from django.contrib.auth.models import User

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PricingTier(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    distance_base_price = models.DecimalField(max_digits=6, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=6, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=6, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=6, decimal_places=2)

class PricingLog(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
