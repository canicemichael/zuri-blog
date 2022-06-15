from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()