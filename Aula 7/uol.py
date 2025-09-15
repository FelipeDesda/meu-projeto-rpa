import cv2
import pyautogui
import time

print(pyautogui.size())
print(pyautogui.position())

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

def setup():
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.write('https://uol.com.br')
    pyautogui.press('enter')
    time.sleep(2)
    botao = pyautogui.locateOnScreen('uol_logo.png')
    time.sleep(2)
    if botao is None:
        raise Exception("Logo do UOL não encontrado")
    
def preencher_formulario(dados):
    """Preenche o formulário com os dados fornecidos."""
    print("Preenchendo formulário com dados")

def aguardar_elemento(imagem, max_tentativas=10):
    tentativas=0
    while tentativas < max_tentativas:
        try:
            pos = pyautogui.locateOnScreen(imagem)
            return pos
        except:
            tentativas += 1
            time.sleep(1)
    raise Exception("Timout aguardando elemento")

def vertificar_sucesso():
    print("Verificando sucesso da operação...")
    return True

def main():
    dados = {
        'nome':'João Silva',
        'email': 'joao@exemplo.com',
    }
    setup()
    preencher_formulario(dados)
if __name__ == "__main__":
    main()                
