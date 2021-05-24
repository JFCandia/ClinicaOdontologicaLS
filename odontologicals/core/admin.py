from django.contrib import admin
from .models import Boleta, Cargo, Categoria, Cliente, Comuna, Contacto, Empleado, Empresa
from .models import EspHora, Especialidad, Especialista, Horario, Informe
from .models import Moneda, OpedProduc, OrdenPedido, Permiso, Producto, Proveedor, Region
from .models import Rol, RolPermiso, Rubro, SitEconomica, Sucursal, TipoPago



# Register your models here.

admin.site.register(Boleta)
admin.site.register(Cargo)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Contacto)
admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(EspHora)
admin.site.register(Especialidad)
admin.site.register(Especialista)
admin.site.register(Horario)
admin.site.register(Informe)
admin.site.register(Moneda)
admin.site.register(OrdenPedido)
admin.site.register(Permiso)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Region)
admin.site.register(Rol)
admin.site.register(RolPermiso)
admin.site.register(Rubro)
admin.site.register(SitEconomica)
admin.site.register(Sucursal)
admin.site.register(TipoPago)
