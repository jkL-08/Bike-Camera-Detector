import pygame
from ffpyplayer.player import MediaPlayer
from peaker import play_video
from peaker import pngLoader
from peaker import likeaDragon
from peaker import update_settings
from peaker import QuiteHungry
import random
import csv
import time
import subprocess
#big true
pygame.init()

#trying to make the settings variables load from the csv so they are consistant upon reload
#with open("Settings.csv", "r", newline="") as file:
#  csv_reader = csv.reader(file)
#   
#   #https://stackoverflow.com/questions/36088176/assign-a-variable-to-each-row-in-a-csv-file, used but not very helpful
#   rows = list(csv.reader(file))
#   button4Setting = rows[0]
#   button6Setting = rows[1]
#   print(button4Setting)
#comes up as ['Bike'] so need to remove the '' and [] but not sure how

 
button4Setting = "Bike"
button6Setting = "5m"
setting1 = button4Setting 
setting2 = button6Setting     

button5_Check = None
menuPage = 'main'


#UI Specifications
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))#, pygame.RESIZABLE)   #makes ui resizeable, want to do this but no idea how to resize background and buttons in real time
pygame.display.set_caption("Falling down a hill simulator")
icon = pygame.image.load("peak/numberOne.png") 
pygame.display.set_icon(icon)

set_width = 1280
set_height = 720
buttonScaleW = screen_width/set_width
buttonScaleH = screen_height/set_height


#Button Specifications
#button_rect = pygame.Rect((900*buttonScaleW), 200*buttonScaleH, 200*buttonScaleW, 50*buttonScaleH)#moves the button to where i want it when ui size different, does not update however
#button_colour = (228, 207, 123 )
#button_text_colour = (255, 255, 255)
font = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
#button_text = font.render("Video Test", True, button_text_colour)
#text_rect = button_text.get_rect(center=button_rect.center)

button2_rect = pygame.Rect(900, 200, 200, 50)
button2_colour = (255, 187, 36)
button2_text_colour = (255, 255, 255)
font2 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button2_text = font2.render("Camera", True, button2_text_colour)
text2_rect = button2_text.get_rect(center=button2_rect.center)

button3_rect = pygame.Rect(900, 300, 200, 50)
button3_colour = (228, 207, 123 )
button3_text_colour = (255, 255, 255)
font3 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button3_text = font3.render("QUIT", True, button3_text_colour)
text3_rect = button3_text.get_rect(center=button3_rect.center)

button4_rect = pygame.Rect(540, 200, 200, 50)
button4_colour = (228, 207, 123 )
button4_text_colour = (255, 255, 255)
font4 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button4_text = font4.render(button4Setting, True, button4_text_colour)
text4_rect = button4_text.get_rect(center=button4_rect.center)

button5_rect = pygame.Rect(900, 250, 200, 50)
button5_colour = (228, 207, 123 )
button5_text_colour = (255, 255, 255)
font5 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button5_text = font5.render("Settings", True, button5_text_colour)
text5_rect = button5_text.get_rect(center=button5_rect.center)

button6_rect = pygame.Rect(540, 250, 200, 50)
button6_colour = (228, 207, 123 ) 
button6_text_colour = (255, 255, 255)
font6 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button6_text = font6.render(button6Setting, True, button6_text_colour)
text6_rect = button6_text.get_rect(center=button6_rect.center)

button7_rect = pygame.Rect(900, 500, 200, 50)
button7_colour = (228, 207, 123 )
button7_text_colour = (255, 255, 255)
font7 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button7_text = font7.render("Return", True, button7_text_colour)
text7_rect = button7_text.get_rect(center=button7_rect.center)

button8_rect = pygame.Rect(540, 360, 200, 50)
button8_colour = (228, 207, 123 )
button8_text_colour = (255, 255, 255)
font8 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button8_text = font8.render("Yes", True, button8_text_colour)
text8_rect = button8_text.get_rect(center=button8_rect.center)

button9_rect = pygame.Rect(540, 310, 200, 50)
button9_colour = (228, 207, 123 )
button9_text_colour = (255, 255, 255)
font9 = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
button9_text = font9.render("No", True, button9_text_colour)
text9_rect = button9_text.get_rect(center=button9_rect.center)

#yay text time :(
rectConfirm = pygame.Rect(350, 250, 600, 100)
fontConfirm = pygame.font.Font("peak/AlexanderQuill.ttf", 36)
textConfirm = fontConfirm.render("Are you sure you want to change settings?", True, (255, 255, 255))

