# Projek: Sistem Resit Kedai Runcit (Versi Pro)
# Dibuat oleh: Danial (Bakal Actuary)
# Ciri-ciri: Dictionary, Nested List, Error Handling, Alignment Format


bakul = {}
total = 0
tambah_lagi = "YA"

try :
  while tambah_lagi.upper() == "YA" :
    barang = input("MASUKKAN NAMA BARANG : ")
    unit = int(input("MASUKKAN BERAPA UNIT BARANG : "))
    harga = float(input("MASUKKAN HARGA BARANG : RM"))
    bakul[barang] = [unit , harga]
    tambah_lagi = input("NAK TAMBAH BARANG LAGI KA? (YA/TIDAK) :")
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
  total += info[0] * info[1]
  harga_teks = f"RM{harga:.2f}"
  print(f"{barang :<15} {unit :^10} {harga_teks :>10}")
print("=" * 40)
print(f"TOTAL (RM) : RM{total:.2f}")
print("=" * 40)
