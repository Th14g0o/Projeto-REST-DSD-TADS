from django.db import models

STATUS_CHOICES = [
    ('aguardando', 'Aguardando'),
    ('em_andamento', 'Em andamento'),
    ('finalizada', 'Finalizada'),
]

class Partida(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aguardando')

    jogador1_id = models.IntegerField(null=True, blank=True)
    jogador2_id = models.IntegerField(null=True, blank=True)

    vencedor_id = models.IntegerField(null=True, blank=True)

    criada_em = models.DateTimeField(auto_now_add=True)

    # Estado do jogo
    turno_id = models.IntegerField(null=True, blank=True)

    cartas_jogador1 = models.JSONField(default=list)
    cartas_jogador2 = models.JSONField(default=list)

    carta_topo = models.JSONField(null=True, blank=True)

    baralho = models.JSONField(default=list)

    def __str__(self):
        return f'Partida {self.id}'