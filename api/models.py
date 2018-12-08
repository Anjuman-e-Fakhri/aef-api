from django.db import models

# Create your models here.
class Mumin(models.Model):
    its_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} | {}'.format(self.its_id, self.first_name)

    class Meta:
        ordering = ['its_id']
        verbose_name_plural = 'mumineen'