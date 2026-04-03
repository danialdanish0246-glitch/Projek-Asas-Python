# ============================================================
# AUTHOR: Danial
# Beginner level: Exploring Sentinel Search algorithm.
# Just started learning Python. Still practicing my logic!
# PROJECT: Sentinel Search Algorithm
# ============================================================
def sentinel_search(senarai,target) :
  n = len(senarai)

  elemen_terakhir = senarai[n - 1]
  senarai[n -1] = target
  i = 0
  while senarai[i] != target :
    i += 1
  senarai[n - 1] = elemen_terakhir 
  if (i < n - 1) or (senarai[n - 1] == target) :
    return f"dh jumpa,berada dekat senarai ke-{i}"
  else :
    return "tak jumpa"
berapa_nk_masuk = int(input("nak masuk berapa nombor : "))
nombor_list = []
for i in range(berapa_nk_masuk) :
    nombor = int(input(f"masukkan nombor ke-{i} :"))
    nombor_list.append(nombor)
cari = int(input("masukkan nombor nk cari : "))
result = sentinel_search(nombor_list,cari)
print(result)
