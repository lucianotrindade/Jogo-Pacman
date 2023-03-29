import pygame

pygame.init()

#Criando a tela do jogo.

largura_tela, altura_tela = 800, 600
amarelo = (255, 255, 0)
preto = (0, 0, 0)

tela = pygame.display.set_mode((largura_tela, altura_tela), 0, 0)

#Criando o pacman
class pacman:

    def __init__(self):
        self.centro_x = largura_tela / 2
        self.centro_y = altura_tela / 2
        self.tamanho = 50
        self.raio = int(tamanho / 2)
    def pintar(self, tela):
        #Desenho do corpo do pacman
        pygame.draw.circle(tela, amarelo, (int(self.centro_x), int(self.centro_y)), self.raio, 0)
        #Desenho da Boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, preto, pontos, 0)

if __name__ == "__main__":
    pacman = pacman()

while True:
    pacman.pintar(tela)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()