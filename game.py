from menus import *
from personagens import *
from atributos import *
import pygame

#Inicialização
pygame.init()
frame = pygame.time.Clock()

#Pescagem
tela = tela()
fontes = fonte()
som_eff = som_efeitos()
cobra,maca,bases = conteudos(tela)
cenarios = imagem(tela)
bases = inicio(bases,tela,cenarios,fontes,som_eff)

#Programa
while True:
    frame.tick(60)
    bases = som(bases)
    tela['tela_definida'].fill((0,0,0))
    tela['tela_definida'].blit(cenarios['cenario1'],(0,0))
    cobra, base,cobra_tela = cobra_eventos (tela,cobra,bases)
    maca,bases = maca_eventos (tela,maca,bases,cobra_tela,som_eff)
    bases = aumenta (bases,tela,cobra)
    bases = game_over (bases,cobra_tela,cobra,tela,fontes,som_eff,cenarios)
    if bases['reset']:
        cobra, maca, bases = conteudos(tela)
        bases = som(bases)
    while bases['pause']:
        pause(tela,fontes,bases,som_eff)
        if bases['unpause']:
            bases=unpause(som_eff,bases)
            break
    pygame.display.update()