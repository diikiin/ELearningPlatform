# Register your models here.
from django.contrib import admin

from elearn.models import (
    User, Category, Course, Enrollment, Lesson, Review, Payment, Quiz, QuizQuestion, UserProgress
)


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_student', 'is_instructor')
    search_fields = ('username', 'is_student', 'is_instructor')


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title',)


@admin.register(Enrollment)
class Enrollment(admin.ModelAdmin):
    list_display = ('user_id', 'course_id', 'enrollment_date', 'status')
    search_fields = ('user__username', 'course__title')


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('title', 'course_id')
    search_fields = ('title', 'course__title')


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('course_id', 'user_id', 'rating', 'created_at')
    search_fields = ('course__title', 'user__username')


@admin.register(Payment)
class Payment(admin.ModelAdmin):
    list_display = ('user_id', 'amount', 'payment_date', 'status')
    search_fields = ('user__username', 'status')


@admin.register(Quiz)
class Quiz(admin.ModelAdmin):
    list_display = ('course_id', 'title', 'total_marks')
    search_fields = ('course__title', 'title')


@admin.register(QuizQuestion)
class QuizQuestion(admin.ModelAdmin):
    list_display = ('quiz_id', 'question_text')
    search_fields = ('quiz__title',)


@admin.register(UserProgress)
class UserProgress(admin.ModelAdmin):
    list_display = ('user_id', 'course_id', 'completedLessons')
    search_fields = ('user__username', 'course__title')
