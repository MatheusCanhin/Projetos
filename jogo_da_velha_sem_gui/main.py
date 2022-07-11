from random import randint


class JogoDaVelha():
    """ Têm como objetivo criar um jogo da velha"""

    def __init__(self):
        self.tabuleiro = {'7': ' ', '8': ' ', '9': ' ',
                          '4': ' ', '5': ' ', '6': ' ',
                          '1': ' ', '2': ' ', '3': ' '}
        self.rodada = 0
        self.turno = None
        self.ganhou = False
        self.empatou = False
        self.x_ganha = 0
        self.o_ganha = 0
        self.velha = 0
        self.jogador_da_vez = randint(0, 1)

    def fazer_jogada(self, jogada):
        """Tem a função de realizar a jogada do jogador"""

        if jogada in self.tabuleiro:
            if self.tabuleiro[jogada] == ' ':
                self.tabuleiro[jogada] = self.turno
                self.rodada += 1
            else:
                outra_jogada = input(
                    "Este lugar já foi ocupado, tente outro: ")
                self.fazer_jogada(outra_jogada)
        else:
            outra_jogada = input("Por favor digite um número válido: ")
            self.fazer_jogada(outra_jogada)

    def sortear_jogador(self):
        """Tem a função de sortear um jogador para começar"""

        if self.jogador_da_vez == 1:
            self.turno = 'X'
        else:
            self.turno = 'O'

    def mostra_tabuleiro(self):
        """Tem a função de printar o tabuleiro na tela"""

        print("┌───┬───┬───┐")
        print(
            f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │ ")
        print("├───┼───┼───┤")
        print(
            f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(
            f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
        print("└───┴───┴───┘")

    def jogar_novamente(self):
        """Verifica se os jogadores quem jogar novamente"""

        self.placar()
        repetir = input("Deseja jogar novamente(S/N)? ").strip().upper()
        if repetir == 'S':
            self.rodada = 0
            self.ganhou = False
            self.empatou = False
            self.jogador_da_vez = randint(0, 1)
            for item in self.tabuleiro:
                self.tabuleiro[item] = " "
        else:
            print("Obrigado por jogar!")
            exit()

    def verificar_vitoria(self):
        """Verifica todas as formas de ocorrer vitória"""

        # Verificando Linhas:
        if self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            self.ganhou = True
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            self.ganhou = True
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            self.ganhou = True

        # Verificando Colunas
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            self.ganhou = True
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            self.ganhou = True
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            self.ganhou = True

        # Verificando Diagonais
        if self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            self.ganhou = True
        elif self.tabuleiro['9'] == self.tabuleiro['5'] == self.tabuleiro['1'] != ' ':
            self.ganhou = True

    def verificar_empate(self):
        '''Verifica se ocorreu um empate'''

        if (self.ganhou is False) and (self.rodada == 9):
            self.empatou = True

    def placar(self):
        '''Mostra o placar do jogo'''

        print("\nO placar está assim:\n")
        print(
            f"\U00002B55 = {self.o_ganha} | \U0000274C {self.x_ganha} | \U0001F512 {self.velha}\n")

    def jogar(self):
        """Inicia o jogo da velha"""

        print("\n---BEM VINDO(A) AO JOGO DA VELHA---\n")
        print("Essas são as possiveis jogadas:\n")
        print("┌───┬───┬───┐")
        print("│ 7 │ 8 │ 9 │")
        print("├───┼───┼───┤")
        print("│ 4 │ 5 │ 6 │")
        print("├───┼───┼───┤")
        print("│ 1 │ 2 │ 3 │")
        print("└───┴───┴───┘")
        resposta = input("Preparado para jogar(S/N)? ").upper().strip()

        if resposta == "S":
            self.sortear_jogador()
            while True:
                self.mostra_tabuleiro()
                print(f"Turno do jogador {self.turno}")
                jogada = input('digite a sua jogada: ')

                self.fazer_jogada(jogada)
                self.verificar_vitoria()
                self.verificar_empate()

                if self.ganhou is True:
                    print("="*50)
                    print(f"Parabens!!!\nO jogador {self.turno} Ganhou!")
                    print("="*50)
                    if self.turno == 'X':
                        self.x_ganha += 1
                    else:
                        self.o_ganha += 1
                    self.mostra_tabuleiro()
                    self.jogar_novamente()
                elif self.empatou is True:
                    print("\n\nParece que temos um empate!")
                    self.velha += 1
                    self.mostra_tabuleiro()
                    self.jogar_novamente()
                else:
                    self.turno = "X" if self.turno == "O" else "O"
        else:
            print("\nAté a próxima!")

if __name__ == '__main__': 
    a = JogoDaVelha()
    a.jogar()
