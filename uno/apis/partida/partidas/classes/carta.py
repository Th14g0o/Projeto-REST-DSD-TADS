class Carta:

    def __init__(self, cor, valor):
        self.cor = cor
        self.valor = valor

    def pode_ser_jogada(self, carta_topo):
        return (
            self.cor == carta_topo.cor
            or self.valor == carta_topo.valor
        )