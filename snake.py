import pygame as py
import time
import random


#GUI
WIDTH = 900
HEIGHT = 900
WINDOW = py.display.set_mode((WIDTH, HEIGHT))

#COLORS
BLACK = py.Color(0 , 0 , 0)
WHITE = py.Color(255,255, 255)
GREY = py.Color(128, 128, 128)

#initial position
init_pos_x = 450
init_pos_y = 450


def drawGrid():
    blockSize = 20
    for x in range(0, WIDTH, blockSize):
        for y in range(100, HEIGHT, blockSize):
            rect = py.Rect(x, y, blockSize, blockSize)
            py.draw.rect(WINDOW, GREY, rect, 1)


#main
def main():
    while True:
        drawGrid()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
        py.display.update()

if __name__ == "__main__":
    main()


