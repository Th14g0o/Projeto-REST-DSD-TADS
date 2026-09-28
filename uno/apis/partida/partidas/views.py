from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Partida
from .serializers import PartidaSerializer
import random

def criar_baralho():
    cores = ['vermelho', 'azul', 'verde', 'amarelo']

    baralho = []

    for cor in cores:
        for valor in range(10):
            baralho.append({
                'cor': cor,
                'valor': valor
            })

    random.shuffle(baralho)

    return baralho

class PartidaListView(generics.ListCreateAPIView):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

class PartidaDetailView(generics.RetrieveAPIView):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

class EntrarPartidaView(APIView):

    def post(self, request, pk):
        try:
            partida = Partida.objects.get(pk=pk)
        except Partida.DoesNotExist:
            return Response(
                {'erro': 'Partida não encontrada.'},
                status=status.HTTP_404_NOT_FOUND
            )

        jogador_id = request.data.get('jogador_id')

        if not jogador_id:
            return Response(
                {'erro': 'jogador_id é obrigatório.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if partida.jogador1_id == int(jogador_id):
            return Response(
                {'erro': 'Jogador já está na partida.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if partida.jogador2_id is not None:
            return Response(
                {'erro': 'A partida já possui dois jogadores.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        partida.jogador2_id = jogador_id
        partida.status = 'em_andamento'
        partida.save()

        return Response(PartidaSerializer(partida).data)