moreh = {}
tambah_lagi = "YA"
total = 0

try:
  while tambah_lagi.upper() == "YA" :
    nama = input("MASUKKAN NAMA ANDA : ")
    makanan = input("MASUKKAN MAKANAN YANG INGIN DIBAWA : ")
    harga = float(input("MASUKKAN HARGA MAKANAN MAKANAN : RM"))
    moreh[nama] = [makanan , harga]
    tambah_lagi = input("ADAKAH ANDA INGIN MENAMBAH LAGI (YA/TIDAK) : ")
    total += harga
    if  tambah_lagi.upper() != "YA" :
      break
except:
  print("MASUKKAN NOMBOR ATAU HURUF PADA TEMPAT YANG BETUL!")
total_makanan = len(moreh)
print("\n" * 5 + "=" * 20)
for nama , info in moreh.items() :
  makanan = info[0]
  harga = info[1]
  print(f"-{nama} bawa {makanan} dengan harga RM{harga:.2f}.")
print(f"TOTAL MAKANAN : {total_makanan}")
print("=" * 20)
