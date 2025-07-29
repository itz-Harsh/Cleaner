import os
import pyautogui as gui
import time as t


# Prefetch

os.system("start C:\\Windows\\Prefetch")
t.sleep(1)
gui.click(500, 600)
gui.hotkey('ctrl', 'a')
gui.press('delete')
t.sleep(1)
gui.press('esc')
t.sleep(1)
gui.press('enter')




# Temp

os.system("start C:\\Windows\\Temp")
t.sleep(1)
gui.click(500, 600)
gui.hotkey('ctrl', 'a')
gui.press('delete')
t.sleep(1)
gui.press('esc')
t.sleep(1)
gui.press('enter')




# %temp%

path = os.path.expanduser("~")
name = os.path.basename(path)
print(name)
os.system(f"start C:\\Users\\{name}\\AppData\\Local\\Temp")
t.sleep(1)
gui.click(500, 600)
gui.hotkey('ctrl', 'a')
gui.press('delete')
t.sleep(1)
gui.press('esc')
t.sleep(1)
gui.press('enter')




#Recycle Bin

os.system("start shell:RecycleBinFolder")
t.sleep(1)
gui.click(500, 0)
gui.hotkey('ctrl', 'a')
gui.press('delete')
gui.press('enter')
os.system("taskkill /f /im explorer.exe")
os.system("start explorer.exe")