import pyautogui
from time import sleep

pyautogui.click(968,542, duration=0.5)
pyautogui.write('Pedro')

pyautogui.click(969,571, duration= 0.5)
pyautogui.write('pedro123')

pyautogui.click(862,597, duration=0.5)

pyautogui.click(968,542, duration=0.5)
pyautogui.write('Pedro')

pyautogui.click(969,571, duration= 0.5)
pyautogui.write('pedro123')

pyautogui.click(862,597, duration=0.5)


with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(711,529, duration=0.5)
        pyautogui.write(produto)

        pyautogui.click(704,553, duration=0.5)
        pyautogui.write(quantidade)

        pyautogui.click(699,581, duration=0.5)
        pyautogui.write(preco)
        
        pyautogui.click(581,737, duration=0.5)

        sleep(1)