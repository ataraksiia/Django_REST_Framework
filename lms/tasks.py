from datetime import timedelta, timezone

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from lms.models import Course, Subscription
from users.models import User


@shared_task
def course_update_mailing(course_pk):
    course = Course.objects.filter(pk=course_pk).first()
    users = User.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(
            course=course_pk, user=user.pk
        ).first()
        if subscription:
            send_mail(
                subject=f"Обновление курса!",
                message=f"Новые материалы по курсу '{course.name}'",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )


@shared_task
def check_last_login():
    today = timezone.now().date()
    inactive_date = today - timedelta(days=30)

    users = User.objects.filter(
        is_active=True,
        is_staff=False,
        is_superuser=False,
        last_login__isnull=False,
        last_login__lt=inactive_date,
    ).update(is_active=False)

    for user in users:
        if timezone.now() - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(
                f"Пользователь {user.email} заблокирован, так как не заходил больше месяца"
            )
        else:
            print(f"Пользователь {user.email} активен")
