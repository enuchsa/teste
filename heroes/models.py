from django.db import models



class Hero(models.Model):
    name = models.CharField(max_lentgh=150, blank=False, null=False)
    description = models.CharField(max_lentgh=400, blank=False, null=False)
    image = models.CharField(max_lentgh=150, blank=False, null=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Group(models.Model):
    name = models.CharField(max_lentgh=150, blank=False, null=False)
    description = models.CharField(max_lentgh=300, blank=False, null=False)
    heroes = models.ForeignKey(Hero, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
