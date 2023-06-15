from django.contrib import admin
from apps.owner.models import Owner

# Register your models here.
#admin.site.register(Owner)
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'pais', 'vigente')  #aunque sea un solo elemento, se pone la coma
    list_filter = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')
    fields = ('nombre','edad')