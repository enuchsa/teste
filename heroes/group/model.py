from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    hero = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'group'
