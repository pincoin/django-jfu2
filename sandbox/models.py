from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(
        verbose_name='title',
        max_length=255,
    )

    body = models.TextField(
        verbose_name='content body',
    )

    created = models.DateTimeField(
        verbose_name='created time',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk, ])
