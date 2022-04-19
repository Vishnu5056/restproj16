from .models import Product,Review
from rest_framework import serializers
class ReviewSerializer(serializers.ModelSerializer):
    created_by=serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model=Review
        fields=('id','title','review','rating','created_by')
class ProductSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(read_only=True,many=True)
    class Meta:
        model=Product
        fields=('pid','pname','pcost','pmfdt','pexpdt','reviews')

