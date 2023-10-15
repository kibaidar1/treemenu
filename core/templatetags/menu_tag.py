from django import template

from core.models import MenuModel
from django.shortcuts import get_object_or_404

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name: str = None):
    menu_slug = context.request.GET.get('slug')
    if menu_slug:
        current_menu = get_object_or_404(MenuModel, slug=menu_slug)
        current_menu_first_child = current_menu.child.first()
        path = get_all_parents(current_menu)
        path.append(current_menu)
        path.append(current_menu_first_child)
        menu = path.pop(0)
        target_menu = path[0]
    else:
        menu = get_object_or_404(MenuModel, name=name, parent=None)
        target_menu = None
        path = None

    menu_items = menu.child.all()
    return {'menu_items': menu_items, 'target_menu': target_menu, "path": path}


@register.inclusion_tag('menu.html')
def depth_menu(path: list = None):
    menu = path.pop(0)
    menu_items = menu.child.all()
    if path:
        target_menu = path[0]
    else:
        target_menu = None

    return {'menu_items': menu_items, 'target_menu': target_menu,
            'path': path}


def get_all_parents(menu: MenuModel) -> list:
    parents = []
    while menu.parent:
        menu = menu.parent
        parents.append(menu)
    parents.reverse()
    return parents


