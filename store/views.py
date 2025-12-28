from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer

@api_view(['GET'])
def get_products(req):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_categories(req):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)