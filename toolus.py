while True: #Pengulangan
    #Import File
    import os
    import sys
    import time
    #scriptpath = "../storage/emulated/0/python/toolus.py"
#    sys.path.append(os.path.abspath(scriptpath)).
#    scriptpath = "../storage/emulated/0/python/bin.py"
#    sys.path.append(os.path.abspath(scriptpath))
#    scriptpath = "../storage/emulated/0/python/celcius_conv.py"
#    sys.path.append(os.path.abspath(scriptpath))
#    scriptpath = "../storage/emulated/0/python/hitunglembur.py"
#    sys.path.append(os.path.abspath(scriptpath))
#    scriptpath = "../storage/emulated/0/python/updatetools.py"
#    sys.path.append(os.path.abspath(scriptpath))
    #Hiasan
    print("====PROGRAM TOOLS SEDERHANA====")
    print("""
    Pilihan Tools:
        1.Kalkulator Suhu
        2.Kalkulator Biner
        3.Hitung Lemburan
        0.Keluar Program
        """)
     #Input
    a = input("Masukan pilihan : ")
    #Output
    nilai = a 
    if nilai == "1":
        import celcius_conv
    elif nilai == "2":
        import bin
    elif nilai == "3":
        import hitunglembur
    #elif nilai == "a":
        #import updatetools
    elif nilai == "0":
        os.system("clear")
        print("\nProgram Berhenti!")
        break
    else:
        print("\nMohon Masukan Input Anda!")
        time.sleep(1)
        os.system("clear")
        import toolus
    #Pengulangan
    pilih = input("\n\nMulai lagi? 'Y/N' : ")
    if pilih == "Y":
        os.system("clear")
        import toolus
    elif pilih == "N":
        os.system("clear")
        print("\nProgram Berhenti")
        break
    else:
        print("\nMohon Masukan Input Anda!")
        time.sleep(1)
        import toolus