from django.db import models
from django.conf import settings


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=50, verbose_name='Title')
    task_info = models.CharField(max_length=500, verbose_name='Information')
    task_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='user'
    )

    def __str__(self):
        return f'{self.task_user} - {self.task_name}'
