class PesawatTerbang:
    def __init__(self, maskapai, tujuan, Jam_terbang):
     self.maskapai = maskapai
     self.tujuan = tujuan
     self.Jam_terbang = Jam_terbang
    def info(self):
     print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}\nJam_terbang; {self.Jam_terbang}")
pesawatA = PesawatTerbang("Batik Air", "Jakarta - Palembang", "15.30 WIB")
pesawatA.info()