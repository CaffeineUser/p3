import random                                   # modul untuk pengambilan sampel acak
from collections import Counter                 # untuk menghitung frekuensi hasil pilihan

# Profil operasional: frekuensi kemunculan tiap nilai x dari 50 pengamatan
frekuensi = {
    1: 10,                                      # x = 1 paling sering muncul (10 kali)
    2: 5, 8: 5, 9: 5, 20: 5,                    # x = 2, 8, 9, 20 masing-masing 5 kali
    10: 2, 11: 2, 12: 2, 13: 2, 14: 2,          # x = 10..14 masing-masing 2 kali
    3: 1, 4: 1, 5: 1, 6: 1, 7: 1,               # x = 3..7 masing-masing 1 kali
    15: 1, 16: 1, 17: 1, 18: 1, 19: 1,          # x = 15..19 masing-masing 1 kali
}

TOTAL_SAMPEL = 50                               # total pengamatan pada profil operasional
JUMLAH_TEST = 10                                # jumlah test case yang akan dipilih

# Validasi: jumlah frekuensi harus sama dengan total sampel pengamatan
assert sum(frekuensi.values()) == TOTAL_SAMPEL, "Total frekuensi tidak sama dengan 50"

# Validasi: semua nilai pada rentang 1..20 harus terdefinisi di profil
assert set(frekuensi) == set(range(1, 21)), "Ada nilai x yang belum terdefinisi"

nilai_x = sorted(frekuensi.keys())              # daftar nilai x yang diurutkan (1..20)
bobot = [frekuensi[x] for x in nilai_x]         # bobot tiap nilai = frekuensinya

# Probabilitas operasional tiap nilai = frekuensi / total sampel
probabilitas = {x: frekuensi[x] / TOTAL_SAMPEL for x in nilai_x}

random.seed(42)                                 # seed tetap agar hasil dapat direproduksi (hapus untuk acak penuh)

# Pemilihan 10 test case: peluang terpilih sebanding dengan bobot (dengan pengembalian)
test_cases = random.choices(nilai_x, weights=bobot, k=JUMLAH_TEST)

# Cetak profil operasional sebagai referensi
print("=== Profil Operasional ===")              # judul bagian profil
print(f"{'x':<4}{'Frekuensi':<12}{'Probabilitas':<12}")  # header tabel profil
for x in nilai_x:                               # iterasi setiap nilai x dari 1 sampai 20
    print(f"{x:<4}{frekuensi[x]:<12}{probabilitas[x]:<12.2f}")  # cetak x, frekuensi, probabilitas

# Cetak hasil test case terpilih
print("\n=== 10 Test Case Terpilih (Operational Distribution) ===")  # judul hasil
for i, x in enumerate(test_cases, start=1):     # iterasi test case dengan nomor urut mulai dari 1
    print(f"Test Case {i:>2}: x = {x:<3} (peluang {probabilitas[x]:.0%})")  # cetak nilai x dan peluangnya

print(f"\nDaftar test case : {test_cases}")      # cetak seluruh test case dalam bentuk list

# Ringkasan frekuensi nilai yang terpilih
ringkasan = Counter(test_cases)                 # hitung berapa kali tiap nilai terpilih
print(f"Ringkasan terpilih: {dict(sorted(ringkasan.items()))}")  # cetak ringkasan terurut