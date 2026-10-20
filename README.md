# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Alfitrah Zahra Ameliya  
NIM: 2225250181  
Kelas: 3B

## Tujuan

Mengolah kumpulan data numerik dengan list Python.

## Struktur Program

Folder `latihan` berisi program-program latihan untuk mempelajari penggunaan list Python, termasuk akses indeks, slicing, manipulasi elemen, dan pengolahan data numerik.

Folder `praktik` berisi program `analisis_nilai_mahasiswa.py` untuk mengolah data nilai mahasiswa, menghitung jumlah data, total nilai, rata-rata, nilai minimum, nilai maksimum, serta jumlah mahasiswa yang lulus dan belum lulus.

## Cara Menjalankan

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| No. | Data Uji | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | `[60, 70, 80]` | Rata-rata = 70.00 | Rata-rata = 70.00 | Berhasil |
| 2 | `[60, 70, 80]` | Minimum = 60 dan maksimum = 80 | Minimum = 60 dan maksimum = 80 | Berhasil |
| 3 | `[60, 70, 80]` | Jumlah mahasiswa lulus = 3 | Jumlah mahasiswa lulus = 3 | Berhasil |
| 4 | `[59, 60, 61]` | Jumlah mahasiswa lulus = 2 | Jumlah mahasiswa lulus = 2 | Berhasil |
| 5 | `[]` | Fungsi rata-rata menangani list kosong tanpa error | Rata-rata = 0.00 | Berhasil |

## Refleksi

Saya memahami bahwa list dapat digunakan untuk menyimpan beberapa data dalam satu variabel. Setiap elemen dapat diakses menggunakan indeks yang dimulai dari 0. Saya juga memahami penggunaan fungsi `len()`, `sum()`, `min()`, dan `max()` untuk membantu pengolahan data numerik.

Salah satu hal yang perlu diperhatikan adalah penanganan list kosong saat menghitung rata-rata. Jika list kosong, jumlah datanya adalah nol sehingga pembagian tidak dapat dilakukan. Oleh karena itu, fungsi rata-rata perlu memeriksa apakah list kosong terlebih dahulu agar program dapat berjalan tanpa error.