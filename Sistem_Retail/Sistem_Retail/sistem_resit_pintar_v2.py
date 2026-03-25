# Sistem Resit Barang dengan Diskaun
bakul = {}
tambah_lagi = "YA"
total_kasar = 0
try :
 while tambah_lagi.upper() == "YA" :
    barang = input("MASUKKAN NAMA BARANG : ")
    unit = int(input("MASUKKAN BERAPA UNIT BARANG : "))
    harga = float(input("MASUKKAN HARGA BARANG : RM"))
    bakul[barang] = [unit , harga]
    tambah_lagi = input("NAK TAMBAH BARANG LAGI KA? (YA/TIDAK) : ")
    if tambah_lagi.upper() != "YA" :
      break
except :
  print("MASUKKAN NOMBOR ATAU HURUF PADA RUANG YANG BETUL!")
print("\n" * 5 + "=" * 40)
print("                RESIT ANDA ")
print("=" * 40)
print(f"{'items':<15} {'qty':^10} {'(RM)':>10}")
print("-" * 40)
for barang , info in bakul.items() :
      unit = info[0]
      harga = info[1]
      harga_teks = f"RM{harga:.2f}"
      total = info[0] * info[1]
      total_kasar += total
      print(f"{barang :<15} {unit :^10} {harga_teks :>10}")
if total_kasar > 100 :
      diskoun = total_kasar * 0.10
else:
      diskoun = 0
total_bersih = total_kasar - diskoun
print("=" * 40)
print(f"TOTAL SEBELUM DISKOUN (RM) : RM{total_kasar:.2f}")
print(f"TOTAL SELEPAS DISKOUN (RM) : RM{total_bersih:.2f}")
print("=" * 40)
