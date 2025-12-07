from rest_framework import serializers
from review_app.models import Review
from profile_app.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating reviews. It validates that the target
    user is a business profile, enforces that only certain fields can be updated
    on PATCH, and ensures that each reviewer may submit only one review per
    business user.
    """

    def validate_business_user(self, value):
        """
        Ensure that the selected business_user has an associated profile
        of type 'business'; otherwise, reject the value as invalid.
        """
        business_user_id = value.id
        try:
            Profile.objects.get(Q(user_id=business_user_id) & Q(type='business'))
        except Profile.DoesNotExist:
            raise serializers.ValidationError('This business_user does not exist.')
        
        return value

    def validate(self, attrs):
        """
        Apply request-method-specific validation rules: PATCH requests are
        restricted to certain fields, while POST requests are checked so that
        a user cannot review the same business more than once.
        """
        request = self.context['request']
        if request.method == "PATCH":
            return self.validate_patched_fileds(request, attrs)
        
        if request.method == "POST":
            asd = self.validate_post_request(request, attrs)
            return asd

        return attrs
    

    def validate_patched_fileds(self, request, attrs):
        """
        Validate that only allowed fields (rating, description) are present
        in a PATCH request, preventing partial updates to protected fields.
        """
        allow_fields = ['rating', 'description']

        for field in request.data:
            if field not in allow_fields:
                raise serializers.ValidationError(f"{field} cannot be updated.", code=400)
        return attrs
    
    def validate_post_request(self, request, attrs):
        """
        Ensure that the authenticated user does not already have a review
        for the specified business_user, enforcing a one-review-per-user rule.
        """
        business_user = attrs['business_user']
        reviewer = request.user

        is_first_review = business_user.review.filter(reviewer=reviewer)

        if is_first_review:
            raise serializers.ValidationError("You can only submit one review for this user.")

        return attrs

    class Meta:
        model = Review
        fields = [
            'id',
            'reviewer',
            'rating',
            'created_at',
            'updated_at',
            'description',
            'business_user'
        ]
        read_only_fields = ['reviewer', 'updated_at', 'created_at']
