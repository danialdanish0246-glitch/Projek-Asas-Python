def kira_untung(harga_beli,harga_jual,unit,caj_beli,caj_jual) :
   duit_kasar = ( harga_jual - harga_beli ) * unit
   return duit_kasar - (caj_beli + caj_jual)
try :
  caj_beli = 8
  caj_jual = 8
  unit = int(input("MASUKKAN UNIT NK BELI : "))
  harga_beli = float(input("MASUKKAN HARGA BELI (per syer) : RM"))
  harga_jual = float(input("MASUKKAN HARGA JUAL (per syer) : RM"))
  duit_bersih = kira_untung(harga_beli,harga_jual,unit,caj_beli,caj_jual)
  duit_kasar =  harga_beli  * unit 
  if duit_bersih > 0 :
    print("UNTUNG!!!!!")
  else :
    print("RUGI!!")
  duit_bersih = round(duit_bersih,2)
  peratus = (duit_bersih / duit_kasar) * 100
  peratus = round(peratus,2) 

  print(f"JUMLAH UNTUNG  : RM{duit_bersih}")
  print(f"PERATUS UNTUNG : {peratus}%")
except ZeroDivisionError:
    print("Harga beli tak boleh 0!")
except :
  print("MASUKKAN NOMBOR SAHAJA!")
