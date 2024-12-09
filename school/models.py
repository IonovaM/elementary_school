from django.db import models
from users.models import User


class Class(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, related_name='classes')
    schedule = models.TextField()  # JSON с расписанием.

    def __str__(self):
        return f"{self.name} ({self.specialization})"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=200)

    def __str__(self):
        return self.user.get_full_name()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.user.get_full_name()
