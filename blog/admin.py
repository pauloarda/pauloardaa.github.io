from django.contrib import admin
from .models import *


class InfoAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategory','date')

admin.site.register(Kategori)
admin.site.register(Doa)
admin.site.register(Info, InfoAdmin)