from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Введите город проживания",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_METHOD = [
        ("cash", "Наличные"),
        ("transfer", "Перевод"),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    payment_amount = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name="Сумма оплаты"
    )
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD,
        default="cash",
        verbose_name="Способ оплаты",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
