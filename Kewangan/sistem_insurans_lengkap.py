def kira_umur(tahun_lahir,tahun_sekarang) :
  return tahun_sekarang - tahun_lahir
def kira_harga(umur) :
  if umur < 18 :
    return 100
  elif 18 <= umur <= 50 :
    return 250
  else : 
    return 500
def kira_diskaun(harga , status) :
  if status .upper() == "VIP" :
    return harga * 0.8
  else :
    return harga
tahun_lahir = int(input("MASUKKAN TAHUN LAHIR ANDA   : "))
tahun_sekarang = int(input("MASUKKAN TAHUN SEKARANG  : "))
status = input("MASUKKAN STATUS ANDA (VIP/BIASA)     : ")
umur = kira_umur(tahun_lahir , tahun_sekarang)
harga = kira_harga(umur)
harga_premium = kira_diskaun(harga , status)

print("\n" * 5)
print("=" * 30)
print(f"UMUR : {umur} TAHUN")
print(f'STATUS : {status}')
print(f"HARGA  : {harga_premium:.2f}")
print("=" * 30)
print("TERIMA KASIH KERANA TELAH")
print("BERBAKTI KEPADA SYARIKAT KAMI.")
