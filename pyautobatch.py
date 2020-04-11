import pyautogui, time, pygame

count = 0
espera = 0
print('Copiar o *S ENTER* iniciando em 5 segundos')
time.sleep(6)

def chamamusica():
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
        pyautogui.locateOnScreen('meliuz.png')
        pyautogui.moveTo('meliuz.png')
        pyautogui.click()
        pyautogui.moveTo(x=1169, y=241)
        pyautogui.click()
        #pyautogui.rightClick()
        return True

    except (RuntimeError, TypeError, NameError):
        time.sleep(1)
            
while True:
    print ('Verificando... Aguarde')
    if (verifica() == True):
        count+=1
        espera = 0
        print('identificado ',count," vez")
        time.sleep(3)
        if (count == 10):
            break
        
    else:
        espera+=1
        if (espera >= 75):
            chamamusica()
        else:
            time.sleep(12)
            print ('não identificado, esperado (',(espera*12), ' segundos)')
            
