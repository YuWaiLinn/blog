from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from products.models import ProductItem
from products.serializers import ProductItemListSerializer

class ListProductItem(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """
        Return a list of all users.
        """
        print("Product list vieew")
        products = ProductItem.objects.all()

        print("Product list vieew : ", products)
        ser = ProductItemListSerializer(products,  context={"request": request}, many=True)
        print("Product list vieew : ", ser.data)
        return Response(data=ser.data, status=200)