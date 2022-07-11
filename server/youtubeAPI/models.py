from django.db import models
import uuid

# Create your models here.
class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    youtube_id = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    video_thumbnail = models.URLField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['-published_at']),
        ]


class API_Key(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateField()
    key = models.CharField(max_length=200)
    quota_exceeded = models.BooleanField(default=False)

    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"
