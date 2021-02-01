from django.db import models
from django.utils import timezone

from django.utils.translation import gettext as _


class Writer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=(('F', 'Female'), ('M', 'Male')), default='d', max_length=1)
    slug = models.SlugField(max_length=100, unique=True, default='')

    @property
    def post_number(self):
        posts = Post.objects.filter(writer=self.id)
        post_number = len(posts)
        return post_number


class Post(models.Model):
    STATUS = (
        ('d', ("Draft")),
        ('p', ("Publish"))
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.ForeignKey(Writer, related_name='writer', on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    create_date = models.DateTimeField()
    status = models.CharField(choices=STATUS, default='d', max_length=1)
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, default='')

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    @property
    def post_age(self):
        try:
            age = timezone.now().year - self.publish_date.year
        except AttributeError:
            age = 'unknown'
        return age
