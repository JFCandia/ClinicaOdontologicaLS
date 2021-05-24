# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Boleta(models.Model):
    id_boleta = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    monto_total = models.BigIntegerField()
    id_emp = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='id_emp')
    id_tipo_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tipo_pago')
    id_esphora = models.ForeignKey('EspHora', models.DO_NOTHING, db_column='id_esphora')
    
    class Meta:
        managed = False
        db_table = 'boleta'

class Cargo(models.Model):
    id_cargo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'cargo'

class Categoria(models.Model):
    id_categoria = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=35)
    
    class Meta:
        managed = False
        db_table = 'categoria'

class Cliente(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    rut = models.BigIntegerField()
    dv = models.BigIntegerField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    usuario = models.CharField(max_length=8)
    contrasena = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    email = models.CharField(max_length=50)
    id_sit_econ = models.ForeignKey('SitEconomica', models.DO_NOTHING, db_column='id_sit_econ')
    
    class Meta:
        managed = False
        db_table = 'cliente'

class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')
    
    class Meta:
        managed = False
        db_table = 'comuna'

class Contacto(models.Model):
    id_contacto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    email = models.CharField(max_length=50, blank=True, null=True)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    
    class Meta:
        managed = False
        db_table = 'contacto'

class Empleado(models.Model):
    id_emp = models.BigIntegerField(primary_key=True)
    rut = models.BigIntegerField()
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    id_sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='id_sucursal')
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='id_rol')
    usuario = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=15)
    
    class Meta:
        managed = False
        db_table = 'empleado'

class Empresa(models.Model):
    id_empresa = models.BigIntegerField(primary_key=True)
    razon_social = models.CharField(max_length=200)
    rut = models.BigIntegerField()
    dv = models.CharField(max_length=1)
    
    class Meta:
        managed = False
        db_table = 'empresa'

class EspHora(models.Model):
    id_esphora = models.BigIntegerField(primary_key=True)
    disponible = models.CharField(max_length=1)
    id_esp = models.ForeignKey('Especialista', models.DO_NOTHING, db_column='id_esp')
    id_horario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='id_horario')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'esp_hora'

class Especialidad(models.Model):
    id_especialidad = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'especialidad'

class Especialista(models.Model):
    id_esp = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='id_especialidad')
    
    class Meta:
        managed = False
        db_table = 'especialista'

class Horario(models.Model):
    id_horario = models.BigIntegerField(primary_key=True)
    dia = models.CharField(max_length=2)
    hora_ini = models.CharField(max_length=5)
    hora_fin = models.CharField(max_length=5)
    
    class Meta:
        managed = False
        db_table = 'horario'

class Informe(models.Model):
    id_informe = models.BigIntegerField(primary_key=True)
    fecha_emision = models.DateField()
    formato = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_emp')
    
    class Meta:
        managed = False
        db_table = 'informe'

class Moneda(models.Model):
    id_moneda = models.BigIntegerField(primary_key=True)
    abreviacion = models.CharField(max_length=3)
    nombre = models.CharField(max_length=20)
    valor_clp = models.BigIntegerField()
    
    class Meta:
        managed = False
        db_table = 'moneda'

class OpedProduc(models.Model):
    id_op_prod = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    precio_clp = models.BigIntegerField()
    id_opedido = models.ForeignKey('OrdenPedido', models.DO_NOTHING, db_column='id_opedido')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    
    class Meta:
        managed = False
        db_table = 'oped_produc'

class OrdenPedido(models.Model):
    id_opedido = models.BigIntegerField(primary_key=True)
    fecha_creacion = models.DateField()
    recepcionado = models.CharField(max_length=1, blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_emp')
    
    class Meta:
        managed = False
        db_table = 'orden_pedido'

class Permiso(models.Model):
    id_permiso = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        managed = False
        db_table = 'permiso'

class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    stock_real = models.BigIntegerField()
    stock_critico = models.BigIntegerField()
    precio_costo = models.BigIntegerField()
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')
    
    class Meta:
        managed = False
        db_table = 'producto'

class Proveedor(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    rut = models.BigIntegerField()
    dv = models.CharField(max_length=1)
    razon_social = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    id_rubro = models.ForeignKey('Rubro', models.DO_NOTHING, db_column='id_rubro')
    
    class Meta:
        managed = False
        db_table = 'proveedor'

class Region(models.Model):
    id_region = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        managed = False
        db_table = 'region'

class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    class Meta:
        managed = False
        db_table = 'rol'

class RolPermiso(models.Model):
    id_rol_per = models.BigIntegerField(primary_key=True)
    per_activo = models.CharField(max_length=1)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')
    id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='id_permiso')
    
    class Meta:
        managed = False
        db_table = 'rol_permiso'

class Rubro(models.Model):
    id_rubro = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'rubro'

class SitEconomica(models.Model):
    id_sit_econ = models.BigIntegerField(primary_key=True)
    ingreso_min = models.BigIntegerField()
    ingreso_max = models.BigIntegerField()
    
    class Meta:
        managed = False
        db_table = 'sit_economica'

class Sucursal(models.Model):
    id_sucursal = models.BigIntegerField(primary_key=True)
    direccion = models.CharField(max_length=200)
    id_encargado = models.BigIntegerField(blank=True, null=True)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')
    
    class Meta:
        managed = False
        db_table = 'sucursal'

class TipoPago(models.Model):
    id_tipo_pago = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    id_moneda = models.ForeignKey(Moneda, models.DO_NOTHING, db_column='id_moneda')
    
    class Meta:
        managed = False
        db_table = 'tipo_pago'
