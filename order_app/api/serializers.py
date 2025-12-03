from rest_framework import serializers
from ..models import Order
from offer_app.models import OfferDetails



class OrderSerializer(serializers.ModelSerializer):

    offer_detail_id = serializers.PrimaryKeyRelatedField(
        queryset = OfferDetails.objects.all(),
        write_only = True
    )


    def validate(self, attrs):

        if self.instance is None:
            return attrs

        request = self.context['request']
        allowed = 'status'
        for field in request.data:
            if field not in allowed:
                raise serializers.ValidationError(f"{field} cannot be updated.", code=400)
            
        return attrs

    def create(self, validated_data):

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