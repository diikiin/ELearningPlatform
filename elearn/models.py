from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_student = models.BooleanField(default=True)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructors = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    total_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    correct_option = models.CharField(max_length=1)


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completedLessons = models.IntegerField(default=0)
    quiz_score = models.FloatField(default=0)
