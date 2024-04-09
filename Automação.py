import pyautogui
import time
import pandas

pyautogui.press("win")
time.sleep(3)
pyautogui.click(x=776, y=348)
pyautogui.write ("chrome")
pyautogui.press("enter") 
time.sleep(1)  

pyautogui.click(x=163, y=59)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
  
pyautogui.click(x=686, y=376)   
pyautogui.write ("email@gmail.com")
pyautogui.press("tab")
pyautogui.write ("password")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep (4)
pyautogui.press("enter")
time.sleep(1)
 
tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index:
    
    pyautogui.click(x=705, y=257)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha,"obs"])
    pyautogui.press("tab")

    
    pyautogui.press("enter")
    pyautogui.scroll (6000)
    
print ("Automação executada com êxito!")
    



