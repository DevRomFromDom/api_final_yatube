from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Адрес страницы группы')
    description = models.TextField(verbose_name='Описание группы')
    title = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        blank=False, verbose_name='текст поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, verbose_name='Картинка')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа',
        related_name='posts')

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост')
    text = models.TextField(blank=False,
                            verbose_name='текст комментария',)
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        ordering = ('-created',)

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name="unique_follow")
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
