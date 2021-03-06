

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from tutorial.quickstart.models import Producto
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, ProductosSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListProductos(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.IsAuthenticated]