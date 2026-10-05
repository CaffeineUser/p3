# Random Testing: Uniform & Operational Distribution

Simulasi *random testing* dengan Python untuk program yang menerima satu parameter `int x` pada rentang valid **1 ≤ x ≤ 20**. Setiap program memilih **10 test case** secara acak.

## Isi Repositori

| Berkas | Pendekatan | Fungsi Python |
|---|---|---|
| `task1.py` | Uniform distribution | `random.randint()` |
| `task2.py` | Operational distribution | `random.choices()` |

## Cara Menjalankan

Membutuhkan Python 3.6+ (hanya modul bawaan, tanpa instalasi tambahan).

```bash
python task1.py
python task2.py
```

## Penjelasan Singkat

### 1. Uniform Distribution
Setiap nilai 1 sampai 20 punya peluang sama (1/20 = 5%). Tiap test case dijalankan ke `program_under_test()` dan dicetak berstatus `PASS` atau `FAIL`. Seed bisa diatur lewat `random_testing(n, seed=...)` agar hasil dapat diulang.

### 2. Operational Distribution
Peluang tiap nilai mengikuti profil penggunaan dari 50 pengamatan:

| Nilai x | Frekuensi | Peluang |
|---|---|---|
| 1 | 10 | 20% |
| 2, 8, 9, 20 | 5 per nilai | 10% |
| 10, 11, 12, 13, 14 | 2 per nilai | 4% |
| 3-7, 15-19 | 1 per nilai | 2% |

Program memvalidasi total frekuensi (50) dan kelengkapan nilai 1 sampai 20, lalu memilih test case dengan `random.choices(nilai_x, weights=bobot, k=10)`. Kode memakai `random.seed(42)`; hapus baris itu untuk hasil acak penuh.

## Contoh Keluaran (seed 42, operational)

```
Daftar test case : [10, 1, 2, 2, 13, 11, 19, 1, 8, 1]
Ringkasan terpilih: {1: 3, 2: 2, 8: 1, 10: 1, 11: 1, 13: 1, 19: 1}
```

## Perbandingan

| Aspek | Uniform | Operational |
|---|---|---|
| Peluang tiap nilai | Sama (5%) | Sebanding frekuensi (2%-20%) |
| Kelebihan | Cakupan domain merata | Fokus pada nilai yang sering dipakai |
| Kekurangan | Mengabaikan pola penggunaan | Nilai jarang (3-7, 15-19) mudah terlewat |

## Catatan

- Pemilihan dilakukan **dengan pengembalian**, sehingga nilai yang sama bisa muncul lebih dari sekali. Gunakan `random.sample()` bila ingin tanpa duplikasi.
- Random testing murni tidak menjamin nilai batas (1 dan 20) terpilih. Kombinasikan dengan *boundary value analysis* dan uji nilai di luar rentang (0, 21, negatif).
- Soal awal menulis rentang `0 > x ≥ 20` yang mustahil secara matematis; diinterpretasikan sebagai `0 < x ≤ 20`.