from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Category, Language, Snippet, Tag


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Snippet)
class SnippetAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    pass


# Register your models here.
