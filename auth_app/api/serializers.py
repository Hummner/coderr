from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from profile_app.models import Profile



class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only = True)
    type = serializers.ChoiceField(choices=[('customer', 'customer'), ('business', 'business')])

    
    def validate(self, attrs):
        pw = attrs['password']
        rep_pw = attrs['repeated_password']

        if pw != rep_pw:
            raise serializers.ValidationError("Password and repeated password are not equal")
        return attrs
    
    def create(self, validated_data):
        type = validated_data.pop('type')
        validated_data.pop('repeated_password')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        username = user.username

        #### hier kommt noch später Profile.objects.create(user=user, type=type)
        Profile.objects.create(user=user, type=type, username=username)
        return user
    

    class Meta:
        model = User
        fields = ['id', 'username', 'repeated_password', 'password', 'type', 'email']
        write_only = ['password', 'repeated_password', 'type']


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        request=self.context.get('request')
        username = attrs['username']
        password = attrs['password']

        if username and password:
            user = authenticate(request, username=username, password=password)

            if not user:
                raise serializers.ValidationError("Username or password invalid")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")


        attrs['user'] = user
        return attrs