from rest_framework import serializers
from profile_app.models import Profile



class BusinessListSerializer(serializers.ModelSerializer):

    
    

    class Meta:
        model = Profile
        fields = ['user', 'username', 'type']