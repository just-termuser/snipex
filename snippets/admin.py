from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import (
    ExportForm,
    ImportForm,
    SelectableFieldsExportForm,
)

from .models import Category, Language, Snippet, Tag


@admin.register(Category)
class CategoryAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm


@admin.register(Snippet)
class SnippetAdmin(ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm


@admin.register(Language)
class LanguageAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm


# Register your models here.
