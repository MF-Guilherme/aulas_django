from django import template

register = template.Library()

@register.filter(name='teste')
def teste(v1):
    if v1 == 1:
        return 'Usuário master do sistema'
    else:
        return 'usuario comum'