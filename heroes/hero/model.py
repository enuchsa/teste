from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)
    image = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'hero'
