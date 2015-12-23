
from globals import globals
import pygame
from pygame.locals import *
import sys



class game:	
	def __init__(self, sizex, sizey, name):
		self.sizex = sizex
		self.sizey = sizey
		self.name = name
		self.boxtext = []
		pygame.init()
		
		self.fpsClock = pygame.time.Clock()
		self.windowSurfaceObj = pygame.display.set_mode((sizex,sizey))
		pygame.display.set_caption(name)
				
		self.red = pygame.Color(255,0,0)
		self.green = pygame.Color(0,255,0)
		self.blue = pygame.Color(0,0,255)
		self.white = pygame.Color(255,255,255)
		self.black = pygame.Color(0,0,0)
		self.fontobj = pygame.font.Font('freesansbold.ttf',32)
		self.mx, self.my = 0 , 0
		self.redrects = []
		self.textrects = []
		
	def addrect(self, posx, posy, sizex = 10, sizey = 10):
		rect= pygame.Rect = (posx, posy, sizex, sizey)
		self.redrects.append(rect)
	
	def textbox(self,window, name= "insert text", font= None, color= (255,0,0),pos = (0,0)):
		if font== None:
			font=(pygame.font.Font('freesansbold.ttf',32))
		text = font.render(name, False, color)
		nameobj = text.get_rect()
		nameobj.topleft = (pos)
		self.textrects.append(nameobj)
		self.boxtext.append(text)
		window.blit(text,nameobj)
	
	
	def killtextbox(self, textindex):
		if (len(self.boxtext) !=0) and ((len(self.boxtext)-1) >= textindex):
			del self.boxtext[textindex]
			del self.textrects[textindex]
			
		
	def killrect(self,rectindex):
		if len(self.redrects) != 0:
			del self.redrects[rectindex]
	
	def loop(self):
		self.textbox(self.windowSurfaceObj, name="8==D the game",pos=(20,20))
		self.textbox(self.windowSurfaceObj, name="play", pos=(20,125))
		self.textbox(self.windowSurfaceObj, name="leave", pos=(150, 125))
		self.addrect(10,100, 280,10)	
		textnum = 0
		
		while(True):
			self.windowSurfaceObj.fill(self.black)
			
			
			for rect in self.redrects:
				pygame.draw.rect(self.windowSurfaceObj, self.red, rect)
			
			for rect in self.textrects:
				if textnum >= len(self.boxtext):
					textnum = 0
				text = self.boxtext[textnum]
				self.windowSurfaceObj.blit(text,rect)
				textnum+=1
					
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				print event.type
				
				if event.type == MOUSEBUTTONUP:
					self.killtextbox(0)
					pass
				
				
			pygame.display.update()
			self.fpsClock.tick(60)
