from django import template
from webapp.models import Menu
register = template.Library()


def tree_struct(menu_items):
    return menu_items


@register.inclusion_tag('menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = tree_struct(Menu.objects.filter(visible=1))
    return {
        "menu_items": menu_items,
        "arr_x": [x.parent_id for x in menu_items]
    }