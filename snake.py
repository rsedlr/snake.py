import pygame, random
from config import Config

class Game:
   def __init__(self, display):
      self.display = display
      self.score = 0
        
   def loop(self):
      clock = pygame.time.Clock()
      snake = Snake(self.display)
      apple = Apple(self.display)
      self.score = 0
      x_change = 0
      y_change = 0
      bumper_x = Config['game']['width'] - Config['game']['bumper_size']
      bumper_y = Config['game']['height'] - Config['game']['bumper_size']
      pygame.font.init()
      font = pygame.font.SysFont('Arial', 25, bold=True)
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
        
         self.display.fill(Config['colors']['grey'])
         pygame.draw.rect(
            self.display, 
            Config['colors']['black'], [
               Config['game']['bumper_size'],
               Config['game']['bumper_size'],
               Config['game']['height'] - Config['game']['bumper_size'] * 2,
               Config['game']['width'] - Config['game']['bumper_size'] * 2
            ]
         )
         apple_rect = apple.draw()
         snake.move(x_change, y_change)
         score = font.render('Score: {}'.format(self.score), True, Config['colors']['white'])
         score_rect = score.get_rect(
            center=(Config['game']['width'] + 30, 40)
         )
         self.display.blit(score, score_rect)
         snake_rect = snake.draw()

         if (snake.x_pos < Config['game']['bumper_size'] or snake.y_pos < Config['game']['bumper_size'] or 
               snake.x_pos + Config['snake']['width'] > bumper_x or 
               snake.y_pos + Config['snake']['height'] > bumper_y ):
            self.loop()

         if len(snake.body) >= 1:
               for cell in snake.body:
                  if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
                     self.loop()

         if apple_rect.colliderect(snake_rect):
            apple.randomize()
            self.score += 1
            snake.eat()

         pygame.display.update()
         clock.tick(Config['game']['fps'])

class Snake:
   def __init__(self, display):
      self.x_pos = (Config['game']['width']) / 2
      self.y_pos = (Config['game']['height']) / 2
      self.display = display
      self.body = []
      self.max_size = 0

   def draw(self):
      for item in self.body:
         pygame.draw.rect(
               self.display, 
               Config['colors']['green'],
               [
                  item[0],
                  item[1],
                  Config['snake']['width'],
                  Config['snake']['height']
               ]
         )
      return pygame.draw.rect(
         self.display, 
         Config['colors']['green'],
         [
            self.x_pos,
            self.y_pos,
            Config['snake']['height'],
            Config['snake']['width']
         ]
      )
   
   def eat(self):
      self.max_size += 1

   def move(self, x_change, y_change):
      self.body.append((self.x_pos, self.y_pos))
      self.x_pos += x_change
      self.y_pos += y_change

      if len(self.body) > self.max_size:
         del(self.body[0])


class Apple:
   def __init__(self, display):
      self.x_pos = 0
      self.y_pos = 0
      self.display = display
      self.randomize()

   def randomize(self):
      height = Config['game']['height']
      width = Config['game']['width']
      bumper = Config['game']['bumper_size']
      max_x = (width - bumper - Config['snake']['width'])
      max_y = (height - bumper - Config['snake']['height']) 
      self.x_pos = round(random.randint(bumper, max_x) / 20) * 20
      self.y_pos = round(random.randint(bumper, max_y) / 20) * 20
         
   def draw(self):
      return pygame.draw.rect(
         self.display, 
         Config['colors']['red'],
         [
            self.x_pos,
            self.y_pos,
            Config['apple']['height'],
            Config['apple']['width']
         ]
      )

def main():
   display = pygame.display.set_mode(
      (Config['window']['width'], 
       Config['game']['height'])
   )
   pygame.display.set_caption(Config['game']['caption'])
   game = Game(display)
   game.loop()


if __name__ == '__main__':
   main()

