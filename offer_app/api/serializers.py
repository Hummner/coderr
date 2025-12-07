from rest_framework import serializers
from ..models import Offer, OfferDetails
from django.contrib.auth.models import User


class OfferDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating individual offer detail objects.
    Used inside OfferSerializer to handle nested detail data.
    """

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
    """
    Serializer for creating and updating an Offer, including multiple nested
    OfferDetails entries. Handles nested creation and partial update logic.
    """

    details = OfferDetailsSerializer(many=True, source='offer_detail')

    def create(self, validated_data):
        """
        Create a new offer and its related offer detail entries.
        Assigns the authenticated user as the offer creator.
        """
        details = validated_data.pop('offer_detail')
        user = self.context['request'].user
        offer = Offer.objects.create(creator=user, **validated_data)

        for detail in details:
            OfferDetails.objects.create(offer=offer, **detail)

        return offer
    
    def update(self, instance, validated_data):
        """
        Update the Offer instance and optionally update matching OfferDetails
        objects based on their offer_type. Only allowed fields are overwritten.
        """
        details = validated_data.pop('offer_detail', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if details:
            for detail in details:
                detail_type = detail.get('offer_type', None)

                if detail_type is not None:
                    try:
                        detail_instace = instance.offer_detail.get(offer_type=detail_type)
                    except OfferDetails.DoesNotExist:
                        continue
                
                for attr, value in detail.items():
                    if attr in ['id', 'offer_type']:
                        continue
                    setattr(detail_instace, attr, value)
                    detail_instace.save()

        return instance

    class Meta:
        model = Offer
        fields = ['id', 'title', 'image', 'description', 'details']


class OfferListSerializer(serializers.ModelSerializer):
    """
    Serializer used for listing offers with lightweight detail links,
    summary pricing information, and basic creator data.
    """

    details = serializers.SerializerMethodField()
    min_price = serializers.IntegerField(read_only=True)
    min_delivery_time = serializers.IntegerField(read_only=True)
    user_detail = serializers.SerializerMethodField()

    def get_user_detail(self, obj):
        """
        Return a summary of the creator's public information.
        """
        user = obj.creator
        return {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    
    def get_details(self, obj):
        """
        Return only the ID and URL for each offer detail entry.
        Useful for listing views where full detail data is not needed.
        """
        details = obj.offer_detail.all()
        data = []

        for detail in details:
            data.append({'id': detail.id, 'url': f'/offerdetails/{detail.id}'})

        return data

    class Meta:
        model = Offer
        fields = [
            'id',
            'title',
            'image',
            'description',
            'details',
            'min_price',
            'min_delivery_time',
            'user_detail',
            'updated_at',
            'created_at'
        ]


class OfferRetrieveSerialzier(serializers.ModelSerializer):
    """
    Serializer for retrieving a single offer, including creator ID, timestamps,
    summary pricing, delivery info, and lightweight detail references.
    """

    min_price = serializers.IntegerField(read_only=True)
    min_delivery_time = serializers.IntegerField(read_only=True)
    details = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='creator'
    )

    def get_details(self, obj):
        """
        Return ID and full API URL for each OfferDetail belonging to the offer.
        """
        details = obj.offer_detail.all()
        data = []

        for detail in details:
            data.append({
                'id': detail.id,
                'url': f'http://127.0.0.1:8000/api/offerdetails/{detail.id}'
            })

        return data

    class Meta:
        model = Offer
        fields = [
            'id',
            'user',
            'title',
            'image',
            'description',
            'created_at',
            'updated_at',
            'details',
            'min_price',
            'min_delivery_time'
        ]


class OfferDeatilsRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer for returning the full stored data of a single OfferDetail object.
    Used in offer detail retrieval views.
    """

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
