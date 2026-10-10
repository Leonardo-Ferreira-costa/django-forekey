import random
from django.core.management.base import BaseCommand
from app.models import Categoria, Produto  # Importando do seu app 'app'

class Command(BaseCommand):  # O "C" maiúsculo aqui é obrigatório!
    help = 'Popula o banco de dados com categorias e produtos fictícios.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Iniciando o povoamento do banco...'))

        # 1. Criar Categorias
        categorias_nomes = ['Eletrônicos', 'Roupas', 'Livros', 'Esportes']
        categorias_objetos = []

        for nome in categorias_nomes:
            categoria, _ = Categoria.objects.get_or_create(
                nome=nome,
                defaults={'descricao': f'Produtos da categoria {nome}.'}
            )
            categorias_objetos.append(categoria)

        # 2. Criar Produtos
        produtos_exemplos = ['Modelo Standard', 'Versão Premium', 'Edição Limitada']
        total_criados = 0

        for categoria in categorias_objetos:
            for item in produtos_exemplos:
                nome_produto = f"{categoria.nome} - {item}"
                
                produto, created = Produto.objects.get_or_create(
                    nome=nome_produto,
                    categoria=categoria,
                    defaults={
                        'preco': round(random.uniform(29.90, 899.90), 2),
                        'estoque': random.randint(5, 40),
                        'descricao': f'Descrição automática para o produto {nome_produto}.'
                    }
                )
                if created:
                    total_criados += 1

        self.stdout.write(self.style.SUCCESS(f'Sucesso! Banco populado com {total_criados} novos produtos.'))
