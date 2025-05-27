from django.contrib import admin
from .models import Item, Fabricante, NotaFiscal
from django.utils.html import format_html
from entrada_de_itens.models import Entrada
from saida_de_itens.models import Saida
import openpyxl
from django.http import HttpResponse

# Register your models here.
class EntradaInline(admin.TabularInline):
    model = Entrada
    extra = 0
    readonly_fields = ['nota_fiscal', 'responsavel', 'data', 'quantidade']
    can_delete = False
    verbose_name_plural = 'Entradas relacionadas'

class SaidaInline(admin.TabularInline):
    model = Saida
    extra = 0
    readonly_fields = ['responsavel', 'data', 'quantidade']
    can_delete = False
    verbose_name_plural = 'Saídas relacionadas'    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['fabricante__nome_do_fabricante', 'nome',]
    list_display = ['nome', 'partnumber', 'fabricante' ,'quantidade', 'disponivel', 'endereco' ,'preview']
    list_filter = ['disponivel', 'fabricante__nome_do_fabricante', 'nome', 'partnumber']
    inlines = [EntradaInline, SaidaInline]
    actions = ['exportar_para_excel']

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


    def exportar_para_excel(self, request, queryset):
        # Cria um workbook
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Estoque"

        # Cabeçalhos
        ws.append(['Nome', 'Fabricante', 'PartNumber', 'Quantidade', 'Endereço', 'Disponível'])

        # Dados
        for item in queryset:
            ws.append([
                item.nome,
                item.fabricante.nome_do_fabricante,
                item.partnumber,
                item.quantidade,
                item.endereco,
                "Sim" if item.disponivel else "Não"
            ])

        # Resposta HTTP
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename=relatorio_estoque.xlsx'
        wb.save(response)
        return response

    exportar_para_excel.short_description = "Exportar selecionados para Excel"

@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    search_fields = ['numero_de_nota']
    list_display = ['numero_de_nota']

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    search_fields = ['nome_do_fabricante']
    list_display = ['nome_do_fabricante']

