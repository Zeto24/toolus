print("\n====FROM INTEGER TO BINARY WITH ARITHMETIC====")
#input
a = int(input("Masukan Angka : "))
b = int(input("Masukan Angka : "))
#processing
c = a + b
d = a - b
e = a * b
f = a / b #biner tidak dapat dibagi karena hasilnya float
g = c
h = d
i = e
j = f + 0 #untuk f jika hasilnya integer
k = f * 0 #untuk f jika hasilnya negatif
l = int(j + k)
m = float(a)
n = float(b)
#untuk mengubah float menjadi integer dan menjadi 0 apabila angka yang              dihasilkan negatif
print("\n==HASIL BAGI TIDAK AKAN DITAMPILKAN JIKA 0.0==\n")
#output
print("--->", m, "/", n, "=")
if f >= 1:
   if f == 0:
        print("Hasil 0")
   else:
       print("----->", j, "<-----")
       print("{Lebih dari 0.0 atau positif}")
else:
       print("----->", k, "<-----")
       print("{Kurang dari 0.0 atau negatif}")
                
print("\n=======HASIL ARITMATIKA DAN BINARY-NYA========\n")
print("Biner angka pertama       = ",format(a, "08b"))
print("Biner angka kedua         = ",format(b,  "08b"))
print("Hasil setelah ditambahkan = ",format(c, "08b"), "=", g)
print("Hasil setelah dikurangi   = ",format(d, "08b"), "=", h)
print("Hasil setelah dikalikan   = ",format(e, "08b"), "=", i)
print("\n==========FLOAT DIUBAH KE INTEGER=============\n")
print("Hasil pembagian {dalam INTEGER} = ",format(l, "08b"), "=", l)