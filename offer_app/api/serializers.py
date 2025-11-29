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


class OfferListSerializer(serializers.ModelSerializer):

    details = serializers.SerializerMethodField()

    min_price = serializers.IntegerField(read_only = True)
    min_delivery_time = serializers.IntegerField(read_only = True)
    user_detail = serializers.SerializerMethodField()


    def get_user_detail(self, obj):
        user = obj.creator

        data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

        return data
    
    def get_details(self, obj):
        details = obj.offer_detail.all()
        data = []

        for detail in details:
            data.append({'id': detail.id, 'url': f'/offerdetails/{detail.id}'})

        return data

    class Meta:
        model = Offer
        fields = ['id', 'title', 'image', 'description', 'details', 'min_price', 'min_delivery_time', 'user_detail']