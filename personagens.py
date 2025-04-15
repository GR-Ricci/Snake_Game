import pygame
from pygame.locals import *
from random import randint

def cobra_eventos(tela,cobra,bases):
#eventos
    for event in pygame.event.get():
            #Encerramento
        if event.type == QUIT:
            pygame.quit()
            exit()
            #Movimento Cobra
        if event.type == KEYDOWN:
            if event.key == K_a and bases['direcao'] != 'direita':
                cobra['x_controle'] = -3
                cobra['y_controle'] = 0
                bases['direcao'] = 'esquerda'

            if event.key == K_d and bases['direcao'] != 'esquerda':
                cobra['x_controle'] = +3
                cobra['y_controle'] = 0
                bases['direcao'] = 'direita'
            if event.key == K_w and bases['direcao'] != 'baixo':
                cobra['x_controle'] = 0
                cobra['y_controle'] = -3
                bases['direcao'] = 'cima'
            if event.key == K_s and bases['direcao'] != 'cima':
                cobra['x_controle'] = 0
                cobra['y_controle'] = +3
                bases['direcao'] = 'baixo'

            if event.key == K_RETURN:
                bases['pause'] = not bases['pause'] #if false = not false(true)
                bases['unpause'] = not bases['pause'] #unpause = if pause (true) = not pause >> (false)
                                                                #if pause (false) = not pause >> (true)

            if bases['direcao'] != 'parado':
                bases['start'] = True

    cobra['x'] += cobra['x_controle']
    cobra['y'] += cobra['y_controle']
    cobra_tela = pygame.draw.rect(tela['tela_definida'], (0, 250, 0),
                                     (cobra['x'], cobra['y'], cobra['largura'], cobra['altura']))
    bases['cobra_corpo'].append(cobra_tela)

    return cobra, bases,cobra_tela

def maca_eventos(tela,maca,bases,cobra_tela,som_eff):
    maca_tela = pygame.draw.rect(tela['tela_definida'], (250,0,0), (maca['x'], maca['y'], maca['largura'], maca['altura']))

    if cobra_tela.colliderect(maca_tela):
        som_eff['comer_maca'].play()
        maca['x'] = randint(0, tela['largura']-20)
        maca['y'] = randint(0, tela['altura'] -20)
        bases['tamanho_cobra'] += 1
    return maca,bases

def aumenta(bases,tela,cobra):
    for v in bases['cobra_corpo']:
        cobra_corpo_tela = pygame.draw.rect(tela['tela_definida'], (0,250,0),
                                                (v[0],v[1],cobra['largura'],cobra['altura']))
        if len(bases['cobra_corpo']) > bases['tamanho_cobra']:
            del(bases['cobra_corpo'][0])
    return bases