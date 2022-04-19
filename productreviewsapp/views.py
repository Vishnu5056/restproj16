from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product,Review
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
# Create your views here.
from .serializers import ProductSerializer,ReviewSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
class ProductsList(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
class ReviewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)