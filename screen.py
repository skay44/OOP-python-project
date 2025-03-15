import pygame
import world
import tile

class Screen:
    WIDTH = 25
    HEIGHT = 25

    BUTTON_RED = 50
    BUTTON_GREEN = 50
    BUTTON_BLUE = 50

    def createTiles(self, x, y, w):
        #print("x:" + str(x) +  " y:" + str(y))
        if(w.animalArray[x][y] != None):
            img = pygame.image.load(w.animalArray[x][y].path)
        else:
            img = pygame.image.load("Images/tile.png")
        self.scr.blit(img,((x+1)*self.WIDTH,(y+1)*self.HEIGHT))


    def updateTiles(self, x, y):
        for i in range(0,x,1):
            for j in range(0,y,1):
                self.createTiles(i,j, self.w)

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.scr = pygame.display.set_mode(((x+24)* self.WIDTH, (y+2)*self.HEIGHT))
        icon = pygame.image.load('Images/icon.png')
        pygame.display.set_icon(icon)

        self.scr.fill((28,23,23))
        for i in range(0,x,1):
            for j in range(0,y,1):
                self.createTiles(i,j, w)


        font = pygame.font.SysFont('Georgia',13,bold=True)

        self.next_round_button_surface = font.render('Next round', True, 'White')
        self.next_round_button = pygame.Rect((x+2)*self.WIDTH,1*self.HEIGHT,4*self.WIDTH,1*self.HEIGHT)

        self.new_board_button_surface = font.render('New board', True, 'White')
        self.new_board_button = pygame.Rect((x+2)*self.WIDTH,2*self.HEIGHT,4*self.WIDTH,1*self.HEIGHT)

        self.save_game_button_surface = font.render('Save game', True, 'White')
        self.save_game_button = pygame.Rect((x+2)*self.WIDTH,3*self.HEIGHT,4*self.WIDTH,1*self.HEIGHT)

        self.load_game_button_surface = font.render('Load game', True, 'White')
        self.load_game_button = pygame.Rect((x+2)*self.WIDTH,4*self.HEIGHT,4*self.WIDTH,1*self.HEIGHT)

        self.text_background = pygame.Rect((x+7)*self.WIDTH,1*self.HEIGHT,16*self.WIDTH,y*self.HEIGHT)

    def checkClicked(self):
        mouse_position = pygame.mouse.get_pos()
        if(self.next_round_button.collidepoint(mouse_position)):
            self.w.next_round()
        elif(self.new_board_button.collidepoint(mouse_position)):
            self.w.new_board()
        elif (self.save_game_button.collidepoint(mouse_position)):
            self.w.save_game()
        elif (self.load_game_button.collidepoint(mouse_position)):
            self.w.load_game()

    def updateVisuals(self):
        mouse_position = pygame.mouse.get_pos()
        if(self.next_round_button.collidepoint(mouse_position)):
            pygame.draw.rect(self.scr, (self.BUTTON_RED + 50, self.BUTTON_GREEN + 50, self.BUTTON_BLUE + 50), self.next_round_button)
        else:
            pygame.draw.rect(self.scr, (self.BUTTON_RED, self.BUTTON_GREEN, self.BUTTON_BLUE), self.next_round_button)

        if(self.new_board_button.collidepoint(mouse_position)):
            pygame.draw.rect(self.scr, (self.BUTTON_RED + 50, self.BUTTON_GREEN + 50, self.BUTTON_BLUE + 50), self.new_board_button)
        else:
            pygame.draw.rect(self.scr, (self.BUTTON_RED, self.BUTTON_GREEN, self.BUTTON_BLUE), self.new_board_button)

        if(self.save_game_button.collidepoint(mouse_position)):
            pygame.draw.rect(self.scr, (self.BUTTON_RED + 50, self.BUTTON_GREEN + 50, self.BUTTON_BLUE + 50), self.save_game_button)
        else:
            pygame.draw.rect(self.scr, (self.BUTTON_RED, self.BUTTON_GREEN, self.BUTTON_BLUE), self.save_game_button)

        if(self.load_game_button.collidepoint(mouse_position)):
            pygame.draw.rect(self.scr, (self.BUTTON_RED + 50, self.BUTTON_GREEN + 50, self.BUTTON_BLUE + 50), self.load_game_button)
        else:
            pygame.draw.rect(self.scr, (self.BUTTON_RED, self.BUTTON_GREEN, self.BUTTON_BLUE), self.load_game_button)

        self.scr.blit(self.next_round_button_surface, (self.next_round_button.x + 15, self.next_round_button.y + 6))
        self.scr.blit(self.new_board_button_surface, (self.new_board_button.x + 15, self.new_board_button.y + 6))
        self.scr.blit(self.save_game_button_surface, (self.save_game_button.x + 15, self.save_game_button.y + 6))
        self.scr.blit(self.load_game_button_surface, (self.load_game_button.x + 15, self.load_game_button.y + 6))

        pygame.display.update()

    def updateLogs(self):
        font = pygame.font.SysFont('Georgia', 13, bold=True)
        pygame.draw.rect(self.scr, (self.BUTTON_RED, self.BUTTON_GREEN, self.BUTTON_BLUE), self.text_background)

        counter = 0
        for log in self.w.logs:
            if(counter >= self.y):
                break
            text = font.render(log, True, 'White')
            self.scr.blit(text, (self.text_background.x + 5, self.text_background.y + counter*self.HEIGHT))
            counter = counter + 1
