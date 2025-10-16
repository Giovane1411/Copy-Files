from django.contrib import admin
from .models import Usuario, processo_administrativo

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'CNPJ', 'data_nascimento', 'telefone', 'endereco')
    search_fields = ('user__username', 'cpf', 'CNPJ')
    list_filter = ('data_nascimento',)
    
    
@admin.register(processo_administrativo)
class ProcessoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('protocolo', 'tipo', 'status', 'data_criacao', 'data_conclusao', 'user_fk')
    search_fields = ('protocolo', 'user_fk__username', 'status')
    list_filter = ('tipo', 'status', 'data_criacao')
