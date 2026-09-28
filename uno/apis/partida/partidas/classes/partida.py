from partidas.classes.baralho import Baralho

class JogoPartida:
    def __init__(self, jogador1_id, jogador2_id):
        self.jogador1_id = jogador1_id
        self.jogador2_id = jogador2_id

        self.baralho = Baralho()

        self.cartas_jogador1 = []
        self.cartas_jogador2 = []

        self.carta_topo = None
        self.turno_id = jogador1_id

    def distribuir_cartas(self):
        for _ in range(7):
            self.cartas_jogador1.append(
                self.baralho.comprar()
            )

            self.cartas_jogador2.append(
                self.baralho.comprar()
            )

    def iniciar(self):
        self.distribuir_cartas()
        self.carta_topo = self.baralho.comprar()