#load a logo image
logo = pygame.image.load("peak/goat.png").convert_alpha()
logo_width, logo_height = logo.get_size()
logo = pygame.transform.scale(logo, (int(logo_width * 0.3), int(logo_height * 0.3)))
logo_rect = pygame.Rect(950, 40, 200, 50)
#logo = pygame.image.load("peak/logo.png").convert_alpha()
#logo_width, logo_height = logo.get_size()
#logo = pygame.transform.scale(logo, (int(logo_width * 0.5), int(logo_height * 0.5)))
#logo_rect = pygame.Rect(837, 50, 200, 50)


#want to make ui resizable, i know that if i take the screen size and the image size and divide to change size you can do something but nothing after that.
def resize_background(image, screenSize):
   bg_width, bg_height = image.getsize()
   target_height, target_width = screenSize
   bg_width/target_height

#make the background an random image
backgrounder = QuiteHungry()
print(backgrounder)
background = pygame.image.load(backgrounder).convert()
background = pygame.transform.scale(background, (screen_width, screen_height))

#play music
pygame.mixer.music.load("peak/Saint Barbara Theme.mp3")
pygame.mixer.music.play(-1)

#when a button is clicked it should play a noise now
buttonNoise = pygame.mixer.Sound("peak/Gong.mp3")
buttonNoise.set_volume(5.0)

def Pressed():
   buttonNoise.play()

running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Video Test
            #if button_rect.collidepoint(event.pos):
            #   play_video("peak\There's a Platypus Controlling Me _ Music Video _ Phineas and Ferb _  _@disneychannel_.mp4")
            if button2_rect.collidepoint(event.pos):
               subprocess.Popen(['python', 'cameraThing/thingy'])#might have to add .py to the end of thingy, does work for me but maybe if you have it displaying .py it might need it
               pygame.quit()
            elif button3_rect.collidepoint(event.pos):
               pygame.quit()
               quit()
            #Movement Type Setting (Don't know if this will do anything)
            elif button4_rect.collidepoint(event.pos):
               if button4Setting == "Bike":
                   button4Setting = "Scooter"
               elif button4Setting == "Scooter":
                  button4Setting = "Walk"
               elif button4Setting == "Walk":
                 button4Setting = "Bike"
               button4_text = font4.render(button4Setting, True, button4_text_colour)
               text4_rect = button4_text.get_rect(center=button4_rect.center)
            #Settings Page Hopfully
            elif button5_rect.collidepoint(event.pos):
               menuPage = "setting"
               Pressed()
            #Distance Setting
            elif button6_rect.collidepoint(event.pos):
               if button6Setting == "5m":
                   button6Setting = "10m"
               elif button6Setting == "10m":
                  button6Setting = "20m"
               elif button6Setting == "20m":
                 button6Setting = "5m"
               button6_text = font6.render(button6Setting, True, button6_text_colour)
               text6_rect = button6_text.get_rect(center=button6_rect.center)
            #Main Page Hopfully
            elif button7_rect.collidepoint(event.pos):
               menuPage = "confirm"
            #No to changing settings
            elif button8_rect.collidepoint(event.pos):
               menuPage = "main"
               button4Setting = setting1 
               button6Setting = setting2
               setting1 = button4Setting
            #Yes to changing settings
            elif button9_rect.collidepoint(event.pos):
               menuPage = "main"
               setting1 = button4Setting
               setting2 = button6Setting
               update_settings(button4Setting, button6Setting)

    screen.blit(background, (0, 0))

    #if button_rect.collidepoint(pygame.mouse.get_pos()):
    #   button_colour = (228, 207, 123)
    #   button_text_colour = (0, 0, 0)
    #else:
    #    button_colour = None
    #    button_text_colour = (255, 255, 255)
   #I dont know how to change the text colour and have a button be clear without rerendering the text or how to make a class that changes the variables being used at the same time
    #button_text = font.render("Video Test", True, button_text_colour)
    #text_rect = button_text.get_rect(center=button_rect.center)

    if button2_rect.collidepoint(pygame.mouse.get_pos()):
       button2_colour = (228, 207, 123)
       button2_text_colour = (0, 0, 0)
    else:
        button2_colour = None
        button2_text_colour = (255, 255, 255)

    button2_text = font.render("Camera", True, button2_text_colour)
    text2_rect = button2_text.get_rect(center=button2_rect.center)  

    if button3_rect.collidepoint(pygame.mouse.get_pos()):
       button3_colour = (228, 207, 123)
       button3_text_colour = (0, 0, 0)
    else:
        button3_colour = None
        button3_text_colour = (255, 255, 255)

    button3_text = font.render("Quit", True, button3_text_colour)
    text3_rect = button3_text.get_rect(center=button3_rect.center)
   
    if button4_rect.collidepoint(pygame.mouse.get_pos()):
       button4_colour = (228, 207, 123)
       button4_text_colour = (0, 0, 0)
    else:
        button4_colour = None
        button4_text_colour = (255, 255, 255)

    button4_text = font.render(button4Setting, True, button4_text_colour)
    text4_rect = button4_text.get_rect(center=button4_rect.center)
   
    if button5_rect.collidepoint(pygame.mouse.get_pos()):
        button5_colour = (228, 207, 123)
        button5_text_colour = (0, 0, 0)
    else:
        button5_colour = None
        button5_text_colour = (255, 255, 255)

    button5_text = font.render("Settings", True, button5_text_colour)
    text5_rect = button5_text.get_rect(center=button5_rect.center)
      
    if button6_rect.collidepoint(pygame.mouse.get_pos()):
       button6_colour = (228, 207, 123)
       button6_text_colour = (0, 0, 0)
    else:
        button6_colour = None
        button6_text_colour = (255, 255, 255)

    button6_text = font.render(button6Setting, True, button6_text_colour)
    text6_rect = button6_text.get_rect(center=button6_rect.center)

    if button7_rect.collidepoint(pygame.mouse.get_pos()):
       button7_colour = (228, 207, 123)
       button7_text_colour = (0, 0, 0)
    else:
        button7_colour = None
        button7_text_colour = (255, 255, 255)

    button7_text = font.render("Return", True, button7_text_colour)
    text7_rect = button7_text.get_rect(center=button7_rect.center)

    if button8_rect.collidepoint(pygame.mouse.get_pos()):
       button8_colour = (228, 207, 123)
       button8_text_colour = (0, 0, 0)
    else:
        button8_colour = None
        button8_text_colour = (255, 255, 255)

    button8_text = font.render("No", True, button8_text_colour)
    text8_rect = button8_text.get_rect(center=button8_rect.center)

    if button9_rect.collidepoint(pygame.mouse.get_pos()):
       button9_colour = (228, 207, 123)
       button9_text_colour = (0, 0, 0)
    else:
        button9_colour = None
        button9_text_colour = (255, 255, 255)

    button9_text = font.render("Yes", True, button9_text_colour)
    text9_rect = button9_text.get_rect(center=button9_rect.center)
