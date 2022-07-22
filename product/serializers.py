from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    '''
    category serializer for handling crud operation
    '''
    
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    '''
    product serializer for handling crud operation
    '''

    class Meta:
        model = Product
        fields = '__all__'
