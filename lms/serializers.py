from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from lms.validators import validate_youtube_links
from .models import Course, Lesson, Subscription


class LessonSerializer(ModelSerializer):
    url_video = serializers.URLField(validators=[validate_youtube_links])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_lessons(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ["id", "name", "img", "description", "lessons", "count_lessons"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "course"]
        read_only_fields = ["user", "course"]
