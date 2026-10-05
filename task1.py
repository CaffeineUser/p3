# LANGKAH 1: Impor modul
# Modul random menyediakan fungsi pembangkit bilangan acak.
import random
 
# LANGKAH 2: Definisikan konfigurasi pengujian
LOW, HIGH = 1, 20      # batas bawah dan atas rentang valid (0 < x <= 20, integer)
NUM_TESTS = 10         # jumlah test case yang akan dibangkitkan
 
 
# LANGKAH 3: Buat fungsi yang mensimulasikan program yang diuji
def program_under_test(x: int) -> bool:
    """Simulasi program yang diuji: menerima x valid (LOW..HIGH)."""
    # Mengembalikan True jika x berada dalam rentang valid, False jika tidak
    return LOW <= x <= HIGH
 
 
# LANGKAH 4: Buat fungsi pembangkit test case secara acak
def random_testing(n: int, seed=None):
    # 4a. Jika seed diberikan, kunci pembangkit acak agar hasil bisa diulang
    if seed is not None:
        random.seed(seed)          # seed tetap -> hasil bisa direproduksi
    # 4b. Bangkitkan n bilangan acak; randint = distribusi uniform diskrit,
    #     sehingga setiap nilai 1..20 berpeluang sama (1/20 = 5%)
    return [random.randint(LOW, HIGH) for _ in range(n)]
 
 
# LANGKAH 5: Blok utama, dijalankan saat berkas dieksekusi langsung
if __name__ == "__main__":
    # 5a. Bangkitkan 10 test case acak
    test_cases = random_testing(NUM_TESTS)
 
    # 5b. Cetak judul dan header tabel hasil
    print(f"Random Testing | Rentang valid: {LOW} <= x <= {HIGH}\n")
    print(f"{'No':<4}{'Input x':<10}{'Hasil':<8}")
 
    # 5c. Jalankan setiap test case terhadap program yang diuji
    for i, x in enumerate(test_cases, 1):
        # Bandingkan hasil dengan harapan: valid -> PASS, selain itu -> FAIL
        status = "PASS" if program_under_test(x) else "FAIL"
        # Cetak nomor test case, nilai input, dan statusnya
        print(f"{i:<4}{x:<10}{status:<8}")
 
    # 5d. Cetak ringkasan: seluruh test case dan jumlah nilai uniknya
    print(f"\nTest case dipilih: {test_cases}")
    print(f"Nilai unik: {len(set(test_cases))} dari {NUM_TESTS}")