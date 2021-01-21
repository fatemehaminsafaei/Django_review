from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='d', max_length=1)
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)

    class Meta:
        ordering =['published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

