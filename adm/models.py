import datetime

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class University(models.Model):
    title = models.CharField(verbose_name="Название университета", max_length=255)
    disciplines = ArrayField(models.CharField(max_length=155), verbose_name="Список факультетов", null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    group_number = models.CharField(verbose_name="Номер группы", max_length=255, null=True)


class Project(models.Model):
    users = ArrayField(models.ForeignKey(Profile, on_delete=models.SET_NULL), verbose_name="Список заинтересованных лиц", null=True)
    project_manager = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Проджект-менеджер", null=True)
    tester = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Тестировщик", null=True)
    front_end = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Фронтендер", null=True)
    back_end = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Бэкендер", null=True)
    design = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Дизайнер", null=True)
    mentor = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name="Куратор проекта", null=True)
    title = models.CharField(verbose_name="Название проекта", max_length=255, null=False)
    description = models.CharField(verbose_name="Описание проекта", max_length=255, null=True)
    goal = models.CharField(verbose_name="Цель проекта", max_length=255, null=False)
    start_date = models.DateTimeField(verbose_name="Дата начала проекта", default=datetime.datetime.utcnow())
    deadline_date = models.DateTimeField(verbose_name="Дедлайн проекта", null=False)
    end_date = models.DateTimeField(verbose_name="Дата конеца проекта", null=True)
    university = models.ForeignKey(University, on_delete=models.SET_NULL)