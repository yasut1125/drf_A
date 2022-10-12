from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price']

    def create(self, validated_data):
        newItem = Item.objects.create(
            name = validated_data["name"],
            price = validated_data["price"],
        )
        newItem.save()
        return newItem