import pygame
from pygame.locals import *
from random import randint
from time import sleep

def conteudos(tela):
#Dimensões
    largura_cobra = 20
    altura_cobra = 20
#Personagens:
    cobra_corpo =[]
    cobra ={'largura': 20,'altura': 20,'x': (tela['largura'] - largura_cobra) / 2,
            'y': (tela['altura'] - altura_cobra) / 2,'x_controle': 0, 'y_controle':0}
    maca = {'largura': 20, 'altura': 20,'x' :randint(0, tela['largura'] - 20),'y': randint(0, tela['altura'] - 20)}
#Bases
    bases = {'start': False, 'gameover': False, 'reset':False,
             'pause': False, 'unpause': False,'inicio':True,
             'som_tocado':False,
             'direcao':'parado',
             'tamanho_cobra':5, 'cobra_corpo': cobra_corpo,
             'faixa': 0}
    return cobra,maca,bases

def fonte():
    calibri = pygame.font.SysFont('calibri',20,False,False)
    arial = pygame.font.SysFont('arial', 50,False,False)
    fontes = {'calibri': calibri,'inicio':arial}
    return fontes

def imagem(tela):
    cenario1_imagem = (pygame.image.load
    ('elementos/Imagem/cenarios/environment_forest_evening.png'))
    gameover_imagem= (pygame.image.load
    ('elementos/Imagem/gameover/ChatGPT Image 14 de abr. de 2025, 18_08_34.png'))
    inicio_imagem = (pygame.image.load
    ('elementos/Imagem/inicio/digital-art-snake-illustration (1).jpg'))
    cenario1 = pygame.transform.scale(cenario1_imagem, (tela['largura'],tela['altura']))
    gameover = pygame.transform.scale(gameover_imagem, (tela['largura'],tela['altura']))
    inicio = pygame.transform.scale(inicio_imagem, (tela['largura'],tela['altura']))
    cenarios = {'cenario1':cenario1,'gameover':gameover,'inicio':inicio}
    return cenarios

def som(bases):
    musicas1 =['som/musicas/Hypnotic-Puzzle.mp3','som/musicas/Hypnotic-Puzzle3.mp3',
               'som/musicas/Hypnotic-Puzzle4.mp3','som/musicas/Hypnotic-Puzzle2.mp3']
    if not bases['pause']:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(musicas1[bases['faixa']])
            pygame.mixer.music.play()
            bases['faixa'] += 1
        if bases['faixa'] == 3:
            bases['faixa'] = 1
    return bases

def som_efeitos():
    comer_maca = pygame.mixer.Sound('elementos/Som/efeitos/Rise03 (online-audio-converter.com).wav')
    colisao_morte = pygame.mixer.Sound('elementos/Som/efeitos/FX01_[cut_1sec].wav')
    morrer = pygame.mixer.Sound('elementos/Som/efeitos/mb_die.wav')
    pause = pygame.mixer.Sound('elementos/Som/efeitos/Pause.wav')
    despause = pygame.mixer.Sound(r'elementos/Som/efeitos/DespauseSom.wav')
    continuar = pygame.mixer.Sound('elementos/Som/efeitos/renascer.wav')
    start = pygame.mixer.Sound('elementos/Som/efeitos/StartSom.wav')

    som_eff = {'comer_maca': comer_maca, 'colisao_morte':colisao_morte, 'morrer':morrer,'pause':pause,'despause':despause,
               'continuar': continuar,'start':start}
    return som_eff