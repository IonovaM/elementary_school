from django.db import models
from school.models import Student, Class

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.CharField(max_length=50)
    grade = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.subject}: {self.grade}"

class Homework(models.Model):
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='homework')
    subject = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.subject} ({self.due_date})"
