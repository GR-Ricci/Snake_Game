import pygame
from pygame.locals import *
from random import randint
from time import sleep

def tela():
    pygame.display.set_caption('Snake')

    largura_tela = int(640)
    altura_tela = int(480)
    tela_definida = pygame.display.set_mode((largura_tela,altura_tela))

    tela = {'largura': largura_tela,'altura':altura_tela,'tela_definida':tela_definida}
    return tela

def inicio(bases,tela,cenarios,fontes,som_eff):
    pygame.mixer.music.load('elementos/Som/musicas/Ketsa - Inside Dead.mp3')
    pygame.mixer.music.play(-1)
    while bases['inicio']:

        for event in pygame.event.get():  # Isso evita travar
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    bases['inicio'] = False
                    som_eff['start'].play()
                    sleep(0.5)
                    pygame.mixer.music.stop()

        tela['tela_definida'].blit(cenarios['inicio'],(0,0))
        mensagem_inicio_pura = f'Enter > Start'
        mensagem_inicio = fontes['inicio'].render(mensagem_inicio_pura, True, (250, 250, 0))
        tela['tela_definida'].blit(mensagem_inicio, (100,50 ))
        pygame.display.update()

    return bases

def pause(tela,fontes,bases,som_eff):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.mixer.music.pause()
        pause_tocado = False

        if not bases ['som_tocado']:
            som_eff['pause'].play()
            bases['som_tocado'] = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            bases['pause'] = False
            bases['unpause'] = True
    mensagem_pause_puro = f'PAUSE'
    mensagem_pause = fontes['calibri'].render(mensagem_pause_puro,True,(250,250,0))
    tela['tela_definida'].blit(mensagem_pause, (0,0))
    pygame.display.update()

def unpause(som_eff,bases):
    bases['som_tocado'] = False
    som_eff['despause'].play()
    pygame.mixer.music.unpause()
    return bases

def game_over(bases,cobra_tela,cobra,tela,fontes,som_eff,cenarios):
    if bases['start'] and bases['cobra_corpo'].count(cobra_tela) > 1:
        bases['gameover']=True
    if cobra['x'] > tela['largura'] -15:
        bases['gameover']=True
    if cobra['x'] < -5:
        bases['gameover']=True
    if cobra['y'] > tela['altura']-15:
        bases['gameover']=True
    if cobra['y'] < -5:
        bases['gameover']=True
#som game-over
    if bases['gameover']:
        canal = som_eff['colisao_morte'].play()
        sleep(1)

        for i in range(0, cenarios['gameover'].get_height(), 5):  # 5px de incremento
            tela['tela_definida'].blit(cenarios['gameover'].subsurface((0, i, cenarios['gameover'].get_width(), 5)), (0, i))
            pygame.display.update((0, i, cenarios['gameover'].get_width(), 5))
            pygame.time.delay(1)  # Velocidade
        pygame.display.update()

        canal.queue(som_eff['morrer'])
        pygame.mixer.music.stop()
        sleep(1)
        pygame.mixer.music.load('elementos/Som/musicas/BoxCat Games - Defeat.mp3')
        pygame.mixer.music.play(-1)


#tela game-over
    while bases['gameover']:
        mensagem_gameover_lista = [f'Esc > Sair', 'Enter > Continuar']
        for i, v in enumerate(mensagem_gameover_lista):
            mensagem_gameover = fontes['calibri'].render(v, True,(250,250,0))
            tela['tela_definida'].blit(mensagem_gameover,(0,0 +i *20))
            pygame.display.update()

            for event in pygame.event.get():  # Isso evita travar
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == K_RETURN:
                        som_eff['continuar'].play()
                        pygame.mixer.music.stop()
                        sleep(1)
                        bases['gameover'] = False
                        bases['reset'] = True
    return bases