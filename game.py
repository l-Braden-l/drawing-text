# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True



txt_font = pygame.font.SysFont("Ariel", 30, bold = True, italic = True)
#-------------------------------------------------

def draw_text(text,font,text_col,x,y):
   render_txt = font.render(text, True, text_col)
   screen.blit(render_txt, (x,y))







#--------------------------------------------------
def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here
   running = True
   while running:
      running = handle_events()
      screen.fill(config.WHITE) # Use color from config

      draw_text("Hello World",txt_font, (0,0,0), 220, 150)

      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()