import os

def menu(): #Pilihan pertama
    os.system("clear")
    print("="*5,"TOOLS SEDERHANA","="*5,"\n")
    print("Pilihan :")
    print(" 1. Gunakan Tools")
    print(" 0. Keluar Program")

def pilihan(): #Pilihan kedua
    os.system("clear")
    while True:
        print("="*5,"PILIHAN TOOLS","="*5,"\n")
        print("Pilihan :")
        print("1. Kalkulator")
        print("2. Coming Soon!")
        print("0. Keluar Program")
        pilih = input("Masukan Pilihan : ")
        if pilih == "1":
            kalkulator()
        elif pilih == "2":
            ntah()
        elif pilih == "0":
            os.system("clear")
            break
        else:
            break
def kalkulator(): #Tools 1
    os.system("clear")
    while True:
        print("="*5,"KALKULATOR","="*5,"\n")
        print("1. Pertambahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Kembali")
        print("0. Keluar Program")
        pilih = input("Masukan pilihan : ")
        if pilih == "1":
            os.system("clear")
            tambah()
            print("\n")
            pilih = input("Keluar Program {Y}/{N}? : ")
            if pilih == "Y":
                print("Program berhenti!")
            elif pilih == "N":
                kalkulator()
        elif pilih == "2":
            os.system("clear")
            kurang()
            print("\n")
            pilih = input("Keluar Program {Y}/{N}? : ")
            if pilih == "Y":
                break
            elif pilih == "N":
                kalkulator()
        elif pilih == "3":
            os.system("clear")
            kali()
            print("\n")
            pilih = input("Keluar Program {Y}/{N}? : ")
            if pilih == "Y":
                break
            elif pilih == "N":
                kalkulator()
        elif pilih == "4":
            os.system("clear")
            bagi()
            print("\n")
            pilih = input("Keluar Program {Y}/{N}? : ")
            if pilih == "Y":
                break
            elif pilih == "N":
                kalkulator()
        elif pilih == "5":
            pilihan()
        else:
            break
def ntah(): #Tools 2
    os.system("clear")
    while True:
        print("\nComing Soon!\n")
        pilih = input("Kembali/Keluar Program {Y}/{N} ?: ")
        if pilih == "Y":
            pilihan()
        elif pilih == "N":
            print("Program Berhenti!")
            break
def angka1(): #Input user
    a = input("Masukan angka pertama : ")
    return a
def angka2():
    b = input("Masukan angka kedua   : ")
    return b
def tambah(): #Pertambahan
    for a in angka1():
        int(a)
    for b in angka2():
        int(b)
    c = int(a) + int(b)
    os.system("clear")
    print("="*5,"HASIL","="*5)
    print("\n",a, "+", b, "=", c)
def kurang(): #Pengurangan
    for a in angka1():
        int(a)
    for b in angka2():
        int(b)
    c = int(a) - int(b)
    os.system("clear")
    print("="*5,"HASIL","="*5)
    print("\n",a,"-", b, "=", c)
def kali(): #Perkalian
    for a in angka1():
        int(a)
    for b in angka2():
        int(b)
    c = int(a) * int(b)
    os.system("clear")
    print("="*5,"HASIL","="*5)
    print("\n",a,"x", b, "=", c)    
def bagi(): #Pengurangan
    for a in angka1():
        int(a)
    for b in angka2():
        int(b)
    c = int(a) / int(b)
    os.system("clear")
    print("="*5,"HASIL","="*5)
    print("\n",a,"÷", b, "=", c)        
#Tampilan Awal      
menu()
pilih = input("masukan pilihan : ")
if pilih == "1":
    pilihan()
elif pilih == "0":
    print("Program Berhenti")
else:
    print("Program Berhenti!")