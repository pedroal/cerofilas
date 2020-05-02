

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tutorial.quickstart.models import Producto, Usuario, Entidad, Comercio, Pedido
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, ProductosSerializer, UsuarioSerializer, \
    EntidadSerializer, ComercioSerializer, PedidoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioSaveData( APIView ):
    serializer_class = UsuarioSerializer

    def post(self, request):
        ser = UsuarioSerializer( data=request.data )
        ser.is_valid( raise_exception=True )
        """
        
        Create and return a new `Serie` instance, given the validated data.
        """
        return Response( Usuario.objects.create( **request ) )





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

class ListUsuarios(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListEntidades(viewsets.ModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListComercios(viewsets.ModelViewSet):
    queryset = Comercio.objects.all()
    serializer_class = ComercioSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListPedidos(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]
