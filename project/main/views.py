import sys
import os
sys.path.append(os.getcwd())
from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from auth_.permissions import ClientPermission, ClientOrAdminPermission
from .models import Cart
from .serializers import CartSerializer, GetCartSerializer



class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]


class CartDetailedView(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    permission_classes = [ClientOrAdminPermission]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetCartSerializer
        elif self.request.method == 'PUT':
            return CartSerializer

    def get(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(client=self.request.user)
        except:
            return JsonResponse({"404": "no such cart"}, safe=False)
        return JsonResponse(GetCartSerializer(cart).data, safe=False)

    def patch(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(client=self.request.user)
        except:
            return JsonResponse({"404": "no such cart"}, safe=False)
        add_products = self.request.data.get('add')
        remove_products = self.request.data.get('remove')
        if add_products is not None:
            for product in add_products:
                try:
                    cart.products.add(product)
                except:
                    return JsonResponse({"404": "no such product"}, safe=False)
        if remove_products is not None:
            for product in remove_products:
                try:
                    cart.products.remove(product)
                except:
                    return JsonResponse({"404": "no such product"}, safe=False)
        cart.save()
        return JsonResponse(GetCartSerializer(cart).data, safe=False)
