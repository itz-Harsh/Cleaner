import os
import time as t

os.system('del /f /s /q "C:\\Windows\\Prefetch\\*"')
t.sleep(1)

# %temp%

temp_path = os.path.join(os.environ['USERPROFILE'], 'AppData\\Local\\Temp')
os.system(f'del /f /s /q "{temp_path}\\*"')
t.sleep(1)

# Windows Temp

os.system('del /f /s /q "C:\\Windows\\Temp\\*"')
t.sleep(1)

# Recycle Bin

os.system('rd /s /q "C:\\$Recycle.Bin"')
t.sleep(1)


        