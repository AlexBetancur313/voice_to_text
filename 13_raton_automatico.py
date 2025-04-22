# Automatizacion


import pyautogui as botMouse
import webbrowser
import random
import time

# webbrowser.open("https://www.youtube.com/@syscursos")
while True:
  print(botMouse.position())
  # random 
  # x = random.randint(400,900)
  # y = random.randint(100,700)
  # botMouse.moveTo(x,y,0.5)
  
  x1 = 1435
  y1 = 274
  x2 = 2112
  y2 = 290
  
  for i in range(10):
    # Pantlla 1
    botMouse.moveTo(x1,y1,0.5)
    botMouse.doubleClick()
    botMouse.hotkey('ctrl', 'c')
    # Pantalla 2
    botMouse.moveTo(x2,y2,0.5)
    botMouse.click()
    botMouse.click()
    botMouse.click()
    botMouse.hotkey('ctrl', 'v')
    
    y1 += 41
    y2 += 20
  
  
  
  time.sleep(10)
  # botMouse.click()
  