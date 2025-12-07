from rest_framework import serializers
from profile_app.models import Profile


class BusinessListSerializer(serializers.ModelSerializer):
    """
    Serializer used to return public-facing information about business profiles.
    This serializer is optimized for listing views and includes all fields that
    help represent a business user in searches or directory displays.
    """

    class Meta:
        model = Profile
        fields = [
            'user',
            'username',
            'first_name',
            'last_name',
            'file',
            'location',
            'tel',
            'description',
            'working_hours',
            'type'
        ]


class CustomerListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing customer profiles. Only essential identifying and
    display-related fields are included, since customers require less public
    profile data compared to business users.
    """

    class Meta:
        model = Profile
        fields = [
            'user',
            'username',
            'type',
            'first_name',
            'last_name',
            'file'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer used for retrieving and updating individual profile data.
    It exposes all editable and read-only fields relevant to both business
    and customer users, allowing flexible profile management.
    """

    class Meta:
        model = Profile
        fields = [
            'user',
            'username',
            'type',
            'first_name',
            'last_name',
            'file',
            'location',
            'tel',
            'description',
            'working_hours',
            'type',
            'email',
            'created_at'
        ]
