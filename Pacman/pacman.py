import pygame

#Inicia pygame
pygame.init()

# Variaveis do jogo
largura_tela, altura_tela = 800, 600
amarelo = (255, 255, 0)
preto = (0, 0, 0)
azul = (0, 0, 255)


#Criando a tela do jogo.
tela = pygame.display.set_mode((largura_tela, altura_tela), 0, 0)

#Criando o pacman
class pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = largura_tela // 2  # onde vai iniciar o pacman
        self.centro_y = altura_tela // 2    # onde vai iniciar o pacman
        self.tamanho = 800 // 30 # Quantidade de casas que o pacman vai percorrer
        self.raio = int(self.tamanho // 2)
        self.velocidade_x = 0.7
        self.velocidade_y = 0.7

    def pintarPacman(self, tela):
        # Corpo do Pacman
        pygame.draw.circle(tela, amarelo, (int(self.centro_x), int(self.centro_y)), self.raio, 0)
        # Desenho da Boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, preto, pontos, 0)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10 )
        pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

# Movimentando o pacman
    def Movimento_Pacman(self):
        # Movimento Horizontal
        self.coluna += self.velocidade_x
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        if self.centro_x + self.raio > largura_tela:
            self.velocidade_x -= 1
        if self.centro_x - self.raio < 0:
            self.velocidade_x += 1
        # Movimento Vertical
        self.linha += self.velocidade_y
        self.centro_y = int(self.linha * self.tamanho + self.raio)
        if self.centro_y + self.raio > altura_tela:
            self.velocidade_y -= 1
        if self.centro_y - self.raio < 0:
            self.velocidade_y += 1

# simulando a classe Main
if __name__ == "__main__":
    pacman = pacman()


while True:

    # Calcular as Regras:
    pacman.Movimento_Pacman()

    # Pintas a tela:
    tela.fill(preto) #limpa a tela e pinta de preto
    pacman.pintarPacman(tela)
    pygame.display.update()
    pygame.time.delay(100)

    #Captura dos eventos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


