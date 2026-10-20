# Input: Data nilai mahasiswa dalam bentuk list.
# Proses: Menghitung banyak data, total nilai, rata-rata,
# nilai minimum, dan nilai maksimum. Memisahkan nilai
# yang lulus dan belum lulus berdasarkan batas nilai 60.
# Output: Menampilkan data nilai, hasil statistik,
# daftar nilai lulus, jumlah mahasiswa lulus,
# dan jumlah mahasiswa belum lulus.

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

print("Data nilai mahasiswa =", nilai)
print("Banyak data =", len(nilai))
print("Total nilai =", sum(nilai))
print(f"Rata-rata = {rata_rata(nilai):.2f}")
print("Nilai minimum =", min(nilai))
print("Nilai maksimum =", max(nilai))

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = len(nilai) - jumlah_lulus

print("Nilai lulus =", lulus)
print("Jumlah mahasiswa lulus =", jumlah_lulus)
print("Jumlah mahasiswa belum lulus =", jumlah_belum_lulus)