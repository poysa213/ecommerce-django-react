from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.decorators import action
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet



from .serializers import  RegisterSerializer, UserSerializer, CustomerSerializer
from .models import Customer

from .permissions import FullDjangoModelPermissions
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    queryset = get_user_model().objects.all()

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            })
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all() 
    serializer_class = CustomerSerializer
    permission_classes = [FullDjangoModelPermissions]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    
        
