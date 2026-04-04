tabung = {"jumlah" : 520}
nk_beli = ['mouse' , 'keyboard']
harga = {'mouse' : 100 , 'keyboard' : 120}

try :
  print("=== SISTEM SIMPANAN DANIAL v1.0 ===")
  print(f"NAK BELI : {nk_beli}")
  while True :
    print(f"BAKI TABUNG : RM{tabung["jumlah"]}")

    print("\nMenu:")
    print("1. Tambah Simpanan Harian")
    print("2. Tambah Barang ke Wishlist")
    print("3. Keluar & Simpan")

    pilihan = int(input("MASUKKAN PILIHAN MENU (1-3) : "))

    if pilihan == 1 :
      nilai = float(input("MASUKKAN BERAPA DUIT NAK MASUK DALAM TABUNG : RM"))
      tabung["jumlah"] += nilai
      print(f"SYABAS! BERJAYA SIMPAN RM{nilai} KE DALAM TABUNG.")
    elif pilihan == 2 :
      while True :
        barang = input("NAK TAMBAH BARANG APA : ")
        harga_unit = float(input(f"MASUKKAN HARGA {barang} : RM"))
        harga[barang] = harga_unit
        nk_beli.append(barang)
        if input("NAK TAMBAH BARANG LAGI (YA/TIDAK) :").upper() != "YA" :
          break
      for item in nk_beli :
        nilai_harga = harga[item]
        print(f"{item:<10}: RM{nilai_harga:.2f}")
    elif pilihan == 3 :
        print("Program tamat. Teruskan menabung untuk LOQ!")
        break
        
    else:
        print("Pilihan tak sah, cuba lagi.")
except :
  print("MASUKKAN NOMBOR ATAU HURUF PADA RUANG YANG BETUL!")
