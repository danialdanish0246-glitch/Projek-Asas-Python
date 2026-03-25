print("---------Sistem Tol Lebuhraya (TNG)----------")
duit = 50.00

try:
  tol = float(input("Sila imbas kad (Masukkan kadar tol): RM"))
  if duit < tol :
    print("BAKI TIDAK MENCUKUPI. SILA TAMBAH NILAI.")
  elif tol <= 0 :
    print("RALAT: KADAR TOL TIDAK SAH.")
  else :
    hasil = duit - tol

  if tol >= 10 :
    hasil += 0.50
except:
  print("MASUKKAN NOMBOR SAHAJA")

print("\n" * 10)
print("==========================")
print(f"HARGA TOL : {tol:.2f}")
print(f"BAKI : {hasil:.2f}")
