from django.contrib import admin
from . models import Darbuotojas,Darbo_laiko_irasai,Darbo_zona_sandelyje, Darbo_grafikas_planas,Notes,Krautuvas

# Register your models here.
admin.site.register(Darbuotojas)
admin.site.register(Darbo_laiko_irasai)
admin.site.register(Darbo_zona_sandelyje)
admin.site.register(Darbo_grafikas_planas)
admin.site.register(Notes)
admin.site.register(Krautuvas)
