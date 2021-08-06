from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    text = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User,
        related_name='documents',
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    def get_absolute_url(self):
        return reverse('view_doc', kwargs={'pk': self.pk})

class Attribute(models.Model):
    doc = models.ForeignKey(Document,
        related_name='attributes',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    value = models.TextField()
