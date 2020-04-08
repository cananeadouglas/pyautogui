import pygame
import time

def chama():
    pygame.init()
    tela = pygame.display.set_mode([300,200])
    pygame.display.set_caption("ACORDAR")

    sair = False

    while sair != True:
        for event in pygame.event.get():
            pygame.mixer.music.load('Gipsy.mp3')
            pygame.mixer.music.play()
            if event.type == pygame.QUIT:
                sair = True
        pygame.display.update()

    pygame.quit()
    

chama()
