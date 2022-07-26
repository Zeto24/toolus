import os
import sys
import time

def menu(): #Pilihan pertama
    os.system("clear")
    print("="*5,"TOOLS SEDERHANA","="*5,"\n")
    print("Pilihan :")
    print(" 1. Gunakan Tools")
    print(" 0. Keluar Program")

def pilihan(): #Pilihan kedua
    while True:
        os.system("clear")
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
            os.exit(1)
        else:
            print("\n","!"*3,"Mohon masukan input anda","!"*3,"\n")
            time.sleep(1)
            pilihan()
def kalkulator(): #Tools 1
    while True:
        os.system("clear")
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
            pilih = input("Mulai lagi? 'Y/N' ? : ")
            if pilih == "Y":
                kalkulator()
            elif pilih == "N":
                break
        elif pilih == "2":
            os.system("clear")
            kurang()
            print("\n")
            pilih = input("Mulai lagi? 'Y/N' ? : ")
            if pilih == "Y":
                kalkulator()
            elif pilih == "N":
                break
        elif pilih == "3":
            os.system("clear")
            kali()
            print("\n")
            pilih = input("Mulai lagi? 'Y/N' ? : ")
            if pilih == "Y":
                kalkulator()
            elif pilih == "N":
                break
        elif pilih == "4":
            os.system("clear")
            bagi()
            print("\n")
            pilih = input("Mulai lagi? 'Y/N' ? : ")
            if pilih == "Y":
                kalkulator()
            elif pilih == "N":
                break
        elif pilih == "5":
            pilihan()
        else:
            print("\n","!"*3,"Mohon masukan input anda","!"*3,"\n")
            time.sleep(1)
            break
def ntah(): #Tools 2
    os.system("clear")
    while True:
        print("\nComing Soon!\n")
        pilih = input("Kembali? 'Y/N' ?: ")
        if pilih == "Y":
            pilihan()
        elif pilih == "N":
            os._exit(1)
        else:
            print("\n","!"*3,"Mohon masukan input anda","!"*3,"\n")
            time.sleep(1)
            break
def tambah(): #Pertambahan
        a = int(input("Masukan angka pertama : "))
        b = int(input("Masukan angka kedua   : "))
        c = a + b
        os.system("clear")
        print("="*5,"HASIL","="*5)
        print("\n",a,"+",b, "=",c)
def kurang(): #Pengurangan
    a = int(input("Masukan angka pertama : "))
    b = int(input("Masukan angka kedua   : "))
    c = a - b
    os.system("clear")
    print("="*5,"HASIL","="*5)
    print("\n",a,"-", b, "=", c)
def kali(): #Perkalian
    a = int(input("Masukan angka pertama : "))
    b = int(input("Masukan angka kedua   : "))
    c = a * b
    os.system("clear")
    print("="*5,"HASIL","="*5)
    print("\n",a,"x", b, "=", c)    
def bagi(): #Pengurangan
    a = int(input("Masukan angka pertama : "))
    b = int(input("Masukan angka kedua   : "))
    c = a / b
    os.system("clear")
    print("="*5,"HASIL","="*5)
    print("\n",a,"÷", b, "=", c)        
#Tampilan Awal  
while True:    
    menu()
    pilih = input("masukan pilihan : ")
    if pilih == "1":
        pilihan()
    elif pilih == "0":
        print("\n","="*10,"Program Berhenti","="*10)
        break
    else:
        print("\n","!"*3,"Mohon masukan input anda","!"*3,"\n")
        time.sleep(1)