'''Api'''

from rest_framework import viewsets,permissions
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    '''View Set'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (SearchFilter,OrderingFilter,DjangoFilterBackend)
    filterset_fields = ('id', 'email', 'password','name','shippingAddress')
    search_fields = ('id', 'email', 'password','name','shippingAddress')