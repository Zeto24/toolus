while True: #Pengulangan
    #Import File
    import os
    import sys
    scriptpath = "../storage/emulated/0/python/bin.py"
    sys.path.append(os.path.abspath(scriptpath))
    scriptpath = "../storage/emulated/0/python/celcius_conv.py"
    sys.path.append(os.path.abspath(scriptpath))
    #Hiasan
    print("====PROGRAM TOOLS SEDERHANA====")
    print("""
    Pilihan Tools:
        1.Kalkulator Suhu
        2.Kalkulator Biner
        0.Keluar Program
        """)
     #Input
    a = int(input("Masukan pilihan : "))
    #Output
    nilai = a 
    if(nilai == 1):
        import celcius_conv
    elif(nilai == 2):
        import bin
    elif(nilai == 0):
        print("\nKetik 'Y' Untuk Keluar!")
    else:
        print("\nKetik 'Y' Untuk Keluar!")
    print("\t")
    #Pengulangan
    if input("Keluar Program? {Y}: ") == "Y":
        break