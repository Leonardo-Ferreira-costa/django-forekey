from django.contrib import admin
from .models import Categoria, Produto

# Configuração simples para Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criado_em')
    search_fields = ('nome',)

# Configuração avançada para Produto (com filtros e busca)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'preco', 'estoque', 'criado_em')
    list_filter = ('categoria', 'criado_em')
    search_fields = ('nome', 'descricao')
    list_editable = ('preco', 'estoque') # Permite editar preço e estoque direto na listagem
