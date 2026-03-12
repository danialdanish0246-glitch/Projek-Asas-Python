print("---------- SISTEM KASIR KEDAI RUNCIT ----------")

try:
   bilangan_barang = int(input("MASUKKAN BILANGAN BARANG : "))

   total = 0

   for i in range(bilangan_barang):
     print(f"Barang ke{i + 1} : ")
     nama = input("Barang : ")
     harga = float(input(f"Harga {nama} : RM"))
     total = total + harga

   print("\n" + "-" * 30)

   if total > 50 :
    total_semua = total * 0.9
    print("DAPAT 10% DISKOUN")
   else :
    total_semua = total
    print("TAK DAPAT DISKOUN")
except:
  print("SILA MENGIKUT ARAHAN DENGAN BETUL")

print("\n" * 10)
print("RESIT KEDAI RUNCIT")
print("-" * 30)
print(f"HARGA ASAL : RM{ total}")
print(f"HARGA SELEPAS DISKOUN : RM{total_semua}")
print("-" * 30)
print("TERIMA KASIH,DATANG LAGI")
