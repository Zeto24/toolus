t = float(input("Masukan UMK daerah anda : "))
g = float(input("Masukan total gaji      : "))
h = g - t
print("\n===Total hasil Lembur Keseluruhan===")
print("           ===", h ,"===\n")
data = []
i = float(input("masukan angka diatas : "))
data = [i]
print(data)

c1 = 1 * 1.5 * 1 / 173 * t
#print("\ntotal hasil lembur satu jam")
print("\ntotal hasil lembur /satu jam = Rp.",c1,"\n")
c2 = 1 * 2 * 1 / 173 * t
#print("\ntotal hasil lembur dua jam")
print("total hasil lembur /dua jam = Rp.",c2,"\n")
c = data[0] / c1
print("total hasil lembur keseluruhan dibagi total hasil lembur /satujam = \n","\ntotal lembur \n=", c,"\n")
d = data[0] / c2
print("total hasil lembur keseluruhan dibagi total hasil lembur /duajam = \n","\ntotal lembur \n=", d,"\n")
e = c // d
print("pembagian bulat dari\ntotal lembur satu jam dibagi total lembur dua jam = \n","\n=",e)
f = d + e
print("\n*data diatas masih berbentuk float dan akan diubah ke integer di hasil akhir.")
print("*hasil akhir hanya mengambil data hasil dari total lembur dua jam.")
print("\nsudah berapa kali anda lembur?")
print(int(d), "+" ,int(e), "=", int(f), "kali")
 