import pygame

from Code.menu import Menu
from asset.Const import WIN_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all events
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                   # pygame.quit()  # close window
                    #quit()  # end pygame