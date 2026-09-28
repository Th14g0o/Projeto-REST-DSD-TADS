import random

from .carta import Carta


class Baralho:

    def __init__(self):
        self.cartas = []
        self._criar_cartas()
        self.embaralhar()

    def _criar_cartas(self):
        cores = [
            'vermelho',
            'azul',
            'verde',
            'amarelo'
        ]

        for cor in cores:
            for valor in range(10):
                self.cartas.append(
                    Carta(cor, valor)
                )

    def embaralhar(self):
        random.shuffle(self.cartas)

    def comprar(self):
        return self.cartas.pop()