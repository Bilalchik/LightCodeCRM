from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from datetime import datetime


class Role(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Employee(models.Model):
    full_name = models.CharField(max_length=123, verbose_name='ФИО')
    image = models.ImageField(upload_to='media/image', verbose_name='Фотография', blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name='Роль')
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, verbose_name='Зарплата')
    description = models.TextField(verbose_name=('Описание для Лэндинга'), blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return self.full_name

    def cover_image(self):
        return format_html(f'<img src="{self.image.url}" style="width:100px;height:150px;" />')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Currency(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class PaymentMethod(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'


class Student(models.Model):
    full_name = models.CharField(max_length=80, verbose_name=('ФИО'))
    phone_number = PhoneNumberField(verbose_name=('Номер телефона'))
    course = models.ForeignKey('landing.Course', on_delete=models.PROTECT, verbose_name='Курс', related_name='student')
    tariff = models.CharField(max_length=80, verbose_name='Формат обучения', blank=True, null=True)
    certificate = models.PositiveSmallIntegerField(default=0, verbose_name='Сертификат')
    url = models.URLField(blank=True, null=True)
    time = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Утро'),
            (2, 'День'),
            (3, 'Вечер'),
            (4, 'Ночь'),
        ),
        verbose_name='Время обучения',
        blank=True,
        null=True
    )
    total_payment = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00,
        verbose_name='Общая оплата',
        blank=True,
        null=True)
    last_payment_date = models.DateTimeField(verbose_name='Дата последней оплаты', blank=True, null=True)
    is_graduate = models.BooleanField(default=False, verbose_name='Выпускник')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Expense(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    value = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, verbose_name='Цена')
    flow_type = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Постоянный'),
            (2, 'Одноразовый'),
            (3, 'Сотрудник'),
        ),
        verbose_name='Тип расхода'
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'


class Income(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name='Студент')
    course = models.ForeignKey('landing.Course', on_delete=models.PROTECT, verbose_name='Курс')
    value = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, verbose_name='Цена')
    payment_method = models.ForeignKey(
                PaymentMethod,
                on_delete=models.PROTECT,
                verbose_name='Способ оплаты',
                related_name='incomes',
            )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return str(self.student)

    def save(self, *args, **kwargs):
        student = self.student
        student.total_payment += self.value
        student.last_payment_date = datetime.now()
        student.save()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Доходы'
        verbose_name_plural = 'Доходы'


# class StudentPayment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name='Студент')
#     value = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, verbose_name='Оплата')
#     currency = models.ManyToManyField(Currency, verbose_name='Валюта', related_name='student')
#     payment_method = models.ManyToManyField(
#         PaymentMethod,
#         verbose_name='Способ оплаты',
#         related_name='student',
#     )
#     created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
#
#     def save(self, *args, **kwargs):
#         student = Student.objects.get(id=self.student.id)
#         if student:
#             ...
#             # student.update(total_payment=)
#         Income.objects.create(
#             title=self.student,
#             value=self.value
#         )
#         student = self.student
#         student.total_payment += self.value
#         student.last_payment_date = datetime.now()
#         student.save()
#
#         return super().save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.student)
#
#     def currency_names(self):
#         return " %s" % (", ".join([currencies.title for currencies in self.currency.all()]))
#
#     def payment_method_names(self):
#         return " %s" % (", ".join([payment_methods.title for payment_methods in self.payment_method.all()]))
#
#     class Meta:
#         verbose_name = 'Оплата студента'
#         verbose_name_plural = 'Оплата студентов'


class Lead(models.Model):
    full_name = models.CharField(max_length=80, verbose_name=('ФИО'))
    phone_number = PhoneNumberField(verbose_name=('Номер телефона'))
    course = models.ForeignKey('landing.Course', on_delete=models.PROTECT, verbose_name=('Курс'), blank=True, null=True)
    description = models.TextField(verbose_name=('Описание'), blank=True, null=True)
    is_add = models.BooleanField(default=False, verbose_name=('Добавить'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=('Дата создания'))

    def __str__(self):
        return self.full_name

    def clean(self):
        if self.is_add == True:
            if not self.course:
                raise ValidationError({'course': 'На какой курс хочет записаться Лид'})
            elif self.is_add == True:
                Student.objects.create(
                    full_name=self.full_name,
                    phone_number=self.phone_number,
                    course=self.course,
                )
        return super(Lead, self).clean()

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'




