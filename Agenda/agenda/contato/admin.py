from django.contrib import admin
from agenda.contato.models import Contato

class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = ['contato_nome', 'contato_email', 'contato_favorito']
    list_filter = ['contato_sexo', 'contato_estato_civil']
    search_fields = ['contato_nome']
    save_on_top = True
admin.site.register(Contato, ContatoAdmin)
