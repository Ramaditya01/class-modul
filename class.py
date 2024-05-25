class Laci:
    def __init__(self):
        self.tumpukan = []
    
    def tambah_berkas(self, berkas):
        self.tumpukan.append(berkas)
        print(f"Berkas '{berkas}' telah ditambahkan ke dalam laci.")
    
    def ambil_berkas(self):
        if not self.tumpukan:
            print("Laci kosong. Tidak ada berkas untuk diambil.")
            return None
        berkas = self.tumpukan.pop()
        print(f"Berkas '{berkas}' telah diambil dari laci.")
        return berkas
    
    def lihat_berkas_teratas(self):
        if not self.tumpukan:
            print("Laci kosong.")
            return None
        print(f"Berkas teratas di dalam laci adalah '{self.tumpukan[-1]}'.")
        return self.tumpukan[-1]
    
    def apakah_kosong(self):
        is_empty = len(self.tumpukan) == 0
        if is_empty:
            print("Laci kosong.")
        else:
            print("Laci tidak kosong.")
        return is_empty
    
    def jumlah_berkas(self):
        count = len(self.tumpukan)
        print(f"Terdapat {count} berkas di dalam laci.")
        return count

laci = Laci()

laci.tambah_berkas("Berkas A")
laci.tambah_berkas("Berkas B")
laci.tambah_berkas("Berkas C")

laci.lihat_berkas_teratas()

laci.ambil_berkas()
laci.lihat_berkas_teratas()

laci.jumlah_berkas()
laci.apakah_kosong()

laci.ambil_berkas()
laci.ambil_berkas()

laci.apakah_kosong()