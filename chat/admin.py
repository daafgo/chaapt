from django.contrib import admin
from .models import *
# Register your models here.
class MensajeAdmin(admin.ModelAdmin):
    list_filter = ["conversacion"]
    list_display = ["conversacion"]


admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Conversacion)