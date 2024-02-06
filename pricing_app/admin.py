from django.contrib import admin
from .models import PricingConfig, PricingTier, PricingLog

admin.site.register(PricingConfig)
admin.site.register(PricingTier)
admin.site.register(PricingLog)
