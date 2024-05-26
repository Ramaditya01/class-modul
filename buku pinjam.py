class Anggota:
  def _init_(self, nama, ID):
    self. nama=[Adit]
    self. ID=[TI20230001]
    self. buku pinjaman=[segitiga biru]
  def tampilkan buku_pinjaman (self):
    if self. buku pinjaman:
      print(f"-- Buku pinjaman {self.nama}--")
      for buku in self. buku_pinjaman:
        print(buku)
    else:
      print(f"{self.nama}tidak memiliki buku pinjaman. ")

def main():
  #buat beberapa buku
  buku1 =Buku(" dunia","Dalgona","Fiksi","Tersedia")
  buku2 =Buku("segitiga biru","Jarot Gatot","Fiksi","Tersedia")
  buku3 =Buku("Filosofi Kopi", "Mentari Hapsari"," Fiksi","Dipinjam")
  
  #Buat Perpustakaan dan anggota
  perpustakaan = Perpustakaan {}
  perpustakaan. koleksi_buku.extended([buku1, buku2, buku3])
  
  anggota1= Anggota ("Abas",5646)
  anggota2= Anggota ("Dragon",9991)
  
  #Jalankan program
  print("\n -- Menu Perpustakaan--")
  print("1.Tampilkan Daftar Buku")
  print("2. Cari Buku")
  print("3. Pinjam Buku")
  print("4. Kembalikan")
  angka=int(input("pilih menu:_"))
  
  if angka == 1:
    perpustakaan tampilkan_buku();
  elif angka == 2:
    judul=input("input judul buku:")
    perpustakaan. cari_buku(judul);
  elif angka == 3:
    buku=input ("buku yang dipinjam:")
    anggota=input("input nama anggota:")
    perpustakaan. pinjam_buku(buku, anggota)
  else:
    print("anda salah pilih")
  
  if _name_=="_main":
    main();
   