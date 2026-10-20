# Input: Data nilai mahasiswa dalam bentuk list.
# Proses: Menghitung total, rata-rata, nilai minimum,
# dan nilai maksimum menggunakan fungsi agregasi.
# Output: Menampilkan total, rata-rata, nilai minimum,
# dan nilai maksimum.

nilai = [75, 80, 65, 90, 88]
print(f"Total = {sum(nilai)}")
print(f"Rata-rata = {sum(nilai)/len(nilai):.2f}")
print(f"Minimum = {min(nilai)}")
print(f"Maksimum = {max(nilai)}")