import pygame
from time import sleep
pygame.init()
window=pygame.display.set_mode((1300,800))
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(0.5)
img=pygame.image.load('scr.jpg')
window.blit(img,(0,0))
pygame.display.update()
sleep(3)

