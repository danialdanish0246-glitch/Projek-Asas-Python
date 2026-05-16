import time
import json

# ==========================================
# 1.  BARU ("w" - WRITE )
# ==========================================
print("Sistem Aktuari sedang dimulakan...")
time.sleep(3)
print("Sistem Sedia! Selamat kembali, Master Danial.")

with open("wishlist.txt", "w") as fail:
    fail.write("baju\n")
    fail.write("seluar\n")
print("Data berjaya dikunci ke dalam fail txt!\n")


# ==========================================
# 2.  TAMBAH DATA ("a" - APPEND )
# ==========================================
try:
    benda = input("masukkan objek yg nj tambah masuk dalam fail ni : ")
    with open("wishlist.txt", "a") as fail:
        fail.write(f"{benda}\n")
except:
    print("masukkan maklumat yg betul!")

print("loading.....")
time.sleep(2)
print(f"{benda} berjaya ditambah tanpa memadam Cili dan Sayur!\n")


# ==========================================
# 3.  BACA FAIL ("r" - READ )
# ==========================================
with open("wishlist.txt", "r") as fail:
    isi_kandungan = fail.read()

print("--- ISI KANDUNGAN FAIL TXT ---")
time.sleep(2)
print(isi_kandungan)


# ==========================================
# 4. TULIS DICTIONARY KEDALAM JSON ("w" - WRITE )
# ==========================================
profil_danial = {
    "nama": "Danial",
    "umur": 15,
    "wishlist": ["Cili", "Sayur", "Baju"]
}

with open("profil_simpanan.json", "w") as fail:
    json.dump(profil_danial, fail, indent=4)

print("Sedang menyunghilangkan data ke dalam bentuk skrol JSON...")
time.sleep(2)
print("Profil penuh berjaya dikunci secara kekal!\n")


# ==========================================
# 5.  MEMBACA FAIL JSON ("r" - READ )
# ==========================================
with open("profil_simpanan.json", "r") as fail:
    profil_terbaharu = json.load(fail)

print("loading............")
time.sleep(3)
print(f"nama : {profil_terbaharu['nama']}")
print(f"wishlist : {profil_terbaharu['wishlist']}")
