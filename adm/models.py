import datetime

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class University(models.Model):
    title = models.CharField(verbose_name="Название университета", max_length=255)
    disciplines = ArrayField(models.CharField(max_length=155), verbose_name="Список факультетов", null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, related_name='user_university')
    group_number = models.CharField(verbose_name="Номер группы", max_length=255, null=True)


class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=155, null=False)
    description = models.CharField(verbose_name="Описание категории" ,max_length=255, null=True)


class Project(models.Model):
    users = ArrayField(models.IntegerField(), verbose_name="Список заинтересованных лиц")
    project_manager = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Проджект-менеджер", null=True,
                                        related_name='project_project_manager')
    tester = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Тестировщик", null=True,
                               related_name='project_tester')
    front_end = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Фронтендер", null=True,
                                  related_name='project_front_end')
    back_end = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Бэкендер", null=True,
                                 related_name='project_back_end')
    designer = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Дизайнер", null=True,
                                 related_name='project_designer')
    mentor = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Куратор проекта", null=True,
                               related_name='project_mentor')
    title = models.CharField(verbose_name="Название проекта", max_length=255, null=False)
    description = models.CharField(verbose_name="Описание проекта", max_length=255, null=True)
    goal = models.CharField(verbose_name="Цель проекта", max_length=255, null=False)
    start_date = models.DateTimeField(verbose_name="Дата начала проекта", default=datetime.datetime.utcnow())
    deadline_date = models.DateTimeField(verbose_name="Дедлайн проекта", null=False)
    end_date = models.DateTimeField(verbose_name="Дата конеца проекта", null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, verbose_name="Университет", null=True,
                                   related_name='project_university')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория проекта", null=True,
                                 related_name='project_category')


class MarkChoices(models.IntegerChoices):
    TOO_BAD = 1, 'Too Bad'
    BAD = 2, 'Bad'
    NORMAL = 3, 'Normal'
    GOOD = 4, 'Good'
    EXCELLENT = 5, 'Excellent'


class Mark(models.Model):
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Куратор проекта", null=False,
                               related_name='mark_mentor')
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Студент", null=False,
                                related_name='mark_student')
    mark = models.IntegerField(verbose_name="Оценка", default=MarkChoices.BAD, choices=MarkChoices.choices)
