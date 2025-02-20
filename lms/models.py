from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Введите название курса",
    )
    img = models.ImageField(
        upload_to="lms/courses/img",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["name", "description"]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Введите название урока",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание урока",
    )
    img = models.ImageField(
        upload_to="lms/lessons/img",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью курса",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Название",
        help_text="Введите название курса",
        null=True,
        blank=True,
        related_name="lessons",
    )

    url_video = models.URLField(
        max_length=100,
        verbose_name="Ссылка",
        help_text="Введите ссылку на видео",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["course"]

    def __str__(self):
        return self.name
