from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    # def get_count_lessons(self, course):
    #     return Lesson.objects.filter(course=course).count()

    def get_count_lessons(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ["id", "name", "img", "description", "lessons", "count_lessons"]
