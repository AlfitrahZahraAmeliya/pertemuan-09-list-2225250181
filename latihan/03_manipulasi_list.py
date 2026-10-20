# Input: Data nilai mahasiswa dalam bentuk list.
# Proses: Mengubah elemen, menambahkan elemen dengan append(),
# menyisipkan elemen dengan insert(), dan menghapus elemen
# dengan remove().
# Output: Menampilkan list setelah dilakukan manipulasi.

nilai = [75, 80, 65]
nilai[1] = 82
nilai.append(90)
nilai.insert(1, 70)
nilai.remove(65)
print(nilai)