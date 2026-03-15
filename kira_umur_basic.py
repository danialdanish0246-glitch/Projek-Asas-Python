def kira_umur(tahun_lahir,tahun_sekarang) :
  return tahun_sekarang - tahun_lahir

tahun_lahr = int(input("MASUKKAN TAHUN ANDA LAHIR   : "))
tahun_sekarng = int(input("MASUKKAN TAHUN SEKARANG  : "))
umur = kira_umur(tahun_lahr , tahun_sekarng)
print("\n" * 5)
print("=" * 10)
print(f"TAHUN : {tahun_sekarng}")
print(f"UMUR  : {umur}")
print("=" * 10)
