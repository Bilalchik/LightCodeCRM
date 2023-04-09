from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Topic(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    slug = models.SlugField()
    parent_topic = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Главная тема')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        full_path = [self.title]
        k = self.parent_topic
        while k is not None:
            full_path.append(k.title)
            k = k.parent_topic
        return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    title = models.CharField(max_length=225, verbose_name='Название')
    slug = models.SlugField()
    body = models.TextField(verbose_name='Контент')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user} -> {self.topic}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    body = models.TextField(verbose_name='Комментарий')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родительский комментарий')

    def __str__(self):
        if self.parent_comment is None:
            return f"{self.user} -> {self.question}"
        else:
            return f"{self.user} -> {self.parent_comment}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class AccessRights(models.Model):
    moderator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Модератор', related_name='moderator')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user')
    start_date = models.DateField(auto_now_add=True, verbose_name='Начало даты бана')
    end_date = models.DateField(verbose_name='Конец даты бана')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return str(self.user)

    def clean(self):
        moderator = self.moderator
        user = self.user
        if moderator.is_admin != True:
            if moderator.status != 6 :
                raise ValidationError({'moderator': 'Забанить может только Модератор или Админ'})
            raise ValidationError({'moderator': 'Забанить может только Модератор или Админ'})
        elif moderator == user:
            raise ValidationError({'user': 'Вы не можете забанить самого себя'})
        return super().clean()

    class Meta:
        verbose_name = 'Права доступа'
        verbose_name_plural = 'Права доступа'
        unique_together = ['user']





