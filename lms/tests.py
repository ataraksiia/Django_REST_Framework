from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from lms.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(name="Python-разработчик")
        self.lesson = Lesson.objects.create(
            name="Погружение в Python-разработку",
            course=self.course,
            url_video="https://www.youtube.com/watch?v=xTlbnxr62Vo",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            data.get("name"),
            self.lesson.name,
        )

    def test_lesson_create(self):
        data = {
            "name": "32.1 Валидаторы, пагинация и тесты",
            "url_video": "https://www.youtube.com/watch?v=xTlbnxr62Vo",
        }
        response = self.client.post("/lms/lessons/create/", data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(Lesson.objects.count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "Новое имя",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            data.get("name"),
            "Новое имя",
        )

    def test_lesson_delete(self):
        url = reverse("lms:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_lessons_list(self):
        url = reverse("lms:lessons_list")
        response = self.client.get(url)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "url_video": self.lesson.url_video,
                    "name": self.lesson.name,
                    "description": None,
                    "img": None,
                    "course": self.course.id,
                    "owner": self.user.id,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(name="Python-разработчик")
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        data = {"course_id": self.course.id}
        response = self.client.post("/lms/subscribe/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        subscription = Subscription.objects.first()
        self.assertEqual(subscription.user, self.user)
        self.assertEqual(subscription.course, self.course)

    def test_unsubscribe_from_course(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {"course_id": self.course.id}
        response = self.client.post("/lms/subscribe/", data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)
