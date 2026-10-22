# Modul Praktikum Pertemuan 5
# Algoritma dan Struktur Data: Tipe Data, Variabel, dan Operator Python

print("=== Praktikum 1: Mengenali Tipe Data ===")
nama = "Lindi"
umur = 19
berat = 54.5
terdaftar = True
print("Nama:", nama, "| Tipe:", type(nama))
print("Umur:", umur, "| Tipe:", type(umur))
print("Berat:", berat, "| Tipe:", type(berat))
print("Terdaftar:", terdaftar, "| Tipe:", type(terdaftar))
umur = 20
print("Umur setelah diubah:", umur, "| Tipe:", type(umur))

print("\n=== Praktikum 2: Operator Aritmatika ===")
harga = 12500
jumlah = 4
total = harga * jumlah
sisa = total % 2000
total_diskon = total - 5000
print("Harga per buku: Rp", harga)
print("Jumlah buku:", jumlah)
print("Total harga: Rp", total)
print("Sisa pembagian total dengan 2.000:", sisa)
print("Total setelah diskon Rp5.000: Rp", total_diskon)

print("\n=== Praktikum 3: Operator Perbandingan dan Logika ===")
nilai = 82
kehadiran = 90
syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80
print("Memenuhi syarat nilai:", syarat_nilai)
print("Memenuhi syarat kehadiran:", syarat_kehadiran)
print("Lulus dengan and:", syarat_nilai and syarat_kehadiran)
print("Lulus dengan or:", syarat_nilai or syarat_kehadiran)
nilai = 70
syarat_nilai = nilai >= 75
print("Nilai setelah diubah:", nilai)
print("Lulus dengan and setelah nilai diubah:", syarat_nilai and syarat_kehadiran)
print("Lulus dengan or setelah nilai diubah:", syarat_nilai or syarat_kehadiran)

print("\n=== Praktikum 4: Operator Penugasan ===")
poin = 100
print("Nilai awal:", poin)
poin += 25
print("Setelah += 25:", poin)
poin -= 10
print("Setelah -= 10:", poin)
poin *= 2
print("Setelah *= 2:", poin)
poin /= 2
print("Setelah /= 2:", poin)

print("\n=== Praktikum 5: Struktur Data Dasar ===")
nilai = [78, 85, 90, 85]
mahasiswa = {"nama": "Lindi", "kelas": "IF-A"}
koordinat = (5, 8)
angka = {2, 4, 4, 6, 8}
print("Nilai pertama:", nilai[0])
nilai.append(95)
print("List terbaru:", nilai)
print("Nama mahasiswa:", mahasiswa["nama"])
print("Koordinat pertama:", koordinat[0])
print("Angka unik:", sorted(angka))

print("\n=== Tantangan Terintegrasi: Program Rekap Nilai ===")
def rekap_nilai(nama, nilai_tugas, nilai_ujian):
    rata_rata = (nilai_tugas + nilai_ujian) / 2
    lulus = rata_rata >= 75
    print("Nama:", nama)
    print("Nilai tugas:", nilai_tugas)
    print("Nilai ujian:", nilai_ujian)
    print("Rata-rata:", rata_rata)
    print("Status lulus:", lulus)
    print("-" * 30)

rekap_nilai("Lindi", 80, 90)
rekap_nilai("Dhea", 70, 65)
