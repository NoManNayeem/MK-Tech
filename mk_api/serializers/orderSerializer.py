from django.contrib.auth.models import User, Group
from rest_framework import serializers

from ..serializers.profileSerializer import ProfileSerializer
from ..serializers.productSerializer import ProductSerializer

from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = ProfileSerializer(many=False)
    product = ProductSerializer(many=False)
    class Meta:
        model = Order
        fields = "__all__"
    