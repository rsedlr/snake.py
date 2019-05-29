import pygame
from config import Config

class Game:
   def __init__(self, display):
      self.display = display
        
   def loop(self):
      clock = pygame.time.Clock()
      snake = Snake(self.display)
      x_change = 0
      y_change = 0
      while True:
         for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
               exit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                  x_change = -Config['snake']['speed']
                  y_change = 0
               elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                  x_change = Config['snake']['speed']
                  y_change = 0
               elif event.key == pygame.K_UP or event.key == pygame.K_w:
                  x_change = 0
                  y_change = -Config['snake']['speed']
               elif event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                  x_change = 0
                  y_change = Config['snake']['speed']
        
         self.display.fill(Config['colors']['black'])
         snake.move(x_change, y_change)
         snake.draw()
         pygame.display.update()
         clock.tick(Config['game']['fps'])

class Snake:
   def __init__(self, display):
      self.x_pos = Config['game']['width'] / 2
      self.y_pos = Config['game']['height'] / 2
      self.display = display

   def draw(self):
      pygame.draw.rect(
         self.display, 
         Config['colors']['green'],
         [
            self.x_pos,
            self.y_pos,
            Config['snake']['height'],
            Config['snake']['width']
         ]
      )

   def move(self, x_change, y_change):
      self.x_pos += x_change
      self.y_pos += y_change

def main():
   display = pygame.display.set_mode(
      (Config['game']['width'], 
       Config['game']['width'])
   )
   pygame.display.set_caption(Config['game']['caption'])
   game = Game(display)
   game.loop()

if __name__ == '__main__':
   main()