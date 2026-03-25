print("------------Sistem Tiket Parking Mall------------")

try:
  masa = int(input("MASUKKAN BERAPA JAM NK PARKING : "))

  if masa == 1 :
    harga = 2
  else :
    harga = 2 + (masa - 1)

  if harga > 5 :
    harga -= 1
except:
  print("masukkan nombor sahaja ")
print("\n" * 10)
print("-" * 10)
print("-" * 10)
print(f"MASA  : RM{masa}")
print(f"HARGA : RM{harga}")
