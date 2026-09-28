from rest_framework import serializers

from .models import Partida


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = [
            'id',
            'status',
            'jogador1_id',
            'jogador2_id',
            'vencedor_id',
            'turno_id',
            'cartas_jogador1',
            'cartas_jogador2',
            'carta_topo',
            'baralho',
            'criada_em',
        ]
        read_only_fields = [
            'id',
            'criada_em',
            'turno_id',
            'cartas_jogador1',
            'cartas_jogador2',
            'carta_topo',
            'baralho',
        ]