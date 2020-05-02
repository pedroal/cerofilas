from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tutorial.quickstart.models import Producto, Usuario, Entidad, Comercio, Pedido


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductosSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto','tipo','precio','descripcion','id_comercio_id']

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','mail','fecha_nacimiento','contraseña','nacionalidad']

class EntidadSerializer(ModelSerializer):
    class Meta:
        model : Entidad
        fields = ['id_entidad','nombre','iibb','calle','numero','piso','departamento']

class ComercioSerializer(ModelSerializer):
    class Meta:
        model : Comercio
        fields = ['id_comercio','id_entidad','cuit','disponible','razon_social','nombre']

class PedidoSerializer(ModelSerializer):
    class Meta:
        model : Pedido
        fields = ['id_pedido','id_usuario','id_estado','id_comercio','descripcion','fecha','validez','monto_total']