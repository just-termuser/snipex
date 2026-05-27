from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Snippet, Tag


# Create your views here.
def home(request):
    context = {
        "snippets": Snippet.objects.filter(is_public=True),
        "categories": Category.objects.all(),
        "current_category": None,
    }
    return render(request, "snippets/home.html", context)


def categories(request, category_id):
    context = {
        "snippets": Snippet.objects.filter(
            is_public=True, category__id=category_id
        ),
        "categories": Category.objects.all(),
        "current_category": Category.objects.get(id=category_id).name,
    }
    return render(request, "snippets/home.html", context)

def htmx_test(request):
    tags = Tag.objects.all()
    return render(request, "snippets/partials/tags-list.html", {'tags': tags})
