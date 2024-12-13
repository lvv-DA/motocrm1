# crm/serializers.py

from rest_framework import serializers
from .models import Client, Customer, SalesRepresentative, Location, Opportunity, Item

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()  # Nested serializer for related customer

    class Meta:
        model = Client
        fields = '__all__'

class SalesRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRepresentative
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class OpportunitySerializer(serializers.ModelSerializer):
    client = ClientSerializer()  # Nested ClientSerializer
    sales_representative = SalesRepresentativeSerializer()  # Nested SalesRepresentativeSerializer

    class Meta:
        model = Opportunity
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
