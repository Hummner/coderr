from rest_framework import serializers
from ..models import Order
from offer_app.models import OfferDetails


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating orders. On creation it copies all
    relevant data from the selected OfferDetails instance to keep a snapshot
    of the offer at the time of ordering, and on update it restricts changes
    so that only the order status can be modified.
    """

    offer_detail_id = serializers.PrimaryKeyRelatedField(
        queryset=OfferDetails.objects.all(),
        write_only=True
    )

    def validate(self, attrs):
        """
        Validate update requests so that only the 'status' field
        can be changed once the order has been created.
        """
        if self.instance is None:
            return attrs

        request = self.context['request']
        allowed = 'status'
        for field in request.data:
            if field not in allowed:
                raise serializers.ValidationError(f"{field} cannot be updated.", code=400)

        return attrs

    def create(self, validated_data):
        """
        Create a new order based on a selected OfferDetails instance.
        Copies offer-related fields and links the current user as customer.
        """
        request = self.context['request']
        offer = validated_data.pop('offer_detail_id')

        validated_data['customer_user'] = request.user
        validated_data['business_user'] = offer.offer.creator
        validated_data['offer_type'] = offer.offer_type
        validated_data['title'] = offer.title
        validated_data['revisions'] = offer.revisions
        validated_data['delivery_time_in_days'] = offer.delivery_time_in_days
        validated_data['price'] = offer.price
        validated_data['features'] = offer.features
        validated_data['offer_detail'] = offer

        order = Order.objects.create(**validated_data)
        return order

    class Meta:
        model = Order
        fields = [
            "id",
            "customer_user",
            "business_user",
            "offer_type",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "status",
            "updated_at",
            "created_at",
            "offer_detail_id"
        ]
        read_only_fields = [
            "customer_user",
            "business_user",
            "offer_type",
            "title",
            "revisions",
            "delivery_time_in_days",
            "price",
            "features",
            "updated_at",
            "created_at",
        ]