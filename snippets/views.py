from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Category, Snippet, Tag, Language

def home(request):
    context = {
        "snippets": Snippet.objects.filter(is_public=True),
        "categories": Category.objects.all(),
        "current_category": None,
    }
    if request.headers.get('HX-Request'):
        return render(request, "snippets/partials/snippets_board.html", context)

    return render(request, "snippets/home.html", context)


def categories(request, category_id):
    context = {
        "snippets": Snippet.objects.filter(is_public=True, category__id=category_id),
        "categories": Category.objects.all(),
        "current_category": Category.objects.get(id=category_id).name,
    }
    if request.headers.get('HX-Request'):
        return render(request, "snippets/partials/snippets_board.html", context)

    return render(request, "snippets/home.html", context)

def htmx_test(request):
    tags = Tag.objects.all()
    return render(request, "snippets/partials/tags-list.html", {'tags': tags})


@login_required
def add_snippet(request):
    context = {
        "categories": Category.objects.all(),
        "languages": Language.objects.all(),
    }
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category_id = request.POST.get("category")
        language_id = request.POST.get("language")
        is_public = request.POST.get("isPublic") == "on"
        tags_string = request.POST.get("tags", "")
        new_snippet = Snippet.objects.create(
            title=title,
            content=content,
            category_id=category_id,
            language_id=language_id,
            is_public=is_public,
            user=request.user
        )
        if tags_string:
            tag_names = tags_string.split(',')
            for name in tag_names:
                name = name.strip()
                if name:
                    tag_obj, created = Tag.objects.get_or_create(name=name)
                    # привязка тега к сниппету
                    new_snippet.tags.add(tag_obj)
        return redirect("home")

    return render(request, "snippets/add_snippet.html", context)

@login_required
def toggle_favorite(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)

    if request.user in snippet.favorites.all():
        snippet.favorites.remove(request.user)
    else:
        snippet.favorites.add(request.user)

    return render(request, "snippets/partials/toggle_button.html", {"snippet": snippet})

@login_required
def favorites(request):
    context = {
        "snippets": Snippet.objects.filter(favorites=request.user),
    }
    return render(request, "snippets/favorites.html", context)
