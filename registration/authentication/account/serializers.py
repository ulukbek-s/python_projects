from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import CustomUser

User = get_user_model()


class RegisterApiSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(min_length=6, required=True,
                                     write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=6, required=True,
                                      write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('id', 'phone_number', 'password',
                  'password2', 'first_name', 'last_name',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if attrs.get('password') != password2:
            raise serializers.ValidationError('Password and password2 did not match')
        if not attrs.get('password').isalnum():
            raise serializers.ValidationError('Password must contain letters and numbers')
        phone_number = attrs.get('phone_number')
        user = authenticate(username=phone_number, password=password2)
        return attrs


class LoginApiSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(min_length=6, required=True,
                                     write_only=True, style={'input_type': 'password'})