from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from .tasks import send_product_notification

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self,serializer):
        product= serializer.save()
        send_product_notification.delay(product.name,str(product.price))
