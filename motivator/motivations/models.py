from django.db import models

class Motivation(models.Model):
    nickname = models.CharField(max_length=64)
    motivation = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)
