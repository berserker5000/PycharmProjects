from __future__ import unicode_literals


from django.db import models

# Create your models here.
class index(models.Model):
    ArticleName=models.CharField(max_length=150)
    ArticleBody=models.TextField()