from django import template

register = template.Library()

@register.simple_tag
def break_loop():
    try:
        raise StopIteration
    except StopIteration:
        raise template.TemplateSyntaxError("Тег 'break_loop' столкнулся с ошибкой.")