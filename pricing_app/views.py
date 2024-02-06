from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PricingConfig, PricingTier

class CalculatePrice(APIView):
    def get(self, request):
        distance = float(request.query_params.get('distance'))
        time = float(request.query_params.get('time'))
        day_of_week = request.query_params.get('day_of_week')
        
        try:
            config = PricingConfig.objects.filter(is_active=True).latest('created_at')
            tier = PricingTier.objects.get(config=config, day_of_week=day_of_week)
        except PricingConfig.DoesNotExist:
            return Response({'error': 'No active pricing configuration found'})
        except PricingTier.DoesNotExist:
            return Response({'error': 'No pricing tier found for the specified day'})

        additional_distance_charge = max(distance - 3, 0) * tier.distance_additional_price
        time_multiplier_factor = tier.time_multiplier_factor
        if time > 60:
            time_multiplier_factor *= 1.25
        if time > 120:
            time_multiplier_factor *= 2.2
        
        price = (tier.distance_base_price + additional_distance_charge) + (time * time_multiplier_factor) + ((time - 3) // 3 * tier.waiting_charges)
        
        return Response({'price': price})
