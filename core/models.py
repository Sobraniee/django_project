from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Unpublished', 'Unpublished')
    )
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('Заголовок', max_length=100, null=True, blank=True)
    description = models.TextField('Описание', null=True)
    photo = models.ImageField('Фотография', upload_to='photo_post/', null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField('Статус публикации', max_length=200, choices=STATUS_CHOICES)
    rating = models.PositiveSmallIntegerField('Рейтинг', choices=RATING_CHOICES)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.name} - {self.rating} - {self.created_date}'


class Category(models.Model):
    post = models.ManyToManyField(
        Post,
        related_name='categories',
        verbose_name='Post')
    name = models.CharField('Category name', max_length=50, null=True)
    description = models.TextField('Description', null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users_comment',
        verbose_name='comment'
        )
    comment_text = models.CharField('txt', max_length=144)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comment_to_post',
                             verbose_name='Post')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user} : {self.comment_text}'
