from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Pais(models.Model):
    id_pais = models.IntegerField('id_pais', primary_key=True, max_length=4, unique=True)
    nombre = models.CharField('nombre', max_length=1000, null=False)

class Ciudad(models.Model):
   # id_pais = models.ForeignKey(models.Pais, db_column='id_pais')
    id_ciudad = models.IntegerField('id_ciudad', primary_key=True, max_length=4, unique=True)
    nombre = models.CharField('nombre', max_length=1000, null=False)

class Barrio(models.Model):
    #id_pais = models.ForeignKey(models.Pais, 'id_pais')
    #id_ciudad = models.ForeignKey(models.Ciudad, 'id_ciudad')
    id_barrio = models.IntegerField('id_barrio', primary_key=True, max_length=4, unique=True)
    nombre = models.CharField('nombre', max_length=1000, null=False)

"""class Direccion(Model):
    id_entidad = ForeignKey(Entidad, 'id_entidad')
    id_pais = ForeignKey(Pais, 'id_pais')
    id_ciudad = ForeignKey(Ciudad, 'id_ciudad')
    id_barrio = ForeignKey(Barrio, 'id_barrio')
    calle = CharField('calle', max_length=100, null=False)
    numero = CharField('numero', max_length=6, null=False)
    piso = CharField('piso', max_length=100, null=True)
    departamento = CharField('departamento', max_length=10, null=True)"""

class Entidad(models.Model):
    id_entidad = models.IntegerField('id_entidad', primary_key=True, max_length=4, unique=True)
   # id_comercio = models.ForeignKey(models.Comercio, 'id_comercio')
    #id_pais = models.ForeignKey(models.Pais, 'id_pais')
    #id_ciudad = models.ForeignKey(models.Ciudad, 'id_ciudad')
    #id_barrio = models.ForeignKey(models.Barrio, 'id_barrio')
    nombre = models.CharField('nombre', max_length=300, null=False)
    iibb = models.BigIntegerField('iibb', max_length=15, null=False)
    calle = models.CharField('calle', max_length=100, null=False)
    numero = models.CharField('numero', max_length=6, null=False)
    piso = models.CharField('piso', max_length=100, null=True)
    departamento = models.CharField('departamento', max_length=10, null=True)

class Comercio(models.Model):
    id_comercio = models.IntegerField('id_comercio', primary_key=True, max_length=4, unique=True)
   # id_entidad = models.ForeignKey(models.Entidad, 'id_entidad')
   # id_pedido = models.ForeignKey(models.Pedido, 'id_pedido')
   # id_producto = models.ForeignKey(models.Producto, 'id_producto')
    cuit = models.BigIntegerField('cuit', max_length=11, null=False, unique=True)
    disponible = models.BooleanField('disponible', null=False)
    razon_social = models.CharField('razon_social', max_length=100, null=False)
    nombre = models.CharField('nombre', max_length=300, null=False)

class Producto(models.Model):
    id_producto = models.IntegerField('id_producto', primary_key=True, max_length=4, unique=True)
   # id_comercio = models.ForeignKey(models.Comercio, 'id_comercio')
    tipo = models.CharField('tipo', max_length=100, null=False)
    precio = models.IntegerField('precio', max_length=8, null=False)
    descripcion = models.CharField('descripcion', max_length=100, null=False)

class Pedido(models.Model):
    id_pedido = models.IntegerField('id_pedido', primary_key=True, max_length=4, unique=True)
   # id_usuario = models.ForeignKey(models.Usuario, 'id_usuario')
   # id_estado = models.ForeignKey(models.Estado, 'id_estado')
    #id_comercio = models.ForeignKey(models.Comercio, 'id_comercio')
    descripcion = models.CharField('descripcion', max_length=100, null=False)
    fecha = models.DateField('fecha', null=False)
    validez = models.DateField('validez', null=False)
    monto_total = models.IntegerField('monto_total', max_length=8, null=False)

class Estado(models.Model):
    id_estado = models.IntegerField('id_estado', primary_key=True, max_length=2, unique=True)
    descripcion = models.CharField('descripcion', max_length=100, null=False)

class Transaccion(models.Model):
    id_transaccion = models.IntegerField('id_transaccion', primary_key=True, max_length=2, unique=True)
   # id_estado = models.ForeignKey(Estado, 'id_estado')
   # id_pedido = models.ForeignKey(Pedido, 'id_pedido')
   # id_usuario = models.ForeignKey(Usuario, 'id_usuario')
    medio_pago = models.CharField('medio_pago', max_length=50, null=False)
    monto = models.IntegerField('monto', max_length=8, null=False)

class Pago(models.Model):
    id_pago = models.IntegerField('id_pago', primary_key=True, max_length=2, unique=True)
    #id_transaccion = models.ForeignKey(models.Transaccion, 'id_transaccion')
    #id_usuario = models.ForeignKey(models.Usuario, 'id_usuario')
    monto = models.IntegerField('monto', max_length=8, null=False)
    fecha_operacion = models.DateField('fecha_operacion', null=False)

class Usuario(models.Model):
    id_usuario = models.IntegerField('id_usuario', primary_key=True, max_length=2, unique=True)
    mail = models.CharField('mail', max_length=80, null=False)
    fecha_nacimiento = models.DateField('fecha_nacimiento', null=False)
    contraseña = models.CharField('contraseña', max_length=50, null=False)
    nacionalidad = models.CharField('nacionalidad', max_length=50, null=False)