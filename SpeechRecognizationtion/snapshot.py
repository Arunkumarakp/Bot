import pygame, sys, os
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

# Ensure we have somewhere for the frames
try:
    os.makedirs("Snaps")
except OSError:
    pass

screen = pygame.display.set_mode((640, 480))

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()

file_num = 0
done_capturing = False

while not done_capturing:
    file_num = file_num + 1
    image = cam.get_image()
    screen.blit(image, (0,0))
    pygame.display.update()

    # Save every frame
    filename = "Snaps/%04d.png" % file_num
    pygame.image.save(image, filename)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done_capturing = True

# Combine frames to make video
os.system("avconv -r 8 -f image2 -i Snaps/%04d.png -y -qscale 0 -s 640x480 -aspect 4:3 result.avi")
