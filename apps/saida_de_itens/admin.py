from django.contrib import admin
from django.contrib import admin
from .models import Saida, Destinatario
import openpyxl
from openpyxl.styles import Font, Alignment
from django.http import HttpResponse
from datetime import datetime

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ['data', 'item', 'quantidade', 'responsavel', 'destino']
    list_filter  = ['data', 'item', 'responsavel', 'destino']
    search_fields = ['item__nome', 'destino']
    date_hierarchy = 'data'
    readonly_fields = ['responsavel']
    actions = ['exportar_saidas_para_excel']

    def exportar_saidas_para_excel(self, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Relatório de Saídas"

        # Cabeçalhos
        headers = ['Item', 'Quantidade', 'Responsável', 'Destinatário', 'Data']
        ws.append(headers)

        # Estilização do cabeçalho
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col)
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center')

        # Linhas de dados
        for saida in queryset:
            ws.append([
                saida.item.nome,
                saida.quantidade,
                saida.responsavel.username,
                saida.destino.destino if saida.destino else '',
                saida.data.strftime('%d/%m/%Y %H:%M'),
            ])

        # Ajustar largura das colunas automaticamente
        for column_cells in ws.columns:
            length = max(len(str(cell.value)) for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = length + 2

        # Nome do arquivo com data/hora
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"relatorio_saidas_{timestamp}.xlsx"

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = f'attachment; filename={filename}'
        wb.save(response)
        return response

    exportar_saidas_para_excel.short_description = "Gerar Relatório de Saídas (Excel)"

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Só define o responsável na criação
            obj.responsavel = request.user
        super().save_model(request, obj, form, change)
    
@admin.register(Destinatario)
class DestinatarioAdmin(admin.ModelAdmin):
   list_display = ['destino'] 
   list_filter = ['destino'] 
   search_fields = ['destino'] 