#load that logo
    screen.blit(background, (0, 0))
    screen.blit(logo, logo_rect)
      
#chnage what buttons load depended on menuPage
    if menuPage == "main":
    #  if button_colour:
    #     pygame.draw.rect(screen, button_colour, button_rect)
    #  screen.blit(button_text, text_rect)
    
      if button2_colour:
         pygame.draw.rect(screen, button2_colour, button2_rect)
      screen.blit(button2_text, text2_rect)

      if button3_colour:
         pygame.draw.rect(screen, button3_colour, button3_rect)
      screen.blit(button3_text, text3_rect)

      if button5_colour:
         pygame.draw.rect(screen, button5_colour, button5_rect)
      screen.blit(button5_text, text5_rect)

    elif menuPage == 'setting':
      dim = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
      dim.fill((0, 0, 0, 150))
      screen.blit(dim, (0,0))

      if button6_colour:
         pygame.draw.rect(screen, button6_colour, button6_rect)
      screen.blit(button6_text, text6_rect)

      if button4_colour:
         pygame.draw.rect(screen, button4_colour, button4_rect)
      screen.blit(button4_text, text4_rect)

      if button7_colour:
         pygame.draw.rect(screen, button7_colour, button7_rect)
      screen.blit(button7_text, text7_rect)
   
    elif menuPage == 'confirm':
      dim = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
      dim.fill((0, 0, 0, 150))
      screen.blit(dim, (0,0))

      if button8_colour:
         pygame.draw.rect(screen, button8_colour, button8_rect)
      screen.blit(button8_text, text8_rect)

      if button9_colour:
         pygame.draw.rect(screen, button9_colour, button9_rect)
      screen.blit(button9_text, text9_rect)

      screen.blit(textConfirm, rectConfirm)
         
    pygame.display.flip()  

pygame.quit()
quit()