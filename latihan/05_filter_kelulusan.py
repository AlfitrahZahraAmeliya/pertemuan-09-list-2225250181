# Input: Data nilai mahasiswa dalam bentuk list.
# Proses: Memeriksa setiap nilai dan memilih nilai yang
# memenuhi batas kelulusan, yaitu nilai minimal 60.
# Output: Menampilkan daftar nilai yang lulus
# dan jumlah nilai yang lulus.

nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")