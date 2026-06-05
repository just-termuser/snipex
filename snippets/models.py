from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    icon = models.CharField(max_length=120, verbose_name="Ссылка на иконку", blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name="Язык программирования")

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя тега")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Snippet(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Код сниппета")
    description = models.TextField(blank=True, verbose_name="Описание")
    language = models.ForeignKey(
        Language, on_delete=models.PROTECT, related_name="snippets", verbose_name="Язык"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="snippets",
        verbose_name="Категория",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="snippets", verbose_name="Автор"
    )

    is_public = models.BooleanField(default=False, verbose_name="Сделать публичным?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    tags = models.ManyToManyField(
        Tag, blank=True, related_name="snippets", verbose_name="Теги"
    )
    favorites = models.ManyToManyField(User, related_name='favorite_snippets', blank=True, verbose_name="В избранном у")


    class Meta:
        verbose_name = "Сниппет"
        verbose_name_plural = "Сниппеты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
