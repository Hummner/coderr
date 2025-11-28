from rest_framework import serializers
from ..models import Offer, OfferDetails


class OfferDetailsSerializer(serializers.ModelSerializer):

  

    class Meta:
        model = OfferDetails
        fields = [
            "id",
            "offer_type",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
        ]
        write_only = ['offer']


class OfferSerializer(serializers.ModelSerializer):
    
    details = OfferDetailsSerializer(many=True, source='offer_detail')

    def create(self, validated_data):


        details = validated_data.pop('offer_detail')
        user = self.context['request'].user
        offer = Offer.objects.create(creator=user, **validated_data)

        for detail in details:
            OfferDetails.objects.create(offer=offer, **detail)
        return offer


    class Meta:
        model = Offer
        fields = ['id', 'title', 'image', 'description', 'details']