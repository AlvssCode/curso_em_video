# Exercício 21 – Tocando um MP3
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('RickAstley.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
