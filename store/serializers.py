from rest_framework import serializers
from .models import Store, Adress, StoreReview, StoreImage


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'owner', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', 'owner')


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ('id', "store", 'street', 'city', 'state', 'zip_code')
        read_only_fields = ('id', 'store')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreReview
        fields = ('id', 'store', 'user', 'rating', 'comment')
        read_only_fields = ('user', "store", "id")


class StoreImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreImage
        fields = ('id', 'store', 'image')
        read_only_fields = ('id', 'store')
