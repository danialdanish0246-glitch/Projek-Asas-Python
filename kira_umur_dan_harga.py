def kira_umur(tahun_lahir,tahun_sekarang) :
  return tahun_sekarang - tahun_lahir
def kira_harga(umur) :
  if umur < 18 :
    return 100
  elif 18 <= umur <= 50 :
    return 250
  else : 
    return 500
tahun_lahir = int(input("MASUKKAN TAHUN ANDA LAHIR   : "))
tahun_sekarang = int(input("MASUKKAN TAHUN SEKARANG  : "))
umur = kira_umur(tahun_lahir  , tahun_sekarang)
harga = kira_harga(umur)
print("\n" * 5)
print("=" * 10)
print(f"UMUR  : {umur} tahun")
print(f"HARGA : RM{harga:.2f} ")
print("=" * 10)
