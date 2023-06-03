from django.contrib import admin
from .models import Author, Blog, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
