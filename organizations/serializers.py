from rest_framework import serializers
from . import models

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'

class OrganizatioStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrganizatioStuff
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentMethod
        fields = '__all__'