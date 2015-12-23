from cat import cat
from game import game
import pygame
from pygame.locals import *
import sys
cats = cat("tom")
print(cats.meow())

gm = game(300,500, "ayy")
gm.loop()

