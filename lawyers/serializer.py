from django.contrib.auth import get_user_model
from rest_framework import serializers
from .import models

User = get_user_model()

def emailAlreadyExist(email):
    return User.objects.filter(email=email).exists()

class LawyerUserSerilaizer(serializers.ModelSerializer):
    is_client = serializers.BooleanField(read_only=True)
    is_lawyer = serializers.BooleanField(read_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    class Meta:
        model = models.Lawyer
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_client', 'is_lawyer']

    def validate(self, attrs):
        try:
            data  = super().validate(attrs)
            email = data['email']
        except:
            email = None
        if emailAlreadyExist(email):
            raise serializers.ValidationError({'error' : 'Email already exist'})
        return data