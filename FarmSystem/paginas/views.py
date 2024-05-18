from django.views.generic import TemplateView

# Criar as views aqui

class IndexView(TemplateView):
    template_name = "modelo.html"