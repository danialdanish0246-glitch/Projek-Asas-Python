import time

def kira_umur(tahun_sekarang,tahun_lahir) :
  tahun = tahun_sekarang - tahun_lahir
  return tahun
wishlist = []
barang_buang = "Tiada"
try :
  nama = input("masukkan nama anda : ")
  tahun_sekarang = int(input("masukkan tahun sekarang : "))
  tahun_lahir = int(input("masukkan tahun lahir anda : "))
  umur = kira_umur(tahun_sekarang,tahun_lahir)
  if umur > 0 :
    print(f"tahniah, umur anda sekarang ialah {umur}.")
  else :
    print("umur tidak sah!")
  cita_cita = input("masukkan cita cita anda : ")
  target = float(input("masukkan target simpanan anda : RM"))
  berapa_barang = int(input("masukkan berapa barang nk beli : "))
  for i in range(berapa_barang) :
    barang = input("barang apa nk beli : ")
  wishlist.append(barang)
  while True :
    buang = input("ada barang nk buang dak (YA/TIDAK) : ").upper()
    if buang == "YA" :
      apa = int(input("nak buang indeks yang mana! : "))
      print("Sistem sedang bermula...")
      if apa >= 0 and apa < len(wishlist):
        time.sleep(2)
        barang_buang = wishlist.pop(apa)
        print(wishlist)
        print("barang berjaya dibuang!")
      else :
        print("masukkan maklumat yang betul!")
        break
    else :
      break
  profil = {"nama": nama, "umur": umur, "cita cita" : cita_cita, "senarai keinginan" : wishlist}
  print(f"nama saya {nama} dan saya ingin menjadi {cita_cita}.")
  print(f"umur saya {umur} tahun dan target simpanan saya ialah RM{target:.2f}")
  print(profil)
  print(f"barang yang dibuang atau dikeluarkan ialah {barang_buang}")
except :
  print("masukkan maklumat yang betul !")
