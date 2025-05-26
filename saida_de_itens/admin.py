from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Saida

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ['data', 'item', 'quantidade', 'responsavel']
    list_filter  = ['data', 'item', 'responsavel']
    search_fields = ['item__nome']
    date_hierarchy = 'data'
    readonly_fields = ['responsavel']

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Só define o responsável na criação
            obj.responsavel = request.user
        super().save_model(request, obj, form, change)
    
        
