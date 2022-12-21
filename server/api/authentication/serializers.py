from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'phone_number', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'phone_number', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        password_data = validated_data.pop('password')
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password_data)
        user.save()
        return user