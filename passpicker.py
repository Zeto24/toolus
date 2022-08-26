#modul yang dibutuhkan
import random
import string
import sys
import os
import time
#def fungsi
def p():
#bebas ubah isi dalam tanda kurung dengan tipe string apapun
    alphabet1 = random.choice(string.hexdigits)
    alphabet2 = random.choice(string.ascii_uppercase)
    alphabet3 = random.choice(string.ascii_lowercase)
    alphabet4 = random.choice(string.ascii_lowercase)
    alphabet5 = random.choice(string.ascii_lowercase)
    alphabet6 = random.choice(string.ascii_lowercase)
    hex = random.choice(string.hexdigits)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)    
#bebas mengubah urutan'nya'
    password = alphabet1 + alphabet2 + hex + alphabet3 + alphabet4 + alphabet5 + alphabet6 + str(number) + special_char
    print(" --> %s" % password)
    print("\n")
#ini header   
title = """
  _____                        _      _    
 |  __ \                      (_)    | |   
 | |__) |_ _ ___ ___     _ __  _  ___| | __
 |  ___/ _` / __/ __|   | '_ \| |/ __| |/ /
 | |  | (_| \__ \__ \   | |_) | | (__|   < 
 |_|   \__,_|___/___/   | .__/|_|\___|_|\_\\
                  ______| |                
                 |______|_|                
                                  
 Welcome to password picker!"""

#loading efek
for i in title:
    time.sleep(0.004)
    sys.stdout.write(i)
    sys.stdout.flush()
#ini header dengan warna
time.sleep(0.009)        
os.system("clear")
print("\033[2;31;40m",title,"\033[0;0m")
#percabangan dalam perulangan
while True:
    print("\n","_"*43)
    response = input("\n Lanjut? Ketik 'y atau n' : ")
    print("\n","_"*43)
    response = response.lower()
    if response == "n":
        sys.exit(1)
    elif response == "y":
        n = int(input("\n Mau berapa jumlah yang dihasilkan? : "))
        print("\n","_"*43)
        print(f"\n [{n}]Password yang dihasilkan: \n")
        for i in range(n):
            p()
    else:
        print(" Mohon masukan input anda!")
        time.sleep(1)