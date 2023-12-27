from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver



class Hero(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)
    image = models.CharField(max_length=150, blank=False, null=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        db_table = 'hero'
    
class Group(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    hero = models.JSONField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'group'
        # unique_together = ('user', 'hero', 'id')

    @receiver(pre_save, sender=Group)
    def validate_unique_hero_ids(sender, instance, **kwargs):
        # Obtém o ID do grupo atual, excluindo-o da comparação
        grupo_atual_id = instance.id if instance.id is not None else None

        # Verifica se os IDs de heróis estão em algum outro grupo
        outros_grupos = Group.objects.exclude(id=grupo_atual_id).filter(
            hero__overlap=instance.hero
        )

        if outros_grupos.exists():
            ids_em_outro_grupo = outros_grupos.values_list('hero', flat=True).get()
            ids_em_conflito = set(instance.hero).intersection(ids_em_outro_grupo)
            raise ValueError(f"IDs de heróis {ids_em_conflito} já estão em outro grupo.")
        


