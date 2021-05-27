from django.urls import path
from core.views import login, inicio, horacancelada, horaexitosa, proxatenciones, registro, resumensolicitud, tomarhora, vermishoras 




urlpatterns = [
    
    path('', login, name="login"),
    path('inicio/', inicio, name="inicio"),
    path('horacancelada/', horacancelada, name="horacancelada"),
    path('horaexitosa/', horaexitosa, name="horaexitosa"),
    path('proxatenciones/', proxatenciones, name="proxatenciones"),
    path('registro/', registro, name="registro"),
    path('resumensolicitud/', resumensolicitud, name="resumensolicitud"),
    path('tomarhora/', tomarhora, name="tomarhora"),
    path('vermishoras/', vermishoras, name="vermishoras"),
   
]