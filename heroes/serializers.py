from rest_framework import serializers
from heroes.models import Hero, Group


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ['url', 'name', 'description']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['url', 'name', 'description', 'hero']
        
    def validate_ids_herois(self, value):
        # Obtém o ID do grupo atual, excluindo-o da comparação
        grupo_atual_id = self.instance.id if self.instance else None

        # Verifica se os IDs de heróis estão em algum outro grupo
        outros_grupos = Hero.objects.exclude(id=grupo_atual_id).filter(
            ids_herois__overlap=value
        )

        if outros_grupos.exists():
            ids_em_outro_grupo = outros_grupos.values_list('ids_hero', flat=True).get()
            ids_em_conflito = set(value).intersection(ids_em_outro_grupo)
            raise serializers.ValidationError(f"IDs de heróis {ids_em_conflito} já estão em outro grupo.")

        return value
