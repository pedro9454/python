# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.mixer.init()  # inicia o pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')  # vai carregar o arquivo MP3
pygame.mixer.music.play()  # é para tocar a música
pygame.event.wait()  # espera a música acabar para encerrar
