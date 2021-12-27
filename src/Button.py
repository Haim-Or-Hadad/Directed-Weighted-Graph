from pygame import *
import pygame

font.init()
arial_font = font.SysFont('Arial', 15, bold=True)

class Button:
    """
    simple button, base for everything
    """

    def __init__(self, title: str, size: tuple[int, int], color=Color(155, 230, 250)) -> None:
        self.title = title
        self.size = size
        self.color = color
        self.rect = Rect((0, 0), size)
        self.show = True
        self.disabled = False

    def add_click_listener(self, func):
        self.on_click.append(func)



    def render(self, surface: Surface, pos):
        if(not self.show):
            return
        self.rect.topleft = pos

        title_srf = arial_font.render(self.title, True, Color(110, 50, 150))
        title_rect = title_srf.get_rect(center=self.rect.center)
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, Color(120, 200, 250), self.rect, width=5)
        surface.blit(title_srf, title_rect)



