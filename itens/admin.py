from django.contrib import admin
from .models import Item, Fabricante
from django.utils.html import format_html

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['fabricante__nome', 'nome']
    list_display = ['nome', 'partnumber', 'fabricante' ,'quantidade', 'disponivel', 'endereco' ,'preview']
    readonly_fields = ['quantidade']
    list_filter = ['disponivel', 'fabricante__nome', 'nome', 'partnumber']
    

    def preview(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px; object-fit: contain;" />',
                obj.img.url
            )
        return "-"
    preview.short_description = 'Imagem'
    def has_change_permission(self, request, obj=None):
        # Permite acesso à página de edição
        return True

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Funcionarios').exists():
            # Se for funcionário, todos os campos são readonly, exceto "endereco"
            all_fields = [field.name for field in self.model._meta.fields]
            return [f for f in all_fields if f != 'endereco']
        return super().get_readonly_fields(request, obj)


