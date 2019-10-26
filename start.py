import pygame
pygame.init()

win = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Glory be given to God.")

x = 50
y = 50
width = 40
height = 40
vel = 2

run = True
while run:
	pygame.time.delay(10)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x -= vel
	if keys[pygame.K_RIGHT]:
		x += vel
	if keys[pygame.K_UP]:
		y -= vel
	if keys[pygame.K_DOWN]:
		y += vel
	
	win.fill((0,0,0))
	pygame.draw.rect(win, (0,0,255), (x, y, width, height))
	pygame.display.update()

pygame.quit()
