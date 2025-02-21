from django.urls import path, include
from rest_framework.routers import SimpleRouter
from lms.views import (
    CourseViewSet,
    LessonListAPIView,
    LessonCreateAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
)
from lms.apps import LmsConfig

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lessons/<int:pk>/delete/",
        LessonDestroyAPIView.as_view(),
        name="lesson_delete",
    ),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
]

urlpatterns += router.urls
