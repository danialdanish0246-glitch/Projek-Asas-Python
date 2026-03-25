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
