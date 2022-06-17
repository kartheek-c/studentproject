from django.db import models


class Student(models.Model):
    name = models.CharField(max_length = 200)
    marks = models.CharField(max_length = 100)
    #department = modles.CharField(max_Field = 200)
    mobile = models.IntegerField(default = 0)


class Department(models.Model):
    dept_name = models.CharField(max_length = 100)
    dept_branch = models.CharField(max_length = 200)
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)


