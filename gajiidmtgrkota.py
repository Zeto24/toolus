#keterangan
gaji = 3901000 + 385000
isaku = 100000
tng_kerja = 85720
dn_pensiun = 42860
keshtn = 171440
t1 = 1 * 1.5 * 1 / 173 * gaji
t2 = 1 * 2 * 1 / 173 * gaji
t3 = 1 * 2 * 1 / 173 * gaji

def bpjs():
    h1 = jumlah_1 * t1
    h2 = jumlah_2 * t2
    h3 = jumlah_3 * t3
    h4 = h1 + h2 + h3
    ha = h1 + h2 + h3 + gaji
    p1 = ha - tng_kerja - isaku
    p2 = ha - keshtn - isaku
    p3 = ha - dn_pensiun - isaku
    p4 = ha - (keshtn + tng_kerja) - isaku
    p5 = ha - (tng_kerja + dn_pensiun) - isaku
    p6 = ha - (keshtn + dn_pensiun) - isaku
    p7 = ha - (keshtn + tng_kerja + dn_pensiun) - isaku

    print("Pilihan: \n1.KETENAGAKERJAAN SAJA\n2.KESEHATAN SAJA\n3.DANA PENSIUN SAJA\n4.KETENAGAKERJAAN & KESEHATAN\n5.KETENAGAKERJAAN & DANA PENSIUN\n6.KESEHATAN & DANA PENSIUN\n7.KETIGANYA\n")
    pilih = input("1.Pilih Nomor: ")
    if pilih == "1":
        p1
        print("\nTotal gaji dipotong BPJS & isaku = \nRp.",int(p1))
    elif pilih == "2":
        p2
        print("\nTotal gaji dipotong BPJS & isaku = \nRp.",int(p2))
    elif pilih == "3":
        p3
        print("\nTotal gaji dipotong BPJS & isaku = \nRp.",int(p3))
    elif pilih == "4":
        p4
        print("\nTotal gaji dipotong BPJS & isaku= \nRp.",int(p4))
    elif pilih == "5":
        p5
        print("\nTotal gaji dipotong BPJS & isaku  = \nRp.",int(p5))
    elif pilih == "6":
        p6
        print("\nTotal gaji dipotong BPJS & isaku = \nRp.",int(p6))
    elif pilih == "7":
        p7
        print("\nTotal gaji dipotong BPJS & isaku = \nRp.",int(p7))
    else:
        print("Pilihan tidak ada")
    print("\nTotal_lembur 1 jam = \nRp.",int(h1),"\n")
    print("\nTotal_lembur 2 jam,dst = \nRp.",int(h2),"\n")
    print("\nTotal lembur keseluruhan = \nRp.",int(h4),"\n")
def utuh():
    h1 = jumlah_1 * t1
    h2 = jumlah_2 * t2
    h3 = jumlah_3 * t3
    h4 = h1 + h2 + h3
    ha = h1 + h2 + h3 + gaji
    hasli = ha - isaku
    print("\nTotal_lembur 1 jam = \nRp.",int(h1),"\n")
    print("\nTotal_lembur 2 jam,dst = \nRp.",int(h2),"\n")
    print("\nTotal lembur keseluruhan = \nRp.",int(h4),"\n")
    print("\nTotal gaji tanpa potongan = \nRp.",int(ha),"\n")
    print("\nTotal gaji dipotong isaku = \nRp.",int(hasli),"\n")
 
 #input
print("*potongan isaku(Rp.100000) bersifat wajib. \n")
jumlah_1 = int(input("Lembur 1 jam : "))
jumlah_2 = int(input("Lembur 2 jam,dst : "))
jumlah_3 = int(input("Lembur hari libur {normalnya 7 jam} : "))
jumlah_4 = str(input("Apakah ada potongan BPJS? 'Y/N' : "))
if jumlah_4 == "Y":
    bpjs()
elif jumlah_4 == "N":
    utuh() 