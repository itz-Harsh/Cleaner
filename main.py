import os
import time as t

os.system('del /f /s /q "C:\\Windows\\Prefetch\\*"')
t.sleep(1)

# %temp%
path = os.path.expanduser("~")
name = os.path.basename(path)
os.system(f'''del /f /s /q "C:\\Users\\{name}\\AppData\\Local\\Temp\\*"''')
t.sleep(1)

# Windows Temp

os.system('del /f /s /q "C:\\Windows\\Temp\\*"')
t.sleep(1)

# Recycle Bin

os.system('rd /s /q "C:\\$Recycle.Bin"')
t.sleep(1)


        