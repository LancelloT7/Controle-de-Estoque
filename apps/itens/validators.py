from django.core.exceptions import ValidationError

def validar_tamanho_imagem(file):
    limite_kb = 50  # 1 MB
    if file.size > limite_kb * 1024:
        raise ValidationError(f"O arquivo não pode ser maior que {limite_kb} KB")