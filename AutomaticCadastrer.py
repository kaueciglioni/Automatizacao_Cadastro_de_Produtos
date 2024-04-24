import pyautogui
from time import sleep
#0  REALIZAR CADASTRP
pyautogui.click(1017,623,duration=0.2)
# 1 - Clicar e digitar meu usuário
pyautogui.click(1015,541,duration=0.2)
pyautogui.write('kaue.ciglioni')
# 2 - Clicar e digitar minha senha
pyautogui.click(1046,582,duration=0.2)
pyautogui.write('12345678')
#CLICAR EM CADASTRAR
pyautogui.click(826,626,duration=0.2)

# 1 - Clicar e digitar meu usuário
pyautogui.click(1015,541,duration=0.5)
pyautogui.write('kaue.ciglioni')
# 2 - Clicar e digitar minha senha
pyautogui.click(1046,582,duration=0.5)
pyautogui.write('12345678')
# 3 - Clicar em entrar
pyautogui.click(826,626,duration=0.5)
# 4 - Extrair cada produto
with open('produtos.txt','r') as arquivo:
#   4.1 - clicar e digitar produto
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #   4.2 - clicar e digitar produto
        pyautogui.click(588,522,duration=0.1)
        pyautogui.write(produto)
        #   4.3 clicar e digitar quantidade
        pyautogui.click(587,561,duration=0.1)
        pyautogui.write(quantidade)
        #    4.3 - clicar e digitar preço
        pyautogui.click(593,601,duration=0.1)
        pyautogui.write(preco)
        #    4.5 clicar em registrar
        pyautogui.click(407,837,duration=0.1)
        sleep(1)