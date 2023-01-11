import webbrowser
import pyautogui
import pandas as pd
from time import sleep
data = pd.read_excel('contacto.xlsx')   ## celular='59173480006'   el codigo de pais en bolivia es 591 seguido 8 numeros 

#cambia los datos del excel con tus contactos

data.head(1) #solo tiene 1 columna con varias lineas OJO la columna se llama (Celular) en el excel

print('Iniciar el envio')
for i in range(len(data)):
  
    celular = data.loc[i,'Celular'].astype(str)
    print(' numero : '+celular)
    # nombre = data.loc[i,'nombre']
  
    mensaje = "*REGISTRATE A NUESTRO CURSO DE PYTHON!!! * "

    webbrowser.open('https://web.whatsapp.com/send?phone=' + celular+'&text='+mensaje)
    sleep(25)  
    pyautogui.press('enter')
    sleep(3)
    pyautogui.hotkey('ctrl', 'w')  # Cerrar la pestaña
    sleep(4)