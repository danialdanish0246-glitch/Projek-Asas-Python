print("------WAYANG KULIT UTARA------")
total_bayaran = 0

try:
  bilangan_ahli = int(input("MASUKKAN BILANGAN AHLI : "))

  for i in range(bilangan_ahli):
      print(f"\n------Ahli ke-{i+1}------")
      umur = int(input("MASUKKAN UMUR : "))


      if umur <= 12 :
        harga_individu = 10
        print("Kanak-kanak (bawah 12): RM10")
      elif 13 <= umur <=17 :
        harga_individu = 15
        print("Remaja (13-17): RM15")
      else :
        harga_individu = 20
        print("Dewasa (18 ke atas): RM20") 

      total_bayaran += harga_individu

except :
    print("SILA MASUKKAN NOMBOR SAHAJA,BUKAN NAMA.")

print("\n" * 10)

print("-----RESIT-----")
print(f"JUMLAH AHLI  : {bilangan_ahli}")
print(f"JUMLAH BAYAR : RM{total_bayaran}")
