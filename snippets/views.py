from django.shortcuts import render

from .models import Category, Snippet


# Create your views here.
def home(request):
    context = {
        "snippets": Snippet.objects.filter(is_public=True),
        "categories": Category.objects.all(),
        "current_category": None,
    }
    return render(request, "snippets/home.html", context)


def categories(request, category_name):
    context = {
        "snippets": Snippet.objects.filter(
            is_public=True, category__name=category_name
        ),
        "categories": Category.objects.all(),
        "current_category": category_name,
    }
    return render(request, "snippets/home.html", context)
