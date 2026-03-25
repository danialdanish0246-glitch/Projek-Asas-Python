moreh = {}
tambah_lagi = "YA"
try:
 while tambah_lagi.upper() == "YA":
    nama = input("Siapa nama kawan? : ")
    benda = input("Dia bawa apa?    : ")
    moreh[nama] = benda
    tambah_lagi = input("Ada lagi dk orang nak bawa (ya/tidak)? :")
    if not tambah_lagi == "ya" :
      break
except:
  print("Masukkan huruf sahaja")
print("\n" * 10 + "=" * 20 )
print("SENARAI MOREH MALAM NI")
print("="*20)

for nama , benda in moreh.items() :
  print(f"-{nama} bawa {benda}")
print("=" * 20)
