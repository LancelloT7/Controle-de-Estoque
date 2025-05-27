from django.contrib import admin
from .models import Entrada

# Register your models here.

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    
    list_display = ['data', 'item', 'quantidade', 'responsavel','nota_fiscal__numero_de_nota']
    list_filter = ['data', 'item', 'quantidade', 'responsavel','nota_fiscal__numero_de_nota']
    readonly_fields = ['responsavel']
    date_hierarchy = 'data'    

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Só define o responsável na criação
            obj.responsavel = request.user
        super().save_model(request, obj, form, change)