import os
import sys
import time
os.system("rm -rf toolus")
os.system("git clone https://github.com/Zeto24/toolus.git")
os.system("clear")
print("-"*30)
print("Tools telah diupdate!")
time.sleep(1)
os.system("cd toolus")
os.system("python toolus.py")