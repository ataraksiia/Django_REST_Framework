# Generated by Django 5.1.6 on 2025-02-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="url_video",
            field=models.URLField(
                blank=True,
                help_text="Введите ссылку на видео",
                max_length=100,
                null=True,
                verbose_name="Ссылка",
            ),
        ),
    ]
