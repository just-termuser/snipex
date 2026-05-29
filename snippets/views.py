from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Snippet, Tag

def home(request):
    context = {
        "snippets": Snippet.objects.filter(is_public=True),
        "categories": Category.objects.all(),
        "current_category": None,
    }
    if request.headers.get('HX-Request'):
        return render(request, "snippets/partials/snippet_board.html", context)

    return render(request, "snippets/home.html", context)


def categories(request, category_id):
    context = {
        "snippets": Snippet.objects.filter(is_public=True, category__id=category_id),
        "categories": Category.objects.all(),
        "current_category": Category.objects.get(id=category_id).name,
    }
    if request.headers.get('HX-Request'):
        return render(request, "snippets/partials/snippet_board.html", context)

    return render(request, "snippets/home.html", context)

def htmx_test(request):
    tags = Tag.objects.all()
    return render(request, "snippets/partials/tags-list.html", {'tags': tags})
