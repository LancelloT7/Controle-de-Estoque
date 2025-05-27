from django.contrib import admin
from .models import Entrada
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime

# Register your models here.

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    
    list_display = ['data', 'item', 'quantidade', 'responsavel','nota_fiscal__numero_de_nota']
    list_filter = ['data', 'item', 'quantidade', 'responsavel','nota_fiscal__numero_de_nota']
    readonly_fields = ['responsavel']
    date_hierarchy = 'data'    
    actions = ['exportar_entradas_para_excel']

    def exportar_entradas_para_excel(self, request, queryset):
        wb = Workbook()
        ws = wb.active
        ws.title = "Relatório de Entradas"

        # Cabeçalhos
        headers = ['Item', 'Quantidade', 'Nota Fiscal', 'Responsável', 'Data']
        ws.append(headers)

        # Estilização dos cabeçalhos
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col)
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center')

        # Preenchimento das linhas com os dados
        for entrada in queryset:
            ws.append([
                entrada.item.nome,
                entrada.quantidade,
                entrada.nota_fiscal.numero_de_nota,
                entrada.responsavel.username,
                entrada.data.strftime('%d/%m/%Y %H:%M'),
            ])

        # Ajustar largura das colunas automaticamente
        for column_cells in ws.columns:
            length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = length + 2

        # Nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"relatorio_entradas_{timestamp}.xlsx"

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = f'attachment; filename={filename}'
        wb.save(response)
        return response

        exportar_entradas_para_excel.short_description = "Gerar Relatório de Entradas (Excel)"

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Só define o responsável na criação
            obj.responsavel = request.user
        super().save_model(request, obj, form, change)