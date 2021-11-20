import math
import os
import sys

import pygame as pg

pg.init()
pg.mixer.pre_init(4800, -16, 2, 256)
pg.mixer.set_num_channels(16)


def distance_function(pos1, pos2):
    """Return the distance between the points (pos1) and (pos2)"""
    x1, y1 = pos1
    x2, y2 = pos2
    # length = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    x_squared = (x2 - x1) * (x2 - x1)
    y_squared = (y2 - y1) * (y2 - y1)
    length = math.sqrt(x_squared + y_squared)
    return length


def draw_text(text, colour, font_type, screen, x, y):  # Draws Centered Text
    """Function that centers text in Pygame
    Args:
        text::str
            String text to be centered
        colour::tuple
            Pretty self explanatory
        font_type::pg.font.SysFont("string", int)
            Specify which font to use
        screen::surface
            Specify which surface to blit centered text on
        x::float
            The x value of centered text
        y::float
            The y value of centered text
    """
    text_obj = font_type.render(text, True, colour)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)


class Main(object):
    def __init__(self):
        self.width = 800
        self.height = 800
        self.surface = pg.display.set_mode((self.width, self.height), flags=pg.HWSURFACE and pg.DOUBLEBUF and pg.SRCALPHA)
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.click = False
        self.mouse_pointer = [None, None]
        pg.display.set_caption("Nut Button")
        pg.display.set_icon(pg.image.load(os.getcwd() + "/assets/Nut_Button.png").convert_alpha())
        self.empty_nut_button = pg.image.load(os.getcwd() + "/assets/Empty_Nut_Button.png").convert_alpha()
        self.nut = pg.mixer.Sound(os.getcwd() + "/assets/Nut.wav")
        self.nut_font = pg.font.Font(os.getcwd() + "/assets/HelveticaLTStd-Roman.otf", 225)

    # ------------------------------------------------------------------------------------------------------------------
    def nut_button(self):
        running = True
        while running:
            for event in pg.event.get():
                pressed = pg.key.get_pressed()  # Gathers the state of all keys pressed
                if event.type == pg.QUIT or pressed[pg.K_ESCAPE]:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left Mouse Button
                        self.click = True
                        if distance_function([self.width / 2, self.height / 2], pg.mouse.get_pos()) < 390:
                            self.nut.play()
                if event.type == pg.MOUSEBUTTONUP:  # Reset Mouse Down value when button is released
                    if event.button == 1:  # Left Mouse Button
                        self.click = False
            self.clock.tick(self.FPS)
            self.surface.fill((255, 255, 255))
            self.surface.blit(self.empty_nut_button, (0, 0, self.width, self.height))
            # pg.draw.circle(self.surface, (255, 0, 0), (self.width / 2, self.height / 2), 390)  # For Reference
            # The font I used is a bit bugged so I used some manual offsetting (see below)
            draw_text("NUT", (255, 255, 255), self.nut_font, self.surface, (self.width / 2) - 14, (self.height / 2) + 36)
            pg.display.update()


# ----------------------------------------------------------------------------------------------------------------------
main = Main()
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main.nut_button()
