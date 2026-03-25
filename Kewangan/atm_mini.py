print("-------Sistem ATM Mini-------")
baki = 1000

try:
  keluar = float(input("SILA MASUKKAN JUMLAH DUIT YANG INGIN KELUAR : RM"))
  if keluar > baki :
    print("DUIT BANK TIDAK CUKUP")
  elif keluar <= 0 :
    print("JUMLAH TIDAK SAH!")
  else :
    print(f"JUMLAH DUIT : RM{keluar}")

  if keluar > 500 :
    baki -= 1

  duit_dalam_bank = baki - keluar
except:
  print("SILA MASUKKAN NOMBOR SAHAJA")
print("\n" * 10)
print("------RESIT------")
print(f"DUIT KELUAR : RM{keluar} ")
print(f"BAKI BANK : RM{ duit_dalam_bank:.2f}")
