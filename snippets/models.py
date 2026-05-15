from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Snippet(models.Model):
    LANGUAGE_CHOICES = (
        ("python", "Python"),
        ("java", "Java"),
        ("html", "HTML"),
        ("css", "CSS"),
        ("bash", "Bash/Shell"),
        ("sql", "SQL"),
    )

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Код сниппета")
    description = models.TextField(blank=True, verbose_name="Описание")
    language = models.CharField(
        max_length=50, choices=LANGUAGE_CHOICES, default="python", verbose_name="Язык"
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

    class Meta:
        verbose_name = "Сниппет"
        verbose_name_plural = "Сниппеты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


# Create your models here.
