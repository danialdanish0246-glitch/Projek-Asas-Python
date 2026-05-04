tabung = {"jumlah" : 675}
nk_beli = {}
try :
  while True :
      nk_beli_apa = input("masukkan barang nk beli : ")
      harga_barang = float(input(f"masukkan harga barang {nk_beli_apa} : USD"))
      nk_beli[nk_beli_apa] = harga_barang
      nk_tambah_lagi = input("nk tambah lagi (YA/TIDAK): ").upper()
      if nk_tambah_lagi != "YA" :
        break
except :
  print('masukkan nombor yg betul!')
for nk_beli_apa , harga_barang in nk_beli.items() :
  if tabung["jumlah"] >= harga_barang :
    tabung["jumlah"] -= harga_barang
  print(f"{nk_beli_apa:<10} : RM{harga_barang:.2f}" )
print(f"baki yg tinggal ialah RM{tabung["jumlah"]}")
