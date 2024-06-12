from django.contrib import admin

from reviews.constants import ITEMS_PER_ADMIN_PAGE
from reviews.models import Category, Comment, Genre, Review, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category', 'description')
    list_display_links = ('name',)
    list_filter = ('category', 'genre', 'year')
    list_per_page = ITEMS_PER_ADMIN_PAGE
    search_fields = ('name',)
    filter_horizontal = ('genre',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'pub_date', 'author', 'score')
    list_display_links = ('title',)
    list_filter = ('pub_date', 'score')
    list_per_page = ITEMS_PER_ADMIN_PAGE
    search_field = ('author', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'pub_date', 'review')
    list_display_links = ('text',)
    list_filter = ('pub_date',)
    list_per_page = ITEMS_PER_ADMIN_PAGE
    search_field = ('author', 'review')
