from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # blank→保存時に何もデータを渡さなくてもOKとする null→NOT NULL制約を外す
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログを公開するメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
