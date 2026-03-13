print("========================================")
print("     SELAMAT DATANG KE SUPER-APP DANIAL ")
print("========================================")


print("1. Sistem Kira Zakat")
print("2. Sistem Grab Food Ringkas")
print("3. Sistem Tiket Wayang")
print("4. Keluar") 

try:
    pilihan = int(input("Sila pilih menu (1-4) : "))

    if pilihan == 1 :
      print("------Sistem Kira Zakat------")
      nama = input("Masukkan nama anda : ")
      gaji = int(input("Masukkan gaji anda : "))
      if gaji < 2500 :
        print("Tidak perlu bayar zakat")
      else :
        print("Sila bayar zakat")
    elif pilihan == 2 :
      print("------ Sistem Grab Food Ringkas------")

      menu = {
       "Nasi lemak" : 2.00,
       "Burger ayam" : 5.00,
       "Burger daging" : 5.50,
       "Pizza" : 8.00,
       "Kebab" : 5.00
      }

      bakul = {}
      total = 0

      try : 
           for makanan , harga in menu . items() :
               kuantiti = int(input(f"Masukkan berapa unit {makanan} (RM{harga:.2f}): "))
    
               if kuantiti > 0 :
                  bakul[makanan] = kuantiti
                  total += harga * kuantiti

               caj = 4
               if total > 30 :
                  caj = 0
                  penghantaran = "Percuma (promosi > RM30)"
               else :
                   caj = 4
                   penghantaran = f"RM{caj:.2f}"

               total_keseluruhan = total + caj
      
      except : 
              print("Sila masukkan nombor sahaja")

      print("\n" * 5)
      print("=" * 30)
      print("      RESIT PESANAN ANDA")
      print("=" * 30)
      for item , kuantiti in bakul.items() :
          print(f"{item:15} x{kuantiti}")
      print("=" * 30)
      print(f"HARGA ASAL        : RM{total:.2f}")
      print(f"CAJ PENGHANTARAN  : RM{caj}")
      print(f"HARGA             : RM{total_keseluruhan}")
      print("=" * 30)
      print("TERIMA KASIH , SILA TUNGGU RIDER!")
      print("=" * 30)
    elif pilihan == 3 :
      print("------WAYANG KULIT UTARA------")
      total = 0
      try:
        ahli = int(input("Masukkan jumlah ahli : "))
        for i in range(ahli) :
          print(f"\n------Ahli Ke-{i+1}------")
          umur = int(input("Masukkan umur : "))
          if umur <= 12 :
            harga = 10
            print ("Kanak-kanak (bawah 12) RM 10")
          elif 13 <= umur <= 17 :
            harga = 15
            print("Remaja (13-17) RM 15")
          else : 
            harga = 20
            print("Dewasa (18 keatas) RM 20")
          total += harga
      
      except :
        print("SILA MASUKKAN NOMBOR SAHAJA,BUKAN NAMA.")

      print("\n" * 10)
      print("-----RESIT-----")
      print(f"JUMLAH AHLI  : {bilangan_ahli}")
      print(f"JUMLAH BAYAR : RM{total_bayaran}")
    elif pilihan == 4 :
      print("Terima Kasih ,jumpa lagi!")
    else :
      print("NOMBOR TIDAK SAH")
except :
  print("SILA MASUKKAN NOMBOR SAHAJA")
print("\n" * 10)
print("=" * 30)
print("SILA DATANG KEMBALI!")
print("=" * 30)
