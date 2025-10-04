import pygame
from ffpyplayer.player import MediaPlayer
import random
import random
import csv
import time

button6Setting = "5m"
def play_video(path):
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Video Player")
    clock = pygame.time.Clock()

    player = MediaPlayer(path)

    while True:
        frame, val = player.get_frame()

        if val == 'eof':    
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.close_player()
                pygame.quit()
                return

        if frame is not None:
            img, _ = frame
            w, h = img.get_size()
            data = img.to_bytearray()[0]
            surface = pygame.image.frombuffer(data, (w, h), 'RGB')
            surface = pygame.transform.scale(surface, (640, 480))
            screen.blit(surface, (0, 0))
            pygame.display.flip()

        clock.tick(24)

def pngLoader(image_path, screen_size=(1280, 720), image_position=(0, 0)):

    pygame.init()

    image = pygame.image.load(image_path).convert_alpha()

    image_width, image_height = image.get_size()
    screen_width, screen_height = screen_size
    scale_factor = min(screen_width / image_width, screen_height / image_height)
    new_width = int(image_width * scale_factor)
    new_height = int(image_height * scale_factor)
    image = pygame.transform.smoothscale(image, (new_width, new_height))
    
    screen_size =(new_width, new_height)


    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("LIKE A WHAT?")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(image, image_position)

        pygame.display.flip()

    pygame.quit()


def likeaDragon(roll=(random.randint(1,4))):
    if roll == 1:
        pngLoader("peak\saythatAgain.png")
    elif roll == 2:
        pngLoader("peak/likeawhat.png")
    elif roll == 3:
        pngLoader("peak/date.png")
    elif roll == 4:
        pngLoader("peak/howdragon.png")
def button_time(rect, colour, text, font, text_colour):
   button = pygame.Surface((rect.width, rect.height))
   pygame.draw.rect(button, colour ,button.get_rect())
   buttonText = font.render(text, True, text_colour)
   textLocation = buttonText.get()
   button.blit(buttonText, textLocation)
   return button



def update_settings(settingOne, settingTwo):
    data_to_write =  [[settingOne]]
    with open('Settings.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data_to_write)
    data_to_write =  [[settingTwo]]
    with open('Settings.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data_to_write)

def QuiteHungry(roll=(random.randint(1,3))):
    print(roll)
    if roll == 1:
        return "peak/background.jpg"
    elif roll == 2:
        return "peak/background2.jpg"
    elif roll == 3:
        return "peak/background3.jpg"

#cameraSettings = [[button4Setting, button6Setting]]
 #              with open('Settings.csv', 'w') as file:
  #                csv_writer = csv.writer(file)
   #               csv_writer.writerows(cameraSettings)
    #              button5_colour = (0, 255, 60)
     #             #print("does this work?")
      #            button5_Check = time.time()