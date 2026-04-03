#KIRA UNTUNG
def kira_untung(unit_syer,harga_persyer,harga_persyer_jual,harga_total_beli_syer) :
  untung = harga_persyer_jual - harga_persyer
  untung *= unit_syer
  return (untung / harga_total_beli_syer) * 100
try :

 unit_syer = int(input("MASUKKAN UNIT SYER : "))
 harga_persyer = float(input("MASUKKAN HARGA PERSYER : RM"))
 harga_persyer_jual = float(input("MASUKKAN HARGA MENJUAL PERSYER : RM"))
 harga_total_syer_jual = int(input("MASUKKAN HARGA ANDA BELI SYER : RM"))
 untung = kira_untung(unit_syer,harga_persyer,harga_persyer_jual,harga_total_syer_jual)
 untung = round(untung,2)
except :
  print("MASUKKAN NOMBOR SAHAJA !")

print(f"UNTUNG ANDA DARIPADA HARGA ASAL IAITU RM{harga_total_syer_jual} IALAH SEBANYAK {untung}%")
