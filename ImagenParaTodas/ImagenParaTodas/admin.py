from django.contrib import admin
from  .models import * #importamos el archivo models

admin.site.register(Tip)

admin.site.register(Cuerpo)

admin.site.register(Vestido)
