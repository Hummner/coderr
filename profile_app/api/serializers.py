from rest_framework import serializers
from profile_app.models import Profile



class BusinessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'username', 'first_name', 'last_name', 'file', 'location', 'tel', 'description', 'working_hours', 'type']

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'username', 'type', 'first_name', 'last_name', 'file']

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user', 'username', 'type', 'first_name', 'last_name', 'file', 'location', 'tel', 'description', 'working_hours', 'type', 'email', 'created_at']

    # def get_file(self, obj):
    #     if obj.file:
    #         return obj.file.name.split("/")[-1]
    #     return None