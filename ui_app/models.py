from django.db import models
from django.utils import timezone


# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset()


class Answer(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique_for_date='publish')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    # objects = models.Manager()
    # published = PublishedManager()

    def __str__(self):
        return self.title


class TmpMessage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique_for_date='created')
    message_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
            return self.title
