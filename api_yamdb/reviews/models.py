from django.contrib.auth import get_user_model
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    RegexValidator)
from django.db import models

User = get_user_model()
slug_validator = RegexValidator(regex=r'^[-a-zA-Z0-9_]+$')


class GenreCategory(models.Model):
    name = models.CharField('Категория', max_length=256)
    slug = models.SlugField(
        'Slug', unique=True, validators=(slug_validator,)
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(GenreCategory):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(GenreCategory):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField('Название', max_length=256)
    year = models.PositiveSmallIntegerField('Год выпуска')
    description = models.TextField('Описание', blank=True)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='titles'
    )

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class ReviewComment(models.Model):
    text = models.TextField('Текст отзыва')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        abstract = True


class Review(ReviewComment):
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=(
            MinValueValidator(
                1, message='Оценка - целое число в диапазоне от 1 до 10'
            ),
            MaxValueValidator(
                10, message='Оценка - целое число в диапазоне от 1 до 10'
            ),
        )
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_review'
            )
        ]


class Comment(ReviewComment):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
