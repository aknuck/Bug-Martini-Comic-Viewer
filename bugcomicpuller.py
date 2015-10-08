#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2,urllib
import re
import sys
import os
import pygame
import threading
from pygame.locals import *
from BugMartiniAPI import *

print "Starting up Bug Martini..."

pygame.init()
pygame.display.set_caption("Bug Martini")
screen = pygame.display.set_mode((1021,505))

#if I asked you to name a soft drink, you would say...
#coke
#now why am I surprised he said coke

buggreen = pygame.Color(112,147,43)
black = pygame.Color(0,0,0)
blue = pygame.Color(0,0,255)
current = getTodays()
if not os.path.exists("bugMartiniAssets"):
	os.makedirs("bugMartiniAssets")
if not os.path.exists("bugMartiniAssets/comics"):
	os.makedirs("bugMartiniAssets/comics")
download(getImage(current),"bugMartiniAssets/comics/"+getName(current)+".png")
comicSurfaceObject = pygame.image.load("bugMartiniAssets/comics/"+getName(current)+".png")
bugLogoSurfaceObject = pygame.image.load("bugMartiniAssets/bugNameLogo.png")
while True:
	screen.fill(buggreen)
	screen.blit(bugLogoSurfaceObject,(10,5))
	screen.blit(comicSurfaceObject,(10,155))
	pygame.draw.rect(screen,black,(8,153,1007,345),3)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				pygame.draw.circle(screen,blue,(990,30),20,0)
				pygame.display.update()
				current = previous(current)
				#t = threading.Thread(target=download,args=(getImage(previous(current)),"bugMartiniAssets/comics/"+getName(previous(current))+".png"))
				#t.daemon = True
				#t.start()
				try:
					comicSurfaceObject = pygame.image.load("bugMartiniAssets/comics/"+getName(current)+".png")
				except:
					download(getImage(current),"bugMartiniAssets/comics/"+getName(current)+".png")
					comicSurfaceObject = pygame.image.load("bugMartiniAssets/comics/"+getName(current)+".png")
			if event.key == K_RIGHT:
				pygame.draw.circle(screen,blue,(990,30),20,0)
				pygame.display.update()
				current = next(current)
				#t = threading.Thread(target=download,args=(getImage(next(current)),"bugMartiniAssets/comics/"+getName(next(current))+".png"))
				#t.daemon = True
				#t.start()
				try:
					comicSurfaceObject = pygame.image.load("bugMartiniAssets/comics/"+getName(current)+".png")
				except:
					download(getImage(current),"bugMartiniAssets/comics/"+getName(current)+".png")
					comicSurfaceObject = pygame.image.load("bugMartiniAssets/comics/"+getName(current)+".png")

	pygame.display.update()


