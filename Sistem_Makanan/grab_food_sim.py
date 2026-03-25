print("------Sistem Grab Food Ringkas------")
nasi_lemak = 5
burger = 10
kfc = 15
cas = 4
try:
   nasi_lemak1 = int(input("MASUKKAN KUANTITI NASI LEMAK: "))
   burger1 = int(input("MASUKKAN KUANTITI BURGER: "))
   kfc1 = int(input("MASUKKAN KUANTITI KFC: "))

   jumlah = ((nasi_lemak1 * 5)+(burger1 * 10)+(kfc1 * 15))

   if jumlah > 30 :
    jumlah = jumlah
   else :
    jumlah +=4
except:
  print("MASUKKAN KUATITI SAHAJA")



print(f"HARGA : RM{jumlah}")
