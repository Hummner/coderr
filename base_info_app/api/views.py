from rest_framework.views import APIView
from rest_framework.response import Response
from review_app.models import Review
from django.db.models import Avg, Count
from profile_app.models import Profile
from offer_app.models import Offer


class BaseInfo(APIView):
    def get(self, request):
        """
        Retrieve and return general application statistics, including the total number 
        of reviews, the average review rating (rounded to two decimals), the number of 
        business profiles, and the total number of offers. This endpoint provides a 
        quick overview of key metrics used for dashboard or summary displays.
        """
        
        stats = Review.objects.aggregate(
            review_count=Count('id'),
            average_rating=Avg('rating')
        )

        average_rating = stats['average_rating']
        if average_rating is not None:
            average_rating = round(average_rating, 2)

        business_profile_count = Profile.objects.filter(type='business').count()
        offer_count = Offer.objects.count()

        return Response({
            "review_count": stats['review_count'],
            "average_rating": average_rating,
            "business_profile_count": business_profile_count,
            "offer_count": offer_count
        })
