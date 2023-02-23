from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class StudyingTime(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Время обучения'
        verbose_name_plural = 'Время обучения'


class CourseForLanding(models.Model):
    title = models.CharField(max_length=123, verbose_name=('Название'))
    slug = models.SlugField()
    cover = models.ImageField(upload_to='media/image/', verbose_name=('Обложка'))
    description = models.TextField(verbose_name=('Описание о языке'))
    studying_time = models.ManyToManyField(StudyingTime, verbose_name='Время обучения')
    format = models.ManyToManyField('srm.LearningFormat', verbose_name='Формат обучения')
    additional_info = models.TextField(verbose_name='Информация о курсе', blank=True, null=True)
    teacher = models.ForeignKey('srm.Employee', on_delete=models.PROTECT, verbose_name='Ментор')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=('Дата создания'))
    is_active = models.BooleanField(default=True, verbose_name=('Активен'))

    def studying_time_names(self):
        return " %s" % (", ".join([formats.title for formats in self.studying_time.all()]))

    def format_names(self):
        return " %s" % (", ".join([formats.title for formats in self.format.all()]))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс для Лэндинга'
        verbose_name_plural = 'Курс для Лэндинга'


class Review(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя')
    direction = models.CharField(max_length=50, verbose_name='Направление')
    description = models.TextField(verbose_name=('Описание'), max_length=515)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=('Дата создания'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'



