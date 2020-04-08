import pyautogui
import time
import pygame

count = 0
time.sleep(3)

def chama():
    pygame.init()
    tela = pygame.display.set_mode([300,200])
    pygame.display.set_caption("ACORDAR")
    pygame.mixer.music.load('Gipsy.mp3')
    pygame.mixer.music.play()

    sair = False

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        pygame.display.update()

    pygame.quit()

def verifica():
    try:
        goog = pyautogui.locateOnScreen(r'C:\Users\canan\Desktop\pyautogui\goog.png')
        #print(goog)
        pyautogui.moveTo('goog.png')
        #pyautogui.click('goog.png')
        #pyautogui.rightClick()
        return True
                
    except (RuntimeError, TypeError, NameError):
            time.sleep(3)

while True:
    print ('Verificando... Aguarde')
    if (verifica() == True):
            count+=1
            print('OK ',count," vez")
            time.sleep(2)
            if (count == 10):
                break
    else:
            print('não identificado tentaremos em 10 segundos')
            time.sleep(10)
            chama()
            
