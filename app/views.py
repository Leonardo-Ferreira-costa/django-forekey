from django.views.generic import ListView, DetailView
from .models import Produto, Categoria

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'  # Caminho do template HTML
    context_object_name = 'produtos'         # Nome da variável que vai para o HTML
    paginate_by = 10                         # Paginação automática (10 por página)

    def get_queryset(self):
        """Otimiza a busca no banco trazendo a categoria junto (evita erro N+1)"""
        return Produto.objects.select_related('categoria').all()


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'
