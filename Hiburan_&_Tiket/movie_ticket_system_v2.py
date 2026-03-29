total = 0
maklumat = {}
tambah_lagi = "YA"

def kira_harga(umur) :
     if umur < 12 :
      return 10
     elif 13 <= umur <= 17 :
      return 15
     else :
      return 20
try :
  while True :
            nama = input("MASUKKAN NAMA ANDA : ")
            umur = int(input("MASUKKAN UMUR ANDA : "))
            harga = kira_harga(umur)
            total += harga
            maklumat[nama] = [umur , harga]
            tambah_lagi = input("ADA ORANG LAGI (YA/TIDAK) ? :").upper()
            if tambah_lagi.upper() != "YA" :
             break
except :
  print("SLIA MASUKKAN NOMBOR ATAU HURUF PADA RUANGAN YANG BETUL !")

print("\n" * 5 + "=" * 40)
print("                RESIT ANDA ")
print("=" * 40)
print(f"{'items':<15} {'qty':^10} {'(RM)':>10}")
print("-" * 40)
for nama , info in maklumat . items() :
      umur = info[0]
      harga_item = info[1]
      harga_teks = f"RM{harga_item:.2f}"
      print(f"{nama :<15} {umur :^10} {harga_teks :>10}")
print("=" * 40)
print(f"TOTAL  (RM) : RM{total:.2f}")
print("=" * 40)
