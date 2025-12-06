from rest_framework import serializers
from review_app.models import Review
from profile_app.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q

class ReviewSerializer(serializers.ModelSerializer):




    reviewer = serializers.CurrentUserDefault()

    def validate_business_user(self, value):
        business_user_id = value.id
        try:
            Profile.objects.get(Q(user_id=business_user_id) & Q(type='business'))
        except Profile.DoesNotExist:
            raise serializers.ValidationError('A business profile for this user does not exist.')
        
        return value

    def validate(self, attrs):
        request = self.context['request']
        if request.method == "PATCH":
            return self.validate_patched_fileds(request, attrs)
        
        if request.method == "POST":
            return self.validate_post_request(request, attrs)
        return attrs
    

    def validate_patched_fileds(self, request, attrs):
        allow_fields = ['rating', 'description']

        for field in request.data:
            if field not in allow_fields:
                raise serializers.ValidationError(f"{field} cannot be updated.", code=400)
        return attrs
    
    def validate_post_request(self, request, attrs):
        business_user = attrs['business_user']
        reviewer = request.user

        is_first_review = business_user.review.filter(reviewer=reviewer)

        if is_first_review:
            return attrs
            raise serializers.ValidationError("You can only submit one review for this user.")

        return attrs

    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'rating', 'created_at', 'uploaded_at', 'description', 'business_user']
        read_only_fields = ['reviewer', 'uploaded_at', 'created_at